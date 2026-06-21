# AI-Powered Resume Screening & Candidate Ranking System

## Overview

The AI-Powered Resume Screening & Candidate Ranking System is a Natural Language Processing (NLP) and Machine Learning project designed to automate the initial stages of candidate evaluation. The system analyzes resumes, compares them with a target job description, identifies relevant skills, calculates role-fit scores, ranks candidates, and highlights missing skills.

This project simulates the functionality of modern Applicant Tracking Systems (ATS) and HR-Tech recruitment platforms, helping recruiters reduce manual screening efforts and improve hiring efficiency.

---

## Problem Statement

Organizations often receive hundreds of resumes for a single job opening. Manual screening is time-consuming, inconsistent, and prone to human bias. This project addresses that challenge by building an automated screening system capable of evaluating resumes based on job-specific requirements.

---

## Objectives

* Parse and analyze resume documents.
* Clean and preprocess unstructured text data.
* Extract technical skills using NLP techniques.
* Match resumes against job descriptions.
* Calculate resume relevance scores.
* Rank candidates based on role suitability.
* Identify missing skills and skill gaps.

---

## Features

### Resume Parsing

* Extracts text from PDF resumes.
* Handles multiple candidate resumes automatically.

### Text Preprocessing

* Converts text to lowercase.
* Removes punctuation, special characters, and stopwords.
* Standardizes text for analysis.

### Skill Extraction

* Identifies relevant technical skills from resumes and job descriptions.
* Uses a predefined skill database for matching.

### Job Description Analysis

* Parses job requirements.
* Extracts required skills and keywords.

### Resume-to-Job Matching

* Uses TF-IDF Vectorization for feature extraction.
* Uses Cosine Similarity to measure resume relevance.

### Candidate Ranking

* Generates candidate scores based on:

  * Resume similarity score
  * Skill match percentage
* Produces ranked candidate lists.

### Skill Gap Identification

* Highlights missing skills for each candidate.
* Provides actionable insights for recruiters and applicants.

### Exportable Results

* Saves ranked candidate information to CSV format.
* Enables easy reporting and analysis.

---

## Technologies Used

* Python
* NLTK
* Scikit-learn
* Pandas
* PDFPlumber
* NumPy
* Matplotlib

---

## Machine Learning & NLP Techniques

### Natural Language Processing

* Text Cleaning
* Tokenization
* Stopword Removal
* Skill Extraction

### Feature Engineering

* TF-IDF Vectorization

### Similarity Measurement

* Cosine Similarity

### Candidate Scoring Logic

Final Candidate Score:

Final Score = (0.7 × Similarity Score) + (0.3 × Skill Match Score)

Where:

* Similarity Score measures overall relevance of the resume to the job description.
* Skill Match Score measures the percentage of required skills present in the resume.

---

## Project Workflow

1. Load Resume PDFs
2. Extract Resume Text
3. Clean and Preprocess Text
4. Extract Skills
5. Parse Job Description
6. Compute TF-IDF Vectors
7. Calculate Cosine Similarity
8. Identify Skill Matches
9. Detect Skill Gaps
10. Generate Candidate Scores
11. Rank Candidates
12. Export Results

---

## Sample Output

| Rank | Candidate       | Similarity Score | Skill Match | Final Score |
| ---- | --------------- | ---------------- | ----------- | ----------- |
| 1    | resume1.pdf | 92.5             | 100.0       | 94.7        |
| 2    | resume2.pdf | 84.3             | 85.7        | 84.7        |
| 3    | resume3.pdf | 68.4             | 57.1        | 65.0        |

### Skill Gap Example

Candidate B Missing Skills:

* NLP
* NumPy

---

## Business Impact

This solution helps:

* Recruiters shortlist candidates faster.
* HR teams reduce manual screening effort.
* Organizations identify qualified candidates efficiently.
* Applicants understand missing skills for targeted career improvement.

---

## Future Enhancements

* Streamlit-based web application.
* Advanced skill extraction using spaCy Named Entity Recognition.
* Experience and education scoring.
* ATS-style resume compatibility analysis.
* Interactive recruiter dashboard.
* Real-time resume uploads and evaluation.

---

## Learning Outcomes

Through this project, the following skills were developed:

* Natural Language Processing (NLP)
* Resume Parsing
* Text Preprocessing
* Feature Extraction
* Machine Learning-Based Ranking Systems
* Candidate Evaluation Techniques
* Similarity Analysis
* Data Processing and Visualization

---

## Internship Information

Project Developed As Part Of:

Machine Learning Internship Program

Future Interns – Task 3

Project Title:
Resume / Candidate Screening System

---

## Author

Bhagya

Aspiring AI/ML Engineer | Python Developer | Robotics Enthusiast | Designer & Video Editor
