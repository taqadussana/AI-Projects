# Resume Screening AI Pro

An AI-powered Applicant Tracking System (ATS) built with Python and Streamlit that helps recruiters evaluate resumes against a job description. The application automatically ranks candidates, analyzes skill gaps, generates ATS match scores, and exports detailed reports for faster hiring decisions.

## Live Demo

https://resume-screening-ai-pro.streamlit.app

---

## Overview

Resume Screening AI Pro streamlines the initial recruitment process by comparing multiple resumes against a job description using Natural Language Processing (NLP) techniques.

The system evaluates resume relevance, identifies matching and missing skills, ranks applicants based on compatibility, and presents the results through an interactive analytics dashboard.

---

## Key Features

- Compare multiple resumes with a single job description
- ATS-based resume scoring
- Resume ranking using TF-IDF and Cosine Similarity
- Skill matching and missing skill detection
- Interactive charts and recruiter dashboard
- Candidate filtering and ranking
- Resume preview
- Professional PDF report generation
- CSV export for further analysis
- Modern responsive Streamlit interface

---

## Technology Stack

### Backend

- Python
- Scikit-learn
- Pandas
- PDFPlumber
- python-docx
- FPDF2

### Frontend

- Streamlit
- Plotly

### NLP Techniques

- TF-IDF Vectorization
- Cosine Similarity
- Keyword Extraction
- Text Preprocessing

---

## Project Structure

```text
Resume-Screening-AI/
│
├── app.py
├── parser.py
├── scorer.py
├── skills.py
├── dashboard.py
├── charts.py
├── recommendation.py
├── suggestions.py
├── pdf_report.py
├── requirements.txt
├── assets/
│   ├── style.css
│   └── uploads/
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/taqadussana/AI-Projects.git
```

### Navigate to the project

```bash
cd AI-Projects/Resume-Screening-AI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Launch the application

```bash
streamlit run app.py
```

---

## How It Works

1. Upload a Job Description (PDF)
2. Upload one or more resumes
3. Click **Analyze Resumes**
4. Review ATS scores and rankings
5. Explore candidate skill analysis
6. Download CSV or PDF reports

---

## Screenshots

Add screenshots of:

- Dashboard
- Candidate Rankings
- Skill Analysis
- ATS Score
- PDF Report

---

## Future Enhancements

- AI-powered resume feedback using LLMs
- Automatic resume summarization
- Experience and education extraction
- Recruiter authentication
- Candidate database integration
- Resume keyword highlighting
- JD generation using AI
- Multi-language resume support
- Docker deployment
- REST API integration

---

## Author

**Taqadus Sana**

- GitHub: [@taqadussana](https://github.com/taqadussana)
- LinkedIn: [Taqadus sana](https://linkedin.com/in/taqadus-sana)

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- Streamlit
- Scikit-learn
- Plotly
- PDFPlumber
- Python Open Source Community
