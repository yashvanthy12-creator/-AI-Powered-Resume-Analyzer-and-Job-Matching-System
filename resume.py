import re
import fitz

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load NLP model
nlp = spacy.load("en_core_web_sm")


# --------------------------------------------------
# 1. Extract text from PDF
# --------------------------------------------------

def extract_resume_text(pdf_path):

    text = ""

    document = fitz.open(r"C:\Users\yashv\Downloads\yash (4) (1).pdf")

    for page in document:
        text += page.get_text()

    document.close()

    return text


# --------------------------------------------------
# 2. Clean text
# --------------------------------------------------

def clean_text(text):

    text = text.lower()

    text = re.sub(r'\s+', ' ', text)

    text = re.sub(r'[^a-zA-Z0-9+#.\s]', '', text)

    return text


# --------------------------------------------------
# 3. Extract skills
# --------------------------------------------------

def extract_skills(text):

    skills_list = [
        "python",
        "java",
        "javascript",
        "react",
        "node.js",
        "html",
        "css",
        "sql",
        "mysql",
        "mongodb",
        "pandas",
        "numpy",
        "scikit-learn",
        "machine learning",
        "deep learning",
        "nlp",
        "tensorflow",
        "pytorch",
        "fastapi",
        "flask",
        "django",
        "git",
        "github",
        "docker",
        "aws",
        "azure",
        "power bi",
        "excel",
        "data analysis",
        "data science"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text:

            found_skills.append(skill)

    return found_skills


# --------------------------------------------------
# 4. Extract education
# --------------------------------------------------

def extract_education(text):

    education_keywords = [
        "b.e",
        "b.tech",
        "be",
        "btech",
        "m.e",
        "m.tech",
        "me",
        "mtech",
        "bca",
        "mca",
        "b.sc",
        "m.sc",
        "bachelor",
        "master",
        "degree"
    ]

    text = text.lower()

    education = []

    for keyword in education_keywords:

        if keyword in text:

            education.append(keyword)

    return list(set(education))


# --------------------------------------------------
# 5. Extract email
# --------------------------------------------------

def extract_email(text):

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    result = re.findall(pattern, text)

    if result:

        return result[0]

    return "Not found"


# --------------------------------------------------
# 6. Resume and Job Description similarity
# --------------------------------------------------

def calculate_similarity(resume_text, job_text):

    documents = [
        resume_text,
        job_text
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


# --------------------------------------------------
# 7. Find missing skills
# --------------------------------------------------

def find_missing_skills(resume_skills, job_skills):

    missing = []

    for skill in job_skills:

        if skill not in resume_skills:

            missing.append(skill)

    return missing


# --------------------------------------------------
# 8. Main program
# --------------------------------------------------

resume_file = "resume.pdf"

job_file = "job_description.txt"


# Extract resume
resume_text = extract_resume_text(resume_file)


# Read job description
with open(job_file, "r", encoding="utf-8") as file:

    job_text = file.read()


# Clean text
clean_resume = clean_text(resume_text)

clean_job = clean_text(job_text)


# Extract information
resume_skills = extract_skills(clean_resume)

job_skills = extract_skills(clean_job)

education = extract_education(clean_resume)

email = extract_email(resume_text)


# Calculate similarity
match_percentage = calculate_similarity(
    clean_resume,
    clean_job
)


# Find missing skills
missing_skills = find_missing_skills(
    resume_skills,
    job_skills
)


# --------------------------------------------------
# Display result
# --------------------------------------------------

print("\n===================================")
print("       AI RESUME ANALYZER")
print("===================================")

print("\nEmail:")
print(email)

print("\nEducation:")
print(education)

print("\nSkills Found:")
for skill in resume_skills:
    print("✓", skill)

print("\nRequired Job Skills:")
for skill in job_skills:
    print("•", skill)

print("\nMissing Skills:")

if missing_skills:

    for skill in missing_skills:
        print("✗", skill)

else:

    print("No major missing skills found")


print("\n===================================")
print("Resume Match:", match_percentage ,"%")
import fitz
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load NLP model
nlp = spacy.load("en_core_web_sm")


# --------------------------------------------------
# 1. Extract text from PDF
# --------------------------------------------------

def extract_resume_text(pdf_path):

    text = ""

    document = fitz.open(r"C:\Users\yashv\Downloads\yash (4) (1).pdf")

    for page in document:
        text += page.get_text()

    document.close()

    return text


# --------------------------------------------------
# 2. Clean text
# --------------------------------------------------

def clean_text(text):

    text = text.lower()

    text = re.sub(r'\s+', ' ', text)

    text = re.sub(r'[^a-zA-Z0-9+#.\s]', '', text)

    return text


# --------------------------------------------------
# 3. Extract skills
# --------------------------------------------------

def extract_skills(text):

    skills_list = [
        "python",
        "java",
        "javascript",
        "react",
        "node.js",
        "html",
        "css",
        "sql",
        "mysql",
        "mongodb",
        "pandas",
        "numpy",
        "scikit-learn",
        "machine learning",
        "deep learning",
        "nlp",
        "tensorflow",
        "pytorch",
        "fastapi",
        "flask",
        "django",
        "git",
        "github",
        "docker",
        "aws",
        "azure",
        "power bi",
        "excel",
        "data analysis",
        "data science"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text:

            found_skills.append(skill)

    return found_skills


# --------------------------------------------------
# 4. Extract education
# --------------------------------------------------

def extract_education(text):

    education_keywords = [
        "b.e",
        "b.tech",
        "be",
        "btech",
        "m.e",
        "m.tech",
        "me",
        "mtech",
        "bca",
        "mca",
        "b.sc",
        "m.sc",
        "bachelor",
        "master",
        "degree"
    ]

    text = text.lower()

    education = []

    for keyword in education_keywords:

        if keyword in text:

            education.append(keyword)

    return list(set(education))


# --------------------------------------------------
# 5. Extract email
# --------------------------------------------------

def extract_email(text):

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    result = re.findall(pattern, text)

    if result:

        return result[0]

    return "Not found"


# --------------------------------------------------
# 6. Resume and Job Description similarity
# --------------------------------------------------

def calculate_similarity(resume_text, job_text):

    documents = [
        resume_text,
        job_text
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


# --------------------------------------------------
# 7. Find missing skills
# --------------------------------------------------

def find_missing_skills(resume_skills, job_skills):

    missing = []

    for skill in job_skills:

        if skill not in resume_skills:

            missing.append(skill)

    return missing


# --------------------------------------------------
# 8. Main program
# --------------------------------------------------

resume_file = r"C:\Users\yashv\Downloads\yash (4) (1).pdf"

job_file = r"C:\Users\yashv\job_description.text"


# Extract resume
resume_text = extract_resume_text(resume_file)


# Read job description
with open(r"C:\Users\yashv\job_description.txt", "r", encoding="utf-8") as file:
    job_text = file.read()


# Clean text
clean_resume = clean_text(resume_text)

clean_job = clean_text(job_text)


# Extract information
resume_skills = extract_skills(clean_resume)

job_skills = extract_skills(clean_job)

education = extract_education(clean_resume)

email = extract_email(resume_text)


# Calculate similarity
match_percentage = calculate_similarity(
    clean_resume,
    clean_job
)


# Find missing skills
missing_skills = find_missing_skills(
    resume_skills,
    job_skills
)


# --------------------------------------------------
# Display result
# --------------------------------------------------

print("\n===================================")
print("       AI RESUME ANALYZER")
print("===================================")

print("\nEmail:")
print(email)

print("\nEducation:")
print(education)

print("\nSkills Found:")
for skill in resume_skills:
    print("✓", skill)

print("\nRequired Job Skills:")
for skill in job_skills:
    print("•", skill)

print("\nMissing Skills:")

if missing_skills:

    for skill in missing_skills:
        print("✗", skill)

else:

    print("No major missing skills found")


print("\n===================================")
print("Resume Match:", match_percentage, "%")
print("===================================")
print("===================================")