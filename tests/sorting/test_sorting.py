from src.pre_built.sorting import sort_by


mock_order = [
    {
        'title': 'Web developer',
        'min_salary': 'invalid',
        'max_salary': 'invalid',
    },
    {
        'title': 'Front end developer',
        'max_salary': '1000',
    },
    {
        'title': 'Back end developer',
        'max_salary': '3000',
    },

    {
        'title': 'Full stack end developer',
        'min_salary': '4000',
        'max_salary': '8000',
    }
]

path = 'tests/mocks/jobs.csv'


def test_sort_by_criteria():
    sort_by(mock_order, 'title')
    assert mock_order == mock_order

    sort_by(mock_order, 'min_salary')
    assert mock_order == mock_order

    sort_by(mock_order, 'max_salary')
    assert mock_order == mock_order
