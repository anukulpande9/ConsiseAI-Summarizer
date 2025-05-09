import os
import ctypes
import subprocess
import whisper
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, StringVar, OptionMenu, Button, Label, Tk, GROOVE
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import summarizer as sm
import docx
import PyPDF2


# Load Whisper model (use "base" or "small" for faster processing)
whisper_model = whisper.load_model("base")


def func1():
    page1 = Tk()
    page1.title("Consise AI - Summarizer")

    img = Image.open("images/page3.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(page1, image=img)
    panel.pack(side="top", fill="both", expand="yes")

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    a, b = str(w // 2 - 620), str(h // 2 - 450)
    page1.geometry(f"1200x720+{a}+{b}")
    page1.resizable(0, 0)

    def dest():
        page1.destroy()
        home()

    photo1 = Image.open("images/6.png")
    img2 = ImageTk.PhotoImage(photo1)
    b1 = Button(page1, highlightthickness=0, bd=0, activebackground="#ffffff", image=img2, command=dest)
    b1.place(x=32, y=18)

    photo2 = Image.open("images/7.png")
    img3 = ImageTk.PhotoImage(photo2)

    def summarize_text():
        """Fetches text, summarizes it, and displays output"""
        input_text = lblText.get("1.0", "end-1c").strip()

        if not input_text or input_text == placeholder:
            messagebox.showerror("Error", "Please enter text to summarize.")
            return

        try:
            success, summarized_text = sm.summarize_text_parallel(input_text)
            if success:
                lblText2.delete("1.0", "end")  # Clear previous summary
                lblText2.insert("1.0", summarized_text)  # Insert new summary
            else:
                raise Exception(summarized_text)
        except Exception as e:
            messagebox.showerror("Summarization Error", str(e))

    b2 = Button(page1, highlightthickness=0, bd=0, activebackground="#ffffff", image=img3, command=summarize_text)
    b2.place(x=314, y=623)

    # Add reset button
    photo_reset = Image.open("images/reset.png")
    img_reset = ImageTk.PhotoImage(photo_reset)
    
    def reset_text():
        lblText.delete("1.0", "end")
        lblText2.delete("1.0", "end")
        lblText.insert("1.0", placeholder)
        lblText2.insert("1.0", placeholder2)
        lblText.config(fg='#b0b0b0')
        lblText2.config(fg='#b0b0b0')
    
    # Position reset button next to submit button with spacing
    submit_button_width = 570
    spacing = 20
    reset_x = 314 + submit_button_width + spacing
    reset_y = 633  # Submit y + 10
    
    b_reset = Button(page1, highlightthickness=0, bd=0, activebackground="#ffffff", image=img_reset, command=reset_text)
    b_reset.place(x=reset_x, y=reset_y)
    
    placeholder = "You may write or paste your text here..."

    def on_focus_in(event):
        if lblText.get("1.0", "end-1c") == placeholder:
            lblText.delete("1.0", "end")
            lblText.config(fg='#ffffff')

    def on_focus_out(event):
        if lblText.get("1.0", "end-1c").strip() == "":
            lblText.insert("1.0", placeholder)
            lblText.config(fg='#b0b0b0')

    lblText = scrolledtext.ScrolledText(
        page1, bg='#262276', fg='#b0b0b0', insertbackground='white', relief=GROOVE,
        height=11, width=46, font='Arial', bd=0
    )
    lblText.place(x=62, y=300)
    lblText.insert("1.0", placeholder)
    lblText.bind("<FocusIn>", on_focus_in)
    lblText.bind("<FocusOut>", on_focus_out)

    placeholder2 = "Summarized text will appear here..."

    def on_focus_in2(event):
        if lblText2.get("1.0", "end-1c") == placeholder2:
            lblText2.delete("1.0", "end")
            lblText2.config(fg='#ffffff')

    def on_focus_out2(event):
        if lblText2.get("1.0", "end-1c").strip() == "":
            lblText2.insert("1.0", placeholder2)
            lblText2.config(fg='#b0b0b0')

    lblText2 = scrolledtext.ScrolledText(
        page1, bg='#6461f6', fg='#b0b0b0', insertbackground='black', relief=GROOVE,
        height=11, width=48, font='Arial', bd=0
    )
    lblText2.place(x=634, y=300)
    lblText2.insert("1.0", placeholder2)
    lblText2.bind("<FocusIn>", on_focus_in2)
    lblText2.bind("<FocusOut>", on_focus_out2)

    page1.mainloop()
    

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file with visible page separation."""
    text_by_page = []
    try:
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(pdf_reader.pages):
                text = page.extract_text() or ""
                text_by_page.append(f"Page break\n" + "-" * 30 + "\n" + text)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text from PDF:\n{str(e)}")
        return None
    return text_by_page

def extract_text_from_docx(docx_path):
    """Extracts text from a Word document with visible page separation."""
    text_by_page = []
    try:
        doc = docx.Document(docx_path)
        all_text = [para.text for para in doc.paragraphs]
        approx_pages = "\n".join(all_text).split("\n\n")  # Approximating pages using double line breaks

        for i, page in enumerate(approx_pages):
            text_by_page.append(f"Page break\n" + "-" * 30 + "\n" + page)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text from Word file:\n{str(e)}")
        return None
    return text_by_page

def func2():
    page2 = Tk()
    page2.title("Concise AI - Summarizer")

    img = Image.open("images/page1.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(page2, image=img)
    panel.pack(side="top", fill="both", expand="yes")

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    w, h = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    page2.geometry(f"1200x720+{w//2-620}+{h//2-450}")
    page2.resizable(0, 0)

    def dest():
        page2.destroy()
        home()

    # Back button
    img2 = ImageTk.PhotoImage(Image.open("images/6.png"))
    b1 = Button(page2, highlightthickness=0, bd=0, activebackground="#ffffff", image=img2, command=dest)
    b1.place(x=32, y=18)

    # Summarize button
    img3 = ImageTk.PhotoImage(Image.open("images/7.png"))
    
    def summarize_text():
        """Summarizes extracted text based on the selected option."""
        input_text = lblText.get("1.0", "end-1c").strip().replace('Page break','')

        if not input_text or input_text == placeholder:
            messagebox.showerror("Error", "No extracted text found. Please select a file first.")
            return

        try:
            if selected_option.get() == "Page Wise":
                pages = input_text.split("\n" + "-" * 30 + "\n") # Splitting by page separator
                summarized_text = "\n\n".join([f"Page break\n" + "-" * 30 + "\n" + sm.summarize_text_parallel(page)[1] for i, page in enumerate(pages) if page.strip()])
            else:
                summarized_text = sm.summarize_text_parallel(input_text)[1]

            lblText2.delete("1.0", "end")
            lblText2.insert("1.0", summarized_text)
        except Exception as e:
            messagebox.showerror("Summarization Error", str(e))

    b2 = Button(page2, highlightthickness=0, bd=0, activebackground="#ffffff", image=img3, command=summarize_text)
    b2.place(x=314, y=623)

    # File select button
    img4 = ImageTk.PhotoImage(Image.open("images/8.png"))

    def load_file():
        """Opens a file dialog, extracts text from PDF or Word, and displays it."""
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx")])
        if not file_path:
            return

        file_extension = file_path.split(".")[-1].lower()
        extracted_text = None

        if file_extension == "pdf":
            extracted_text = extract_text_from_pdf(file_path)
        elif file_extension == "docx":
            extracted_text = extract_text_from_docx(file_path)
        else:
            messagebox.showerror("Error", "Unsupported file format. Please select a PDF or DOCX file.")
            return

        if extracted_text:
            lblText.delete("1.0", "end")
            lblText.insert("1.0", "\n\n".join(extracted_text))  # Display text with page separators

    b4 = Button(page2, highlightthickness=0, bd=0, activebackground="#ffffff", image=img4, command=load_file)
    b4.place(x=314, y=174)

    # Dropdown for summary options
    summary_options = ["Complete Doc", "Page Wise"]
    selected_option = StringVar(value=summary_options[0])

    dropdown = OptionMenu(page2, selected_option, *summary_options)
    dropdown.config(font=('Arial', 12), bg='#8784d8', activebackground="#8784d8", fg='white', width=11, bd=0, highlightthickness=0)
    dropdown.place(x=592, y=262)

    placeholder = "Extracted Text from the file will appear here..."

    def on_focus_in(event):
        if lblText.get("1.0", "end-1c") == placeholder:
            lblText.delete("1.0", "end")
            lblText.config(fg='#ffffff')

    def on_focus_out(event):
        if lblText.get("1.0", "end-1c").strip() == "":
            lblText.insert("1.0", placeholder)
            lblText.config(fg='#b0b0b0')

    lblText = scrolledtext.ScrolledText(page2, bg='#262276', fg='#b0b0b0', insertbackground='white', relief=GROOVE, height=11, width=46, font='Arial', bd=0)
    lblText.place(x=62, y=300)
    lblText.insert("1.0", placeholder)
    lblText.bind("<FocusIn>", on_focus_in)
    lblText.bind("<FocusOut>", on_focus_out)

    placeholder2 = "Summarized text will appear here..."

    def on_focus_in2(event):
        if lblText2.get("1.0", "end-1c") == placeholder2:
            lblText2.delete("1.0", "end")
            lblText2.config(fg='#ffffff')

    def on_focus_out2(event):
        if lblText2.get("1.0", "end-1c").strip() == "":
            lblText2.insert("1.0", placeholder2)
            lblText2.config(fg='#b0b0b0')

    lblText2 = scrolledtext.ScrolledText(page2, bg='#6461f6', fg='#b0b0b0', insertbackground='black', relief=GROOVE, height=11, width=48, font='Arial', bd=0)
    lblText2.place(x=634, y=300)
    lblText2.insert("1.0", placeholder2)
    lblText2.bind("<FocusIn>", on_focus_in2)
    lblText2.bind("<FocusOut>", on_focus_out2)

    # Add reset button
    photo_reset = Image.open("images/reset.png")
    img_reset = ImageTk.PhotoImage(photo_reset)
    
    def reset_text():
        lblText.delete("1.0", "end")
        lblText2.delete("1.0", "end")
        lblText.insert("1.0", placeholder)
        lblText2.insert("1.0", placeholder2)
        lblText.config(fg='#b0b0b0')
        lblText2.config(fg='#b0b0b0')
    
    # Position reset button next to submit button with spacing
    submit_button_width = 570
    spacing = 20
    reset_x = 314 + submit_button_width + spacing
    reset_y = 633  # Submit y + 10
    
    b_reset = Button(page2, highlightthickness=0, bd=0, activebackground="#ffffff", image=img_reset, command=reset_text)
    b_reset.place(x=reset_x, y=reset_y)
    
    page2.mainloop()


def extract_text_from_audio(video_path):
    """Extracts text from audio/video using OpenAI Whisper."""
    try:
        # Convert video to audio if needed
        if video_path.lower().endswith((".mp4", ".mkv", ".avi", ".mov")):
            audio_path = "temp_audio.wav"
            command = f'ffmpeg -i "{video_path}" -ar 16000 -ac 1 -c:a pcm_s16le "{audio_path}" -y'
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            audio_path = video_path  # It's already an audio file

        # Transcribe using Whisper
        result = whisper_model.transcribe(audio_path)

        # Remove temp audio file if converted
        if audio_path == "temp_audio.wav" and os.path.exists(audio_path):
            os.remove(audio_path)

        return result["text"]

    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text:\n{str(e)}")
        return None

def func3():
    page3 = Tk()
    page3.title("Concise AI - Summarizer")

    img = Image.open("images/page2.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(page3, image=img)
    panel.pack(side="top", fill="both", expand="yes")

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    w, h = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    page3.geometry(f"1200x720+{w//2-620}+{h//2-450}")
    page3.resizable(0, 0)

    def dest():
        page3.destroy()
        home()

    img2 = ImageTk.PhotoImage(Image.open("images/6.png"))
    b1 = Button(page3, highlightthickness=0, bd=0, activebackground="#ffffff", image=img2, command=dest)
    b1.place(x=32, y=18)

    img3 = ImageTk.PhotoImage(Image.open("images/7.png"))
    
    def summarize_text():
        """Summarizes transcribed text from the left text box."""
        input_text = lblText.get("1.0", "end-1c").strip()

        if not input_text or input_text == placeholder:
            messagebox.showerror("Error", "No transcribed text found. Please upload a file first.")
            return

        try:
            summarized_text = sm.summarize_text_parallel(input_text)[1]

            lblText2.delete("1.0", "end")
            lblText2.insert("1.0", summarized_text)
        except Exception as e:
            messagebox.showerror("Summarization Error", str(e))

    b2 = Button(page3, highlightthickness=0, bd=0, activebackground="#ffffff", image=img3, command=summarize_text)
    b2.place(x=314, y=623)

    img4 = ImageTk.PhotoImage(Image.open("images/9.png"))

    def load_audio_video():
        """Opens file dialog, extracts text from video/audio, and displays it."""
        file_path = filedialog.askopenfilename(filetypes=[
            ("Audio Files", "*.mp3 *.wav *.m4a *.flac"),
            ("Video Files", "*.mp4 *.mkv *.avi *.mov"),
        ])
        if not file_path:
            return

        extracted_text = extract_text_from_audio(file_path)

        if extracted_text:
            lblText.delete("1.0", "end")
            lblText.insert("1.0", extracted_text)

    b4 = Button(page3, highlightthickness=0, bd=0, activebackground="#ffffff", image=img4, command=load_audio_video)
    b4.place(x=315, y=163)

    placeholder = "Extracted text from the audio/video file will appear here..."

    def on_focus_in(event):
        if lblText.get("1.0", "end-1c") == placeholder:
            lblText.delete("1.0", "end")
            lblText.config(fg='#ffffff')

    def on_focus_out(event):
        if lblText.get("1.0", "end-1c").strip() == "":
            lblText.insert("1.0", placeholder)
            lblText.config(fg='#b0b0b0')

    lblText = scrolledtext.ScrolledText(
        page3, bg='#262276', fg='#b0b0b0', insertbackground='white',
        relief=GROOVE, height=11, width=46, font='Arial', bd=0
    )
    lblText.place(x=62, y=300)
    lblText.insert("1.0", placeholder)
    lblText.bind("<FocusIn>", on_focus_in)
    lblText.bind("<FocusOut>", on_focus_out)

    placeholder2 = "Summarized text will appear here..."

    def on_focus_in2(event):
        if lblText2.get("1.0", "end-1c") == placeholder2:
            lblText2.delete("1.0", "end")
            lblText2.config(fg='#ffffff')

    def on_focus_out2(event):
        if lblText2.get("1.0", "end-1c").strip() == "":
            lblText2.insert("1.0", placeholder2)
            lblText2.config(fg='#b0b0b0')

    lblText2 = scrolledtext.ScrolledText(
        page3, bg='#6461f6', fg='#b0b0b0', insertbackground='black',
        relief=GROOVE, height=11, width=48, font='Arial', bd=0
    )
    lblText2.place(x=634, y=300)
    lblText2.insert("1.0", placeholder2)
    lblText2.bind("<FocusIn>", on_focus_in2)
    lblText2.bind("<FocusOut>", on_focus_out2)

    # Add reset button
    photo_reset = Image.open("images/reset.png")
    img_reset = ImageTk.PhotoImage(photo_reset)
    
    def reset_text():
        lblText.delete("1.0", "end")
        lblText2.delete("1.0", "end")
        lblText.insert("1.0", placeholder)
        lblText2.insert("1.0", placeholder2)
        lblText.config(fg='#b0b0b0')
        lblText2.config(fg='#b0b0b0')
    
    # Position reset button next to submit button with spacing
    submit_button_width = 570
    spacing = 20
    reset_x = 314 + submit_button_width + spacing
    reset_y = 633  # Submit y + 10
    
    b_reset = Button(page3, highlightthickness=0, bd=0, activebackground="#ffffff", image=img_reset, command=reset_text)
    b_reset.place(x=reset_x, y=reset_y)

    page3.mainloop()

def func4():
    page2 = Tk()
    page2.title("Concise AI - Summarizer")

    img = Image.open("images/about.jpeg")
    img = ImageTk.PhotoImage(img)
    panel = Label(page2, image=img)
    panel.pack(side="top", fill="both", expand="yes")

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    w, h = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    page2.geometry(f"1200x720+{w//2-620}+{h//2-450}")
    page2.resizable(0, 0)

    def dest():
        page2.destroy()
        home()

    # Back button
    img2 = ImageTk.PhotoImage(Image.open("images/6.png"))
    b1 = Button(page2, highlightthickness=0, bd=0, activebackground="#ffffff", image=img2, command=dest)
    b1.place(x=32, y=18)
    page2.mainloop()

def home():
    home = Tk()
    home.title("Consise AI - Summarizer")

    img = Image.open("images/home.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(home, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-620)
    b= str(lt[1]//2-450)
    home.geometry("1200x720+"+a+"+"+b)
    home.resizable(0,0)

    def df1():
        home.destroy()
        func1()


    def df2():
        home.destroy()
        func2()
        
    def df3():
        home.destroy()
        func3()

    def df4():
        home.destroy()
        func4()


    def Exit():
        
        result = messagebox.askquestion(
            "Consise AI - Summarizer", 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            home.destroy()
            exit()
        else:
            messagebox.showinfo(
                'Return', 'You will now return to the main screen')
        
    photo = Image.open("images/1.png")
    img2 = ImageTk.PhotoImage(photo)
    b1=Button(home, highlightthickness = 0, bd = 0,activebackground="#ffffff", image = img2,command=df1)
    b1.place(x=71,y=221)

    photo = Image.open("images/2.png")
    img3 = ImageTk.PhotoImage(photo)
    b2=Button(home, highlightthickness = 0, bd = 0,activebackground="#ffffff", image = img3,command=df2)
    b2.place(x=71,y=330)

    photo = Image.open("images/3.png")
    img4 = ImageTk.PhotoImage(photo)
    b3=Button(home, highlightthickness = 0, bd = 0,activebackground="#ffffff", image = img4,command=df3)
    b3.place(x=80,y=436)

    photo = Image.open("images/4.png")
    img5 = ImageTk.PhotoImage(photo)
    b5=Button(home, highlightthickness = 0, bd = 0,activebackground="#ffffff", image = img5,command=df4)
    b5.place(x=80,y=547)
    
    photo = Image.open("images/5.png")
    img6 = ImageTk.PhotoImage(photo)
    b6=Button(home, highlightthickness = 0, bd = 0,activebackground="#ffffff", image = img6,command=Exit)
    b6.place(x=394,y=547)
    
    home.mainloop()

home()



