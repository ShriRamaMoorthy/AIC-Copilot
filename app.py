import streamlit as st
import tempfile

from utils.pdf_parser import extract_text_from_pdf
from agents.resume_parser import parse_resume
from agents.resume_summarizer import generate_resume_summary
from agents.job_parser import extract_job_skills
from agents.recommendation_agent import generate_recommendation
from utils.matching import calculate_match_score

st.set_page_config(
    page_title="AI Career Copilot",
    layout = "wide"
)

st.title("AI Career Copilot")

st.markdown(
    "Upload your rename and compare it against a job description." \
    "Get match scores , skill gaps and personalized recommendations"
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf","doc"]
)

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

        resume_text = extract_text_from_pdf(pdf_path)
        resume_data = parse_resume(resume_text)
        summary = generate_resume_summary(resume_text)

        st.success("Resume Uploaded Successfully!!!")
        st.subheader("Resume Overview")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Skills Found",len(resume_data.get("skills",[])))
        
        with col2:
            st.metric("Experience Entries",len(resume_data.get("experience",[])))

        st.subheader("Professional Summary")
        st.write(summary)

        st.subheader("Parsed Resume Data")

        st.json(resume_data)

        with st.expander("View extracted Resume text"):
            st.text_area("Resume Text",resume_text,height=350)
        st.divider()

        st.subheader("Job Match Analysis")
        job_description = st.text_area("Paste Job Description",height=250)

        if st.button("Analyze Match"):
            if not job_description.strip():
                st.warning("Please paste a job description:")
            else:
                job_data = extract_job_skills(job_description)
                job_skills = job_data.get("skills",[])

                resume_skills = resume_data.get("skills",[])

                match_result = calculate_match_score(resume_skills,job_skills)

                recommendations = generate_recommendation(match_result["missing_skills"],job_description)

                st.subheader("Match Results")

                st.metric("Match Score",f"{match_result['match_score']}%")

                st.subheader("Matched Skills")
                if match_result["matched_skills"]:
                    st.success(", ".join(match_result["matched_skills"]))
                else:
                    st.info("No matched skills found.")
                
                st.subheader("Job Skills")
                st.write(job_skills)
                st.subheader("Career Recommendations")
                st.write(recommendations)