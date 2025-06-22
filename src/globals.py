from openpyxl import load_workbook

file_path = 'data/Harvard_JCHS_State_Nations_Housing_2022.xlsx'

# House Price Index data
pi_sheet_name = 'W-8'
pi_cell_range = 'A5:AG387'

# Load workbook and sheet
pi_wb = load_workbook(filename=file_path, data_only=True)
pi_ws = pi_wb[pi_sheet_name]