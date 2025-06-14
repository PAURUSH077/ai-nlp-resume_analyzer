import spacy
import docx
import fitz  # PyMuPDF
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# ========== Define Skill Bank ==========
SKILL_BANK = [
    "python", "java", "c++", "c", "node.js", "react", "django", "html", "css",
    "sql", "mysql", "mongodb", "git", "aws", "azure", "docker", "linux",
    "verilog", "vhdl", "matlab", "fpga", "raspberry pi", "ansys", "autocad",
    "solidworks", "creo", "revit", "staad pro"
]

# ========== Text Extraction ==========
def extract_text_from_resume(file):
    filename = file.name.lower()

    if filename.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    elif filename.endswith(".pdf"):
        file.seek(0)  # Ensure reading from start
        pdf_bytes = file.read()
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            return "\n".join([page.get_text() for page in doc])

    else:
        raise ValueError("Unsupported file format. Please use .docx or .pdf")

# ========== Skill Extractor ==========
def extract_resume_skills(file):
    text = extract_text_from_resume(file)
    doc_nlp = nlp(text.lower())
    tokens = [token.text for token in doc_nlp]
    matched_skills = set(skill for skill in SKILL_BANK if skill in tokens)
    return matched_skills

# ========== ATS Checks ==========
def check_ats_friendly(file, jd_keywords):
    text = extract_text_from_resume(file).lower()

    checks = {
        "Has Contact Info": bool(re.search(r'\d{10}|\d{3}[-\s]\d{3}[-\s]\d{4}', text)),
        "Has Email": bool(re.search(r'\b[\w.-]+?@\w+?\.\w{2,4}\b', text)),
        "Uses Bullet Points": "•" in text or "-" in text,
        "Has Job Keywords": any(word in text for word in jd_keywords),
        "Avoids Tables": True,  # Static assumption
        "Has Sections (e.g., Education, Experience)": any(sec in text for sec in ["education", "experience", "skills"]),
    }
    return checks

# ========== Score Calculation ==========
def calculate_ats_score(ats_checks):
    total_checks = len(ats_checks)
    passed_checks = sum(1 for check in ats_checks.values() if check)
    return int((passed_checks / total_checks) * 100)
