from resume_parser import extract_text
from text_preprocessing import clean_text

resume_text = extract_text(
    "resumes/resume1.pdf"
)

cleaned_text = clean_text(
    resume_text
)

print(cleaned_text)