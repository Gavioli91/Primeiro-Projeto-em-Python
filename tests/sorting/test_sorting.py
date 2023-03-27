from src.pre_built.sorting import sort_by


mock_order = {
        'title': 'Web developer',
        'min_salary': 'invalid',
        'max_salary': 'invalid',
    }

path = 'tests/mocks/jobs.csv'


def test_sort_by_criteria():
    assert sort_by(path)[0] == mock_order
