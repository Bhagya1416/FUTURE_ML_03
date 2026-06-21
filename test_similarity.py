from resume_parser import extract_text
from text_preprocessing import clean_text
from ranking import calculate_similarity

resume_text = extract_text(
    "resumes/resume1.pdf"
)

with open(
    "job_description.txt",
    "r",
    encoding="utf-8"
) as file:

    jd_text = file.read()

score = calculate_similarity(
    clean_text(jd_text),
    clean_text(resume_text)
)

print(
    f"Similarity Score: {score}%"
)