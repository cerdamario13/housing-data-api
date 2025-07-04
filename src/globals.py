from openpyxl import load_workbook

file_path = 'data/Harvard_JCHS_State_Nations_Housing_2022.xlsx'
pi_wb = load_workbook(filename=file_path, data_only=True)

# House Price Index data
pi_sheet_name = 'W-8'
pi_cell_range = 'A5:AG387'
# Load workbook and sheet
pi_ws = pi_wb[pi_sheet_name]

# Metro Area–Typical Home Value and Mortgage Affordability: April 2022
metro_affordability_sheet_name = 'W-7'
metro_affordability_cell_range = 'A5:E917'
metro_affordability_ws = pi_wb[metro_affordability_sheet_name]

# Year over Year change in rent and home value
yoy_change_sheet_name = 'W-10'
yoy_change_cell_range = 'A4:O107'
yoy_change_ws = pi_wb[yoy_change_sheet_name]