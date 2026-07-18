import re
import nltk

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stop_words = set(stopwords.words("english"))


def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z ]", " ", text)

    words = [
        word for word in text.split()
        if word not in stop_words
    ]

    return " ".join(words)


def score_resume(resume, job):
    resume = clean(resume)
    job = clean(job)

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform([resume, job])

    score = cosine_similarity(matrix[0], matrix[1])

    return round(score[0][0] * 100, 2)