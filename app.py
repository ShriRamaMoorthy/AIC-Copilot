import streamlit as st
import tempfile
from agents.resume_parser import parse_resume
from agents.resume_summarizer import generate_resume_summary
import json

from utils.pdf_parser import(
    extract_text_from_pdf
)

st.set_page_config(
    page_title="AI Career Copilot",
    layout = "wide"
)

st.title("AI Career Copilot")

uploaded_file = st.file_uploader(
    "upload Resume",
    type=['pdf']
)

if uploaded_file:
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    resume_text = extract_text_from_pdf(
        pdf_path
    )

    st.subheader(
        "Extracted Resume Text"
    )

    resume_data = parse_resume(resume_text)
    summary = generate_resume_summary(
        json.dumps(resume_data,indent=2)
    )

    st.subheader("Professional Summary")
    st.write(summary)

    st.text_area(
        "",
        resume_text,
        height=400
    )

    st.success("Resume Uploaded!!!")
    

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Skills Found",
            len(resume_data.get("skills",[]))
        )

    with col2:
        st.metric(
            "Experience Entries",
            len(resume_data.get("experience",[]))
        )