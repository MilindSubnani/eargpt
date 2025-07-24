# EarGPT 🎧🤖  
**Your AI-powered meeting assistant that listens while you talk and instantly summarizes your conversations into clear bullet points.**

---

## 🔍 What is EarGPT?

EarGPT is an AI-driven meeting summarizer that:
- Records or uploads audio
- Transcribes the audio using OpenAI’s Whisper
- Summarizes the transcript using GPT-3.5 in bullet point format

Perfect for students, professionals, and teams who want to capture key takeaways from meetings, lectures, or interviews — hands-free.

---

## ⚙️ Tech Stack

- **Frontend**: React (Vite) + TailwindCSS  
- **Backend**: FastAPI (Python)  
- **AI Tools**:
  - 🧠 Whisper (for speech-to-text)
  - 💬 GPT-3.5 (for summarization)

---

## 🚀 Features

- 🎙️ Upload meeting audio
- ✍️ Real-time transcription
- 📌 Instant AI-generated summaries
- 🌐 Full-stack web application

---

## 🛠️ Installation & Run Locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
uvicorn main:app --reload
