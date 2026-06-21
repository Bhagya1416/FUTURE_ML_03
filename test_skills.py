from resume_parser import extract_text
from text_preprocessing import clean_text
from skill_extractor import extract_skills

resume_text = extract_text(
    "resumes/resume1.pdf"
)

cleaned_text = clean_text(
    resume_text
)

skills = extract_skills(
    cleaned_text
)

print("Skills Found:")
print(skills)
