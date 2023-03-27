from src.pre_built.brazilian_jobs import read_brazilian_file


mock_translate = {
    'title': 'Motorista',
    'salary': '3000',
    'type': 'full time',
}

path = 'tests/mocks/brazilians_jobs.csv'


def test_brazilian_jobs():
    assert read_brazilian_file(path)[1] == mock_translate
