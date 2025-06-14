from resume_parser import extract_resume_skills, SKILL_BANK

# Step 1: Extract resume skills
resume_skills = extract_resume_skills("sample_resume.docx")  # Replace with your actual resume file

# Step 2: Extract JD skills from a text file
with open("job_description.txt", "r", encoding="utf-8") as f:
    jd_text = f.read().lower()

jd_tokens = jd_text.split()
jd_skills = set(skill for skill in jd_tokens if skill in SKILL_BANK)

# Step 3: Normalize
resume_skills = set(skill.lower() for skill in resume_skills)
jd_skills = set(skill.lower() for skill in jd_skills)

# Step 4: Compare sets
matched = resume_skills & jd_skills
missing = jd_skills - resume_skills

# Step 5: Scoring
match_percent = round((len(matched) / len(jd_skills)) * 100, 2) if jd_skills else 0

# Step 6: Display Results
print(f"\n✅ Skill Match Score: {match_percent}%")
print(f"\n✅ Matched Skills: {', '.join(sorted(matched)) if matched else 'None'}")
print(f"\n❌ Missing Skills: {', '.join(sorted(missing)) if missing else 'None'}")
