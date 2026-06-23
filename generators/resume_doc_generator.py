from docx import Document

def generate_resume_doc(optimized_resume,output_path="generated_resume.docx"):
    doc = Document()

    for line in optimized_resume.split("\n"):
        doc.add_paragraph(line)

    doc.save(output_path)

    return output_path