from openpyxl import Workbook
from openpyxl.utils import get_column_letter


class Spreadsheet:
    def __init__(self):
        self.workbook = Workbook()
        self.filename = 'results.xlsx'
        worksheet = self.workbook.active
        worksheet.merge_cells('A1:C1')
        worksheet['A1'] = 'CMUSphinx'
        worksheet.merge_cells('D1:F1')
        worksheet['D1'] = 'Google Speech-to-Text'
        worksheet['A2'] = 'Latency (seconds)'
        worksheet['B2'] = 'Latency (milliseconds)'
        worksheet['C2'] = 'Word Error Rate'
        worksheet['D2'] = 'Latency (seconds)'
        worksheet['E2'] = 'Latency (milliseconds)'
        worksheet['F2'] = 'Word Error Rate'
        self.tables = ['CMUSphinx', 'Google Speech-to-Text']
        self.next_col = 7
    
    def add_speech_engine(self, speech_engine_name):
        worksheet = self.workbook.active
        start_col = get_column_letter(self.next_col)
        end_col = get_column_letter(self.next_col + 2)
        worksheet.merge_cells(f'{start_col}1:{end_col}1')
        worksheet[f'{start_col}1'] = speech_engine_name
        worksheet[f'{start_col}2'] = 'Latency (seconds)'
        worksheet[f'{get_column_letter(self.next_col + 1)}2'] = 'Latency (milliseconds)'
        worksheet[f'{end_col}2'] = 'Word Error Rate'
        self.next_col += 3
        self.tables.append(speech_engine_name)
    
    def populate_table(self, speech_engine_name, data):
        table_index = self.tables.index(speech_engine_name)
        if table_index < 0:
            raise Exception(f'speech recognition engine {speech_engine_name} does not exist')
        cur_col = self.next_col - 3 * (len(self.tables) - table_index)
        latency_s = get_column_letter(cur_col)
        latency_ms = get_column_letter(cur_col + 1)
        wer = get_column_letter(cur_col + 2)
        row = 3
        for data_point in data:
            worksheet[f'{latency_s}{row}'] = data_point.seconds
            worksheet[f'{latency_ms}{row}'] = data_point.milliseconds
            worksheet[f'{wer}{row}'] = data_point.wer
            row += 1

    # data should be a tuple of timedelta and accuracy
    def add_data(self, data):
        worksheet = self.workbook.active
        for data_point in data:
            worksheet[f'A{self.row}'] = data_point.seconds
            worksheet[f'B{self.row}'] = data_point.milliseconds
            worksheet[f'C{self.row}'] = data_point.wer
