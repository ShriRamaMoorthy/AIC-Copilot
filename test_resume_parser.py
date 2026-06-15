from utils.pdf_parser import(
    extract_text_from_pdf
)

from agents.resume_parser import(
    parse_resume
)

text = extract_text_from_pdf(
    r"C:\Users\rams6\Downloads\Resume.pdf"
)

result = parse_resume(text)

print(result)