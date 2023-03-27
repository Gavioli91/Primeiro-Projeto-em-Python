from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:

    salary_reader = read(path)
    job_list = []

    for salary in salary_reader:
        if salary['max_salary'] and salary['max_salary'] != 'invalid':
            job_list.append(int(salary['max_salary']))

    return max(job_list)


def get_min_salary(path: str) -> int:

    salary_reader = read(path)
    job_list = []

    for salary in salary_reader:
        if salary['min_salary'] and salary['min_salary'] != 'invalid':
            job_list.append(int(salary['min_salary']))

    return min(job_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        salary = int(salary)

    except KeyError:
        raise ValueError
    except TypeError:
        raise ValueError
    else:
        if max_salary < min_salary:
            raise ValueError

        return max_salary >= salary >= min_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
