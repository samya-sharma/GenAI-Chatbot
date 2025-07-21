# 📄 backend/main.py

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pdfplumber
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pdf_context = ""


@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global pdf_context
    contents = await file.read()
    with open("temp.pdf", "wb") as f:
        f.write(contents)

    text = ""
    with pdfplumber.open("temp.pdf") as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    pdf_context = text[:3000]  # truncate to first 3000 chars
    return {"message": "PDF uploaded and processed successfully."}


@app.post("/chat")
async def chat(prompt: str = Form(...)):
    global pdf_context
    if not pdf_context:
        raise HTTPException(status_code=400, detail="No PDF uploaded yet.")

    try:
        messages = [
            {"role": "system", "content": "You are a helpful assistant. Use the PDF content to answer the user's question."},
            {"role": "user", "content": f"PDF Content:\n{pdf_context}\n\nUser Question:\n{prompt}"}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        answer = response.choices[0].message.content
        return {"response": answer}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/reset")
def reset_context():
    global pdf_context
    pdf_context = ""
    return {"message": "Context reset."}
