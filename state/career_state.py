from typing import TypedDict

class CareerState(TypedDict):
    resume_text:str
    resume_data:dict
    job_description:str
    job_skills:list
    job_data:dict
    ats_scores:dict
    #ats_analysis:dict
    match_result:dict
    recommendations:str
    ats_report:str
    ats_analysis:str
    optimized_resume:str
    cover_letter:str
    retrieved_context:str
    resume_doc_path:str
    cover_letter_doc_path:str
    