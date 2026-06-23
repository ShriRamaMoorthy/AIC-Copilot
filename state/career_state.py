from typing import TypedDict

class CareerState(TypedDict):
    resume_text:str
    resume_data:dict
    job_description:str
    job_skills:list
    match_result:dict
    recommendations:str
    ats_report:str
    optimized_resume:str
    cover_letter:str
    retrieved_context:str
    resume_doc_path:str
    cover_letter_doc_path:str
    