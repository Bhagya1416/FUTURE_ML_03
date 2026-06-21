def identify_skill_gap(
        jd_skills,
        resume_skills):

    missing_skills = list(
        set(jd_skills)
        -
        set(resume_skills)
    )

    return missing_skills