setup instructions for local development and deployment (e.g., Render):
````markdown
# 🤖 GenAI Chatbot Web App with PDF Upload

This is a full-stack web application that allows users to **upload a PDF**, then **chat with an AI** (OpenAI GPT-3.5 Turbo) based on the content extracted from the PDF.

---

## 📂 Tech Stack

- ⚙️ **Backend**: FastAPI + pdfplumber + OpenAI API
- 💻 **Frontend**: React.js + Axios
- ☁️ **Deployment Ready**: Render (optional)

---

## 🚀 Features

- Upload a PDF and extract its text
- Ask questions about the PDF content
- Get responses from OpenAI's ChatGPT
- Reset chat anytime

---

## 🧑‍💻 Local Development Setup

### 🔧 Prerequisites

- Python 3.8+
- Node.js and npm
- OpenAI API Key

---

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/your-username/genai-chatbot.git
cd genai-chatbot
````

---

### 2️⃣ Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

> Create a `.env` file in the `backend/` directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

> Then run the backend:

```bash
uvicorn main:app --reload --port 8000
```

---

### 3️⃣ Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

> React app will start at [http://localhost:3000](http://localhost:3000)

---

## 🌐 Deployment (Render.com)

> Optional: Deploy backend + frontend automatically using `render.yaml`

### 📄 render.yaml

Place this `render.yaml` in your root folder:

```yaml
services:
  - type: web
    name: genai-chatbot-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port 8000
    envVars:
      - key: OPENAI_API_KEY
        sync: false
    buildFilter:
      paths:
        - backend/**

  - type: web
    name: genai-chatbot-frontend
    env: static
    buildCommand: npm install && npm run build
    staticPublishPath: frontend/build
    buildFilter:
      paths:
        - frontend/**
```

### 🛠 Steps:

1. Push to GitHub
2. Go to [Render](https://render.com)
3. Click **"New Web Service"**
4. Connect your repo and deploy

---

## 📝 Project Structure

```
genai-chatbot/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/App.jsx
│   ├── package.json
│   └── build/ (auto-generated)
│
├── render.yaml
└── README.md
```

---

## 📦 Requirements

### backend/requirements.txt

```
fastapi
uvicorn
openai
python-multipart
pdfplumber
python-dotenv
```

> You can generate it with:

```bash
pip freeze > requirements.txt
```

---

## 🙋‍♀️ Author

**Samya Sharma**
Feel free to reach out for suggestions, ideas, or improvements.

---

## 📜 License

This project is licensed under the MIT License.


