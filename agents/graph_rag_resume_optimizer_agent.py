from vector_db.retriever import retrieve_context
from utils.llm import ask_llm


def graph_rag_resume_optimizer_agent(state):
    resume_text = state["resume_data"]
    skills = resume_text.get("skills", [])
    education = resume_text.get("education", [])
    projects = resume_text.get("projects", [])
    certifications = resume_text.get("certifications", [])
    achievements = resume_text.get("achievements", [])
    job_description = state["job_description"]

    query = f"""
    Resume Optimization Guidelines

    Job Description: {job_description}

    Resume: {resume_text}
 
    """

    rag_context = retrieve_context(query=query,k=5)
    
    prompt = f"""
You are an expert ATS Resume Reviewer and Resume Writer.

Use ONLY the retrieved context provided below.

Retrieved Context:
{rag_context}

Candidate Resume:
{resume_text}

Target Job Description:
{job_description}

TASK 1:
Create an ATS REVIEW REPORT.

Include:

1. Resume Strengths
2. ATS Issues
3. Skills Match Analysis
4. Education Relevance
5. Project Relevance
6. Missing Keywords
7. Resume Weaknesses
8. ATS Improvement Suggestions

IMPORTANT:

Every finding MUST include evidence.

Do NOT make generic statements.

Support findings using:

- Skills
- Education
- Projects
- Certifications
- Achievements

Examples:

Strength:
Python found in Skills section.

Strength:
Traffic Congestion Prediction project demonstrates
Machine Learning and Scikit-Learn experience.

Strength:
M.Sc Artificial Intelligence and Machine Learning
is highly relevant to the target role.

Weakness:
Docker not found in Skills, Projects or Experience.

Weakness:
AWS not found in Skills, Projects or Experience.

Weakness:
No certifications found.

Weakness:
No professional experience found.

------------------------------------------------

TASK 2:
Create a COMPLETE ATS-OPTIMIZED RESUME.

Requirements:

- Professional Summary
- Technical Skills
- Projects
- Experience
- Education

Include ATS score breakdown:

Keyword Match: X/10
Education Relevance: X/10
Project Relevance: X/10
Experience Strength: X/10
ATS Formatting Readiness: X/10

Overall ATS Readiness Score: X/10

Provide a Recruiter Perspective section:

What would impress a recruiter?

What would concern a recruiter?

Limit to 3 bullet points each.


Rules:

- **NEVER invent experience.**
- **NEVER invent projects.**
- **NEVER invent certifications.**
- **NEVER invent achievements.**

NEVER invent:
- email
- linkedin
- github
- phone

If information is unavailable write:"Information not available"

Never add technologies that are not present in candidate resume.

Use ATS-friendly formatting.

IMPORTANT ATS ANALYSIS RULES

Evaluate:

1. Skills Match
2. Education Relevance
3. Project Relevance
4. Certifications
5. Achievements
6. Missing Keywords
7. ATS Compatibility

Base your ATS analysis on ALL available evidence.

Do NOT analyze only skills.

If projects demonstrate relevant technologies,
mention them.

If education is relevant,
mention it.

If certifications are absent,
mention it as a gap.

If achievements are absent,
mention it as a weakness.

Support every ATS finding with evidence from:
- Skills
- Projects
- Education
- Certifications
- Achievements

Return your answer EXACTLY in this format:

ATS_REPORT:
<ATS report here>

OPTIMIZED_RESUME:
<full optimized resume here>

IMPORTANT:

When analyzing candidate skills,
use the skills present in Structured Resume Data.

STRUCTURED RESUME DATA

Candidate Skills:
{skills}

Education:
{education}

Projects:
{projects}

Certifications:
{certifications}

Achievements:
{achievements}

Full Parsed Resume:
{resume_text}

DO NOT say the candidate only has Python and SQL
if additional skills are present.

For ATS analysis:

Present:

Current Skills:
<all parsed skills>

Missing Skills:
<skills missing from JD>

Base ATS report on Structured Resume Data.
"""
    print("\nExecuting graph_rag_resume_optimizer_agent")
    print("\nRetrieved Context Length:",len(rag_context))
    response = ask_llm(prompt)
    ats_report = ""
    optimized_resume = ""

    if "OPTIMIZED_RESUME:" in response:
        parts = response.split("OPTIMIZED_RESUME:")
        ats_report = (parts[0].replace("ATS_REPORT:","").strip())
        optimized_resume = parts[1].strip()
    else:
        ats_report = response
        optimized_resume = response
    state['retrieved_context'] = rag_context
    state['optimized_resume'] = optimized_resume
    state['ats_report']=ats_report

    # return {
    #     "retrieved_context":rag_context[:1000],
    #     "optimized_resume":optimized_resume
    # }
    return {"ats_report":ats_report,
            "optimized_resume":optimized_resume}