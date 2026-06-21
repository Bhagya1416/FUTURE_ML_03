skills_db = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "power bi",
    "tableau",
    "excel",
    "aws",
    "java",
    "c++"
]

def extract_skills(text):

    text = text.lower()

    extracted = []

    for skill in skills_db:

        if skill.lower() in text:

            extracted.append(skill)

    return list(set(extracted))