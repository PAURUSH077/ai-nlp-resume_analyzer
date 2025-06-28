🧠 NLP-Based Resume Analyzer
A smart Python-based Resume Analyzer that uses Natural Language Processing (NLP) to parse, analyze, and evaluate resumes based on job relevance. Designed to help recruiters and applicants get instant feedback on resumes.

🚀 Features
📄 Extracts text from PDF resumes

🧠 Applies NLP to analyze key resume sections (skills, experience, education)

✅ Matches resume content with job requirements

📊 Generates relevance score and improvement suggestions

🧰 Shows skill gaps and highlights strengths

🛠️ Tools & Technologies
Python

spaCy – for NLP processing

PyPDF2 / pdfminer / fitz (PyMuPDF) – for reading PDFs

scikit-learn / Transformers – for vectorization & similarity checks (if applicable)

Streamlit / Tkinter (Optional UI layer)

📁 Project Structure
resume-analyzer/
├── __pycache__/                 # Python cache files
├── images/                     # UI or output screenshots
│   ├── Screenshot 2025-06-15 031820.png
│   ├── Screenshot 2025-06-15 031906.png
│   └── Screenshot 2025-06-15 031920.png
├── app.py                      # Main entry point (Streamlit or Flask)
├── ats_checker.py              # Checks resume against ATS-friendly rules
├── jd_parser.py                # Extracts key info from job description
├── job_description.txt         # Sample job description input
├── match_engine.py             # Core logic for matching resume to job description
├── readme.md.txt               # Backup readme or raw content
├── resume_parser.py            # Parses resumes (.pdf, .docx)
├── sample_resume.docx          # Sample resume for testing
├── temp_jd.txt                 # Cleaned job description (intermediate)
├── temp_resume.pdf             # Resume file input
├── temp_resume_cleaned.txt     # Preprocessed resume text
├── .gitattributes              # Git config file

🛠️ Tech Stack
Python 3.8+

NLP Libraries: spaCy, re

PDF Parsing: PyMuPDF / docx2txt

Text Similarity: Cosine similarity, TF-IDF

Optional UI: Streamlit or Flask

Visualization: Matplotlib / Plotly (optional)

