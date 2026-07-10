from docx import Document

def generate_cover_letter_doc(cover_letter,output_path="generated_cover_letter.docx"):
    doc = Document()
    for line in cover_letter.split("\n"):
        doc.add_paragraph(line)

    doc.save(output_path)

    return output_path