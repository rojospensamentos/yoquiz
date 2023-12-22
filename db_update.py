import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json', scope)
gc = gspread.service_account(filename='gs_credentials.json')
sh = gc.open('user_db')

sheet_id='1iU0EFHvDF3MNEwWH2TFHFkKHS0McGrdZyOyzjs12fVc'
def teamdata_update(team_name,team_city):
    worksheet = sh.worksheet('teams')
    team_id = 2
    if team_name==worksheet.find(team_name):
        print('Ваша команда успешно авторизована')
    else: worksheet.insert_row([team_id,team_name,team_city])
    print('Ваша команда успешно зарегистрирована')

teamdata_update('Team_2','Volgograd')





