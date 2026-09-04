# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes a resume against a given job description and generates a resume-job match score using Natural Language Processing (NLP).

## ✨ Features

* 📄 Upload a resume in PDF format
* 💼 Enter a job description
* 🔍 Extract text from the resume automatically
* 🧠 Generate semantic embeddings using Sentence Transformers
* 📊 Calculate an AI-based resume match score
* ⚡ React-based user interface
* 🔗 Flask REST API backend

## 🛠️ Technologies Used

**Frontend**

* React
* Vite
* JavaScript
* CSS

**Backend**

* Python
* Flask
* Flask-CORS

**AI / NLP**

* Sentence Transformers
* `all-MiniLM-L6-v2`
* Cosine Similarity

**PDF Processing**

* PyPDF

## 🔄 How It Works

```text
Resume PDF + Job Description
              ↓
        React Frontend
              ↓
         Flask Backend
              ↓
       PDF Text Extraction
              ↓
    Sentence Transformer Model
              ↓
      Semantic Similarity
              ↓
       Match Score (0-100)
```

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .gitignore
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

## 🚀 How to Run

### Backend

Open a terminal in the backend folder:

```bash
cd backend
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Flask:

```bash
python app.py
```

The backend runs at:

```text
http://127.0.0.1:5000
```

### Frontend

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally run at:

```text
http://localhost:5173
```

## 🎯 Project Objective

The objective of this project is to demonstrate how Artificial Intelligence and Natural Language Processing can be used to compare resumes with job descriptions and provide an automated compatibility score.

## 🔮 Future Improvements

* Skill extraction and comparison
* Missing skill detection
* Resume improvement suggestions
* Experience and education analysis
* Detailed visual analytics
* Resume ranking for multiple candidates

## 👩‍💻 Author

**ST Shifana Sanobar**

Computer Science & Data Science
