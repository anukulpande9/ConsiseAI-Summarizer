import nltk
import torch
import logging
import threading
from queue import Queue
from nltk.tokenize import sent_tokenize
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Download necessary NLTK components
nltk.download("punkt")

# Configure logging for debugging and monitoring
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load T5 model and tokenizer for summarization
logging.info("Loading T5 tokenizer and model for summarization...")
tokenizer = T5Tokenizer.from_pretrained("t5-large")
model = T5ForConditionalGeneration.from_pretrained("t5-large")

# Check for GPU availability
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device, "\n")
model.to(device)

# Global settings
MAX_INPUT_LENGTH = 1024  # Token limit for the model
THREAD_COUNT = 4  # Number of parallel threads for summarization

def preprocess_text(text):
    """Cleans input text by removing unnecessary characters and formatting issues."""
    return text.replace("\n", " ").replace("\r", " ").strip()

def adjust_summary_length(text_length):
    """
    Dynamically adjusts the min/max summary length based on input text size.
    """
    if text_length < 500:
        return 100, 200
    elif text_length < 2000:
        return 250, 500
    elif text_length < 5000:
        return 400, 800
    else:
        return 500, 1000

def split_text(text, chunk_size=MAX_INPUT_LENGTH):
    """
    Splits large text into chunks that fit within the token limit.
    Splitting is done on sentence boundaries.
    """
    sentences = sent_tokenize(text)
    chunks, current_chunk = [], ""
    for sentence in sentences:
        if len(tokenizer.encode(current_chunk + " " + sentence)) <= chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence  # Start a new chunk
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def summarize_chunk(chunk, min_length, max_length):
    """
    Summarizes a single chunk of text using T5.
    Prepend the "summarize:" prefix to instruct the model to perform summarization.
    """
    try:
        input_text = "summarize: " + chunk
        input_tokens = tokenizer.encode(
            input_text, return_tensors="pt", max_length=MAX_INPUT_LENGTH, truncation=True
        ).to(device)
        
        summary_tokens = model.generate(
            input_tokens,
            max_length=max_length,
            min_length=min_length,
            do_sample=True,          # Enable sampling for more abstraction
            temperature=0.7,
            num_beams=4,
            early_stopping=True,
        )
        
        summary = tokenizer.decode(summary_tokens[0], skip_special_tokens=True)
        logging.info(f"Generated summary: {summary}")
        return summary
    except Exception as e:
        logging.error(f"Error in summarization: {e}")
        return None

def summarize_worker(queue, results, min_length, max_length):
    """
    Worker function for parallel processing of text chunks.
    """
    while not queue.empty():
        try:
            index, chunk = queue.get_nowait()
            logging.info(f"Processing chunk {index + 1}...")
            summary = summarize_chunk(chunk, min_length, max_length)
            if summary:
                results[index] = summary
            queue.task_done()
        except Exception as e:
            logging.error(f"Worker encountered an error: {e}")

def summarize_text_parallel(text):
    """
    Summarizes large text by:
      - Preprocessing and splitting it into manageable chunks.
      - Running parallel summarization on each chunk.
      - Merging the summarized chunks into a final output.
    """
    try:
        # Preprocess text
        text = preprocess_text(text)
        text_length = len(text.split())
        
        # Adjust summary length parameters based on input size
        min_length, max_length = adjust_summary_length(text_length)
        
        # Split text into chunks
        text_chunks = split_text(text)
        num_chunks = len(text_chunks)
        logging.info(f"Text split into {num_chunks} chunks for parallel summarization.")
        
        # If text fits in one chunk, summarize directly
        if num_chunks == 1:
            return True, summarize_chunk(text_chunks[0], min_length, max_length)
        
        # Set up multithreading
        queue = Queue()
        results = [None] * num_chunks  # Placeholder for storing results
        
        for i, chunk in enumerate(text_chunks):
            queue.put((i, chunk))
        
        threads = []
        for _ in range(min(THREAD_COUNT, num_chunks)):
            thread = threading.Thread(target=summarize_worker, args=(queue, results, min_length, max_length))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        # Merge summarized chunks
        final_summary = " ".join(filter(None, results)).strip()
        return True, final_summary
    
    except Exception as e:
        logging.error(f"Summarization failed: {str(e)}")
        return False, str(e)
