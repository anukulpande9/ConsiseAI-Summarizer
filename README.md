
# 🌟 ConsiseAI – AI-Based Document Summarization Tool

🚀 **ConsiseAI** is a robust AI-powered tool for summarizing **text, PDFs, Word documents, and even audio/video transcriptions!**  
It combines the power of **T5 Transformer** for abstractive summarization and **OpenAI Whisper** for speech-to-text transcription.

---

## 🔹 Features

- **AI-Powered Summarization** – Leverages **T5-large** for high-quality abstractive summaries.
- **Multi-format Support** – Handles **Text, PDF, DOCX, MP3, MP4, WAV, FLAC**.
- **Speech-to-Text Integration** – Uses **OpenAI Whisper** to convert audio/video to text.
- **Page-wise Summarization** – Option to summarize entire documents or page-by-page.
- **User-Friendly GUI** – Built using **Tkinter** with intuitive navigation.
- **Multi-threaded Processing** – Faster summarization via **parallel threading**.
- **Reset & Export** – Easily clear the workspace and export summaries.

---

## 🖥 System Requirements

- **OS**: Windows 10+, Ubuntu 20.04+, macOS Monterey+
- **RAM**: Minimum 8 GB (16 GB recommended)
- **Disk Space**: Minimum 10 GB free
- **Python**: Version 3.8 or above
- **GPU**: Optional (for faster processing with T5 model)

---

## 🛠 Installation Guide

### 1️⃣ Install Python

```sh
python --version
```

If not installed: [Download Python](https://www.python.org/downloads/)

### 2️⃣ Install Dependencies

```sh
pip install torch transformers openai-whisper nltk pillow pypdf2 python-docx tk
python -c "import nltk; nltk.download('punkt')"
```

### 3️⃣ Install FFmpeg (Required for Audio/Video Support)

**Windows**:  
Download & extract [FFmpeg](https://ffmpeg.org/download.html).  
Add `C:\ffmpeg\bin` to **System PATH**.

**Linux**:
```sh
sudo apt update && sudo apt install ffmpeg
```

**macOS**:
```sh
brew install ffmpeg
```

Verify installation:
```sh
ffmpeg -version
```

---

## ▶️ Execution Steps

1. Clone the repository or download the project files.
2. Install all required dependencies as per the above steps.
3. Open a terminal in the project directory.
4. Run the application:

```sh
python main.py
```

5. The GUI will open. Choose the input mode (Text, Document, Audio/Video), and click Summarize!

---

## 📌 Supported Formats

| Format                | Supported |
|-----------------------|-----------|
| Plain Text            | ✅ |
| PDF Documents         | ✅ |
| Word Files (DOCX)     | ✅ |
| Audio (MP3, WAV, FLAC) | ✅ |
| Video (MP4, MKV, AVI)  | ✅ |

---

## 🧠 Models & Tech Stack

- **Summarizer**: T5-large (Abstractive summarization)
- **Transcriber**: OpenAI Whisper
- **GUI**: Tkinter
- **Text Preprocessing**: NLTK
- **Parallelization**: Python threading

---

## 🚀 Troubleshooting

**ModuleNotFoundError**  
```sh
pip install -r requirements.txt
```

**FFmpeg Not Found**  
Ensure FFmpeg is installed and added to **PATH**.

**Whisper NoneType Issue**  
```sh
pip uninstall whisper -y && pip install openai-whisper
```

**PDF Reader Error**  
Update `main.py` to use:
```python
from PyPDF2 import PdfReader
```

Or:
```sh
pip install PyPDF2==2.12.1
```

---

## 🏗 Future Enhancements

- Real-time summarization for live streams.
- Multilingual summarization support.
- Enhanced UI/UX (potentially migrate to PyQt or web-based interface).
- Cloud-based processing (AWS/GCP support).

---

## 📜 License

MIT License.

---

## 👨‍💻 Authors

- **Anukul N. Pande**
- **Ram G. Rathod**
- **Dev G. Chukambe**
- **Rushikesh S. Mahulkar**

(Under the guidance of **Prof. S. G. Taley**, PRMIT&R, Badnera)

---

## ⭐ Support

If you find this project helpful, please ⭐ star the repository!
