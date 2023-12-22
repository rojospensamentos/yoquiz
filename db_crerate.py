import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json', scope)
gc = gspread.service_account(filename='gs_credentials.json')
#sh = gc.create('user_db')
#sh.share('rojospensamentos@gmail.com', perm_type='user', role='writer')
sh = gc.open('user_db')
#worksheet = sh.add_worksheet(title='teams', rows="100", cols="4")
worksheet = sh.worksheet('teams')
worksheet.update('A1', 'team_id')
worksheet.update('B1', 'team_name')
worksheet.update('C1', 'team_city')
worksheet.update('D1', 'joined')
worksheet.update('E1', 'game_id')
worksheet.update('D1', 'game_data')