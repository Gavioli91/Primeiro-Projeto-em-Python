from functools import lru_cache
from os import path
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """


with open(path, encoding="utf-8") as file:
    jobs_reader = csv.reader(file, delimiter=",", quotechar='"')
    headers, *jobs = jobs_reader
    jobs_list = []
    for job in jobs:
        job_dict = {}
        for i, header in enumerate(headers):
            job_dict[header] = job[i]
        jobs_list.append(job_dict)

    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_list = read(path)
    job_types = []
    for job in jobs_list:
        if not job['job_type'] in job_types:
            job_types.append(job['job_type'])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
