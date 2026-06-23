from generators.resume_doc_generator import(generate_resume_doc)
from generators.cover_letter_doc_generator import(generate_cover_letter_doc)

def graph_document_generator_agent(state):
    print("\nExecuting graph_document_generator_agent")

    resume_path = generate_resume_doc(state["optimized_resume"])
    cover_letter_path = generate_cover_letter_doc(state["cover_letter"])

    state['resume_doc_path'] = resume_path
    state['cover_letter_doc_path'] = (cover_letter_path)

    return {
        "resume_doc_path":resume_path,
        "cover_letter_doc_path":cover_letter_path
    }