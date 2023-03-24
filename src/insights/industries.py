from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:

    jobs_list = read(path)
    job_industries = []
    for job in jobs_list:
        if not job['industry'] in job_industries and job['industry']:
            job_industries.append(job['industry'])
    return job_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:

    return [
        job for job in jobs
        if job['industry'] == industry
    ]
