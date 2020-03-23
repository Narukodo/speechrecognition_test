import pytest
from experiment.experiment import Experiment

edit_distance_tests = [
    pytest.param([], [], 0, id='trivial'),
    pytest.param(['P', 'O', 'L', 'Y', 'N', 'O', 'M', 'I', 'A', 'L'], ['E', 'X', 'P', 'O', 'N', 'E', 'N', 'T', 'I', 'A', 'L'], 6, id='correct numebr of edits'),
    pytest.param(['P', 'O', 'L', 'Y', 'N', 'O', 'M', 'I', 'A', 'L'], [], 10, id='tracks removing all elements'),
    pytest.param([], ['H', 'E', 'L', 'L', 'O'], 5, id='works for only adding characters'),
    pytest.param(['H', 'E', 'L', 'L', 'O'], ['J', 'E', 'L', 'L', 'O'], 1, id='works when only one replacement is needed'),
    pytest.param(['H', 'E', 'L', 'L', 'O'], ['A', 'B', 'C', 'D', 'E'], 5, id='works when all letters need to be replaced')
]

exp = Experiment()

@pytest.mark.parametrize('M, N, result_ed', edit_distance_tests)
def test_edit_distance(M, N, result_ed):
    assert exp.edit_distance(M, N) == result_ed
