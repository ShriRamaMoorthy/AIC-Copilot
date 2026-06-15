from utils.pdf_parser import extract_text_from_pdf

text = extract_text_from_pdf(
    r"C:\Users\rams6\Downloads\Resume.pdf"
)

print(text[:3000])