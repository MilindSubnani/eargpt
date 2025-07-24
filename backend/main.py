
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from transcribe import transcribe_audio
from summarize import summarize_text
from phrase_detector import extract_highlights

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/transcribe")
async def transcribe(file: UploadFile = File(...)):
    contents = await file.read()
    with open("temp.wav", "wb") as f:
        f.write(contents)

    text = transcribe_audio("temp.wav")
    summary = summarize_text(text)
    highlights = extract_highlights(text)

    return {"transcript": text, "summary": summary, "highlights": highlights}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
