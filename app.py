import streamlit as st
from resume_parser import extract_resume_skills, check_ats_friendly, calculate_ats_score, extract_text_from_resume

# Dummy JD extractor (can be replaced with NLP-based version)
def extract_jd_skills(jd_text):
    return [word.lower() for word in jd_text.split() if len(word) > 2]

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI-Powered Resume Analyzer")
st.markdown("Upload your resume and job description to get ATS score and match percentage.")

resume_file = st.file_uploader("Upload Resume (.docx or .pdf)", type=["docx", "pdf"])
use_embedded_jd = st.checkbox("📎 My resume contains the Job Description (JD) at the bottom")

jd_text = ""

if resume_file:
    if use_embedded_jd:
        full_text = extract_text_from_resume(resume_file)
        lines = full_text.strip().splitlines()
        jd_text = "\n".join(lines[-10:])  # Extract last 10 lines as JD
        resume_text = "\n".join(lines[:-10])

        # Convert text to file-like object
        from io import BytesIO
        resume_file.seek(0)
        resume_copy = BytesIO(resume_file.read())
        resume_copy.name = resume_file.name

        resume_skills = extract_resume_skills(resume_copy)

    else:
        jd_file = st.file_uploader("Upload Job Description (.txt)", type=["txt"])
        if not jd_file:
            st.warning("Please upload a Job Description file or check the embedded JD option.")
            st.stop()
        jd_text = jd_file.read().decode("utf-8")
        resume_skills = extract_resume_skills(resume_file)

    jd_keywords = extract_jd_skills(jd_text)

    st.subheader("✅ Extracted Resume Skills")
    st.write(", ".join(resume_skills) if resume_skills else "No skills found.")

    ats_result = check_ats_friendly(resume_file, jd_keywords)
    ats_score = calculate_ats_score(ats_result)

    st.subheader("📊 ATS Friendliness Report")
    for check, passed in ats_result.items():
        st.write(f"{check}: {'✅' if passed else '❌'}")

    st.subheader("📈 ATS Score")
    st.write(f"{ats_score} / 100")

    st.subheader("🔍 Skill Match Report")
    matched = resume_skills & set(jd_keywords)
    missing = set(jd_keywords) - resume_skills
    match_percent = round((len(matched) / len(jd_keywords)) * 100, 2) if jd_keywords else 0

    st.write(f"🎯 Match Score: {match_percent}%")
    st.write(f"✅ Matched Skills: {', '.join(matched) if matched else 'None'}")
    st.write(f"❌ Missing Skills: {', '.join(missing) if missing else 'None'}")
