import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Player import Player


class Sheet(object):
    def get_player_list(self):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credsPy.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Scoring Sheet Tally").sheet1
        # Extract and print all of the values
        players = sheet.range("A2:A7")
        playerList = []

        for x in players:
            numPaid = sheet.cell(x.row, x.col + 1)
            player = Player(x.value, numPaid.value)
            playerList.append(player)

        return playerList
