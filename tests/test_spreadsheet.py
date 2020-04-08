import pytest

from experiment import spreadsheet, DataPoint
from openpyxl.utils import get_column_letter

get_table_column_tests = [
    pytest.param(['table1', 'table2'], 'nonExistent', None, False, id='should raise for non-existent tables'),
    pytest.param(['table1', 'table2', 'table3', 'table4'], 'table4', 10, True, id='should correctly return column for last table'),
    pytest.param(['table1', 'table2', 'table3', 'table4'], 'table2', 4, True, id='should correctly return column for middle table'),
    pytest.param(['table1', 'table2', 'table3', 'table4'], 'table1', 1, True, id='should correctly return column for first table')
]


@pytest.mark.parametrize('setup_table, engine_name, expected_column, should_pass', get_table_column_tests)
def test_get_table_index_returns_correct_cell_column(setup_table, engine_name, expected_column, should_pass):
    sp = spreadsheet.Spreadsheet()
    sp.tables = setup_table
    sp.next_col = 3 * len(setup_table) + 1
    if should_pass:
        assert sp.get_table_column(engine_name) == expected_column
    else:
        with pytest.raises(Exception):
            sp.get_table_column(engine_name)
