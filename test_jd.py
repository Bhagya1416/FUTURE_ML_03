from text_preprocessing import clean_text
from skill_extractor import extract_skills

with open("job_description.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

cleaned_jd = clean_text(jd_text)

jd_skills = extract_skills(cleaned_jd)

print("Job Description Skills:")
print(jd_skills)