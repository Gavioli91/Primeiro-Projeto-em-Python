from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path, encoding="utf-8") as file:

        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_list = list(jobs_reader)

    return jobs_list


def get_unique_job_types(path: str) -> List[str]:

    jobs_reader = read(path)
    job_type = set()

    for job in jobs_reader:
        job_type.add(job["job_type"])

    return job_type


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:

    job_type = [job for job in jobs if job['job_type'] == job_type]
    return job_type
