import re

# Master Skills Database
SKILLS_DB = {
    # Programming
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "php", "ruby", "go", "rust", "swift", "kotlin", "r", "matlab",

    # Web
    "html", "css", "react", "angular", "vue", "node.js",
    "express", "django", "flask", "fastapi", "bootstrap",

    # Databases
    "mysql", "postgresql", "mongodb", "sqlite", "oracle",
    "sql", "redis", "firebase",

    # Data Science
    "numpy", "pandas", "matplotlib", "seaborn",
    "scikit-learn", "tensorflow", "keras",
    "pytorch", "opencv", "xgboost",

    # AI / NLP
    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "computer vision",
    "generative ai",
    "llm",
    "langchain",

    # Cloud
    "aws", "azure", "gcp",
    "docker", "kubernetes",
    "terraform",

    # DevOps
    "git", "github", "linux",
    "jenkins", "ci/cd",

    # BI
    "power bi", "tableau", "excel",

    # Soft Skills
    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "critical thinking"
}


def extract_skills(text):
    """
    Extract skills from resume or job description.
    """

    text = text.lower()

    found = []

    for skill in SKILLS_DB:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.append(skill)

    return sorted(list(set(found)))


def compare_skills(resume_text, job_text):

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))

    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)

    if len(job_skills) == 0:
        score = 0
    else:
        score = round(len(matched) / len(job_skills) * 100, 2)

    return {
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matched": matched,
        "missing": missing,
        "skill_score": score
    }