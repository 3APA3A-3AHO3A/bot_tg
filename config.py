import openpyxl

# test_bot BOT_TOKEN = '5687247228:AAFPTFmvJCtVU_weFVUnwCf0i7BPkMNAhiA'
BOT_TOKEN = '5221109021:AAGl2b6Vs9Id1Yzss89l-34uwMkQcFNnETQ'
BOT_TOKEN_logs = '5158112868:AAEKWw51sG5IT9Sxqbb4F1A6TTaaHOHyrQA'
admin_id = 454589284

excel_db = openpyxl.load_workbook('Database/database.xlsx')

ex_user = excel_db.get_sheet_by_name("Пользователи")
ex_swats = excel_db.get_sheet_by_name("Спецназ")
worksheet_build_pvp = excel_db.get_sheet_by_name("ПВП")
worksheet_build_bg = excel_db.get_sheet_by_name("БГ")

users = []
swats = []
pvp = []
bg = []

for i in range(ex_user.max_row - 1):
    id_users = ex_user.cell(row=(i+2), column=1).value
    users.append(id_users)

for i in range(ex_swats.max_row - 1):
    id_swats = ex_swats.cell(row=(i+2), column=1).value
    swats.append(id_swats)

for i in range(worksheet_build_pvp.max_row - 1):
    id_pvp = worksheet_build_pvp.cell(row=(i+2), column=1).value
    pvp.append(id_pvp)

for i in range(worksheet_build_bg.max_row - 1):
    id_bg = worksheet_build_bg.cell(row=(i+2), column=1).value
    bg.append(id_bg)
