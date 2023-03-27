from src.pre_built.sorting import sort_by


mock_job = [
    {"max_salary": 1000, "min_salary": 1, "date_posted": "2021-01-01"},
    {"max_salary": 200, "min_salary": 0, "date_posted": "2023-01-01"},
    {"max_salary": 100, "min_salary": 10, "date_posted": "2022-01-01"},
]

job_min_salary = [
    {"max_salary": 200, "min_salary": 0, "date_posted": "2023-01-01"},
    {"max_salary": 1000, "min_salary": 1, "date_posted": "2021-01-01"},
    {"max_salary": 100, "min_salary": 10, "date_posted": "2022-01-01"},
]

job_by_date = [
    {"max_salary": 200, "min_salary": 0, "date_posted": "2023-01-01"},
    {"max_salary": 100, "min_salary": 10, "date_posted": "2022-01-01"},
    {"max_salary": 1000, "min_salary": 1, "date_posted": "2021-01-01"},
]


def test_sort_by_criteria():
    sort_by(mock_job, 'max_salary')
    assert mock_job == mock_job

    sort_by(mock_job, 'min_salary')
    assert mock_job == job_min_salary

    sort_by(mock_job, 'date_posted')
    assert mock_job == job_by_date
