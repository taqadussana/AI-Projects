# Resume Screening AI Pro

An AI-powered Resume Screening and ATS Matching System built with Python and Streamlit. The application helps recruiters compare multiple resumes against a job description, rank candidates, identify missing skills, and export professional reports.

---

## Features

- Upload one job description (PDF)
- Upload multiple resumes (PDF)
- Resume ranking based on job match
- ATS match score
- Skill match analysis
- Missing skills detection
- Interactive dashboard and charts
- Candidate rankings
- Export results as CSV
- Export professional PDF reports

---

## Technology Stack

- Python
- Streamlit
- Pandas
- Plotly
- PDFPlumber
- python-docx
- FPDF

---

## Project Structure

```
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
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/taqadussana/AI-Projects.git
```

Go to the project folder

```bash
cd AI-Projects/Resume-Screening-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Usage

1. Launch the application.
2. Upload a job description in PDF format.
3. Upload one or more resumes.
4. Click **Analyze Resumes**.
5. Review candidate rankings, match scores, and skill analysis.
6. Export the results as CSV or PDF.

---

## Future Improvements

- AI-powered resume feedback
- NLP-based resume parsing
- User authentication
- Candidate database
- Job description generator
- Cloud deployment
- Recruiter analytics dashboard

---

## Author

**Taqadus Sana**

GitHub: https://github.com/taqadussana

---

## License

This project is available under the MIT License.
