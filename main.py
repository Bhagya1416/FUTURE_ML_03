import os
import pandas as pd

from resume_parser import extract_text
from text_preprocessing import clean_text
from skill_extractor import extract_skills
from ranking import (
    calculate_similarity,
    calculate_final_score
)
from skill_gap import identify_skill_gap

# Job Description

with open(
    "job_description.txt",
    "r",
    encoding="utf-8"
) as file:

    jd_text = file.read()

cleaned_jd = clean_text(
    jd_text
)

jd_skills = extract_skills(
    cleaned_jd
)

results = []

for file in os.listdir("resumes"):

    if file.endswith(".pdf"):

        path = os.path.join(
            "resumes",
            file
        )

        resume_text = extract_text(
            path
        )

        cleaned_resume = clean_text(
            resume_text
        )

        resume_skills = extract_skills(
            cleaned_resume
        )

        similarity_score = (
            calculate_similarity(
                cleaned_jd,
                cleaned_resume
            )
        )

        skill_score = (
            len(
                set(resume_skills)
                &
                set(jd_skills)
            )
            /
            len(jd_skills)
        ) * 100

        final_score = (
            calculate_final_score(
                similarity_score,
                skill_score
            )
        )

        missing_skills = (
            identify_skill_gap(
                jd_skills,
                resume_skills
            )
        )

        results.append({

            "Candidate":
                file,

            "Similarity Score":
                similarity_score,

            "Skill Match":
                round(
                    skill_score,
                    2
                ),

            "Final Score":
                final_score,

            "Missing Skills":
                ", ".join(
                    missing_skills
                )
        })

df = pd.DataFrame(
    results
)

df = df.sort_values(
    by="Final Score",
    ascending=False
)

df.insert(
    0,
    "Rank",
    range(
        1,
        len(df)+1
    )
)

print(df)

df.to_csv(
    "outputs/ranked_candidates.csv",
    index=False
)