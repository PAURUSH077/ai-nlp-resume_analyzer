import os
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document

def extract_text_from_file(filepath):
    if filepath.endswith(".pdf"):
        try:
            return extract_pdf_text(filepath)
        except:
            return ""
    elif filepath.endswith(".docx"):
        try:
            doc = Document(filepath)
            return "\n".join([para.text for para in doc.paragraphs])
        except:
            return ""
    return ""

def check_ats_friendly(filepath, jd_keywords):
    ats_score = 0
    issues = []

    # 1. File type check
    if filepath.endswith(".docx") or filepath.endswith(".pdf"):
        ats_score += 1
    else:
        issues.append("Use a .docx or .pdf format.")

    # 2. Text extraction
    text = extract_text_from_file(filepath)
    if len(text.strip()) < 50:
        issues.append("Resume text is hard to extract. Avoid images or complex formatting.")
    else:
        ats_score += 1

    # 3. Keyword coverage
    found = [kw for kw in jd_keywords if kw.lower() in text.lower()]
    coverage = len(found) / len(jd_keywords) if jd_keywords else 0
    if coverage >= 0.6:
        ats_score += 1
    else:
        issues.append("Not enough keywords from JD are present.")

    return {
        "ATS Score (out of 3)": ats_score,
        "Missing ATS Elements": issues,
        "Matched Keywords": found
    }
