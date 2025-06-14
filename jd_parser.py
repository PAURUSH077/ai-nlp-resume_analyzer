# jd_parser.py

def extract_jd_skills(jd_file_path):
    with open(jd_file_path, "r", encoding="utf-8") as f:
        jd_text = f.read()
    jd_keywords = [word.strip().lower() for word in jd_text.split() if len(word) > 2]
    return set(jd_keywords)
