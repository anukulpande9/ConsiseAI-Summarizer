# 🌟 ConsiseAI – AI-Based Document Summarization Tool

🚀 **ConsiseAI** is an advanced AI-powered tool for summarizing **text, PDFs, Word documents, and even audio/video transcriptions!**  
It uses **Facebook's BART Transformer** for intelligent summarization and **OpenAI Whisper** for speech-to-text conversion.

---

## 🔹 Features
- **AI-Powered Summarization** – Uses **BART Transformer** for high-quality summaries.
- **Supports Multiple Formats** – Works with **Text, PDF, DOCX, MP3, MP4, WAV** files.
- **Speech-to-Text Integration** – Converts **audio/video files to text** before summarization.
- **User-Friendly GUI** – Simple and interactive **Tkinter-based interface**.
- **Multi-threaded Processing** – Faster summarization using **parallel computation**.

---

## 🛠 Installation Guide

### 1️⃣ Install Python  
Check if Python is installed:
```sh
python --version
```
If not installed, [Download Python](https://www.python.org/downloads/) and install it.

### 2️⃣ Install Dependencies  
Run the following command in the project folder:
```sh
pip install torch transformers openai-whisper nltk pillow pypdf2 python-docx tk
```

### 3️⃣ Install FFmpeg (For Audio/Video Support)

#### Windows:
1. Download **FFmpeg** from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract it to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to **System PATH**:
   - Press **Win + R**, type `sysdm.cpl`, and press Enter.
   - Go to **Advanced** → **Environment Variables**.
   - Find the `Path` variable and click **Edit**.
   - Click **New** and add `C:\ffmpeg\bin`.
   - Click **OK**, then restart your computer.

#### Linux (Ubuntu/Debian):
```sh
sudo apt update && sudo apt install ffmpeg
```

#### Mac (Homebrew):
```sh
brew install ffmpeg
```

Verify installation:
```sh
ffmpeg -version
```

### 4️⃣ Run the Application  
```sh
python main.py
```

---

## 🎯 How It Works
1. **Enter text manually** or **upload a document/audio/video**.
2. Click **Summarize** – AI processes the content and provides a concise summary.
3. Copy/download the summarized text.

---

## 📌 Supported Formats

| Format                | Supported |
|-----------------------|-----------|
| Plain Text            | ✅        |
| PDF Documents         | ✅        |
| Word Files (DOCX)     | ✅        |
| Audio (MP3, WAV, FLAC) | ✅        |
| Video (MP4, MKV, AVI)  | ✅        |

---

## 🚀 Troubleshooting

- **ModuleNotFoundError**  
  Install missing dependencies using:
  ```sh
  pip install -r requirements.txt
  ```

- **Whisper Error (`NoneType` issue)**  
  Reinstall Whisper:
  ```sh
  pip uninstall whisper -y && pip install openai-whisper
  ```

- **FFmpeg Not Found**  
  Ensure FFmpeg is installed and added to **System PATH**.

- **PDF Extraction Error (`PdfFileReader is deprecated`)**  
  Modify `main.py`:
  ```python
  from PyPDF2 import PdfReader
  pdf_reader = PdfReader(file)
  ```
  Or downgrade PyPDF2:
  ```sh
  pip install PyPDF2==2.12.1
  ```

---

## 💡 Future Improvements
- Cloud-based summarization (AWS/GCP)
- Support for multiple AI models (PEGASUS, GPT-4, etc.)
- Better UI/UX with modern frameworks

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 👨‍💻 Author
Developed by **Anukul Pande** as a **Final Year Project**.

---

## 🌟 Support
If you like this project, please ⭐ **star** the repo on GitHub! 😊
