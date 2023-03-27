from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:

    industries_reader = read(path)
    job_industries = set()

    for industry in industries_reader:
        if len(industry['industry']) > 0:
            job_industries.add(industry['industry'])

    return job_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:

    job_industry = [job for job in jobs if job['industry'] == industry]
    return job_industry
