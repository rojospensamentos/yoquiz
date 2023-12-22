import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json', scope)
client = gspread.authorize(credentials)
sheet = client.create('user_database')
sheet.share('rojospensamentos@gmail.com', perm_type='user', role='writer')
worksheet = sheet.add_worksheet(title='teams', rows='100', cols='4')
worksheet.update('A1', 'team_id')
worksheet.update('B1', 'team_name')
worksheet.update('C1', 'team_city')
worksheet.update('D1', 'joined')
