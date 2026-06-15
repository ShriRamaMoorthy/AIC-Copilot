from utils.pdf_parser import extract_text_from_pdf
from agents.resume_summarizer import generate_resume_summary

text = extract_text_from_pdf(
    r"C:\Users\rams6\Downloads\Resume.pdf"
)

summary = generate_resume_summary(text)
print(summary)