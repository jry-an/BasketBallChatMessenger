from FoxDataService import FoxDataService
from facebookchat import ChatService
from fbchat import Client
from datetime import *


def get_game_list():
    fox_data_service = FoxDataService()
    game_list = fox_data_service.get_games()
    for x in game_list:
        print(x.date + " " + x.time + " at " + x.location)
    return game_list


if __name__ == '__main__':

    current_date = date.today().strftime("%d/%m/%y") + " (Mon)"
    game = get_game_list()
    for x in game:
        if current_date == x.date:
            chat_serv = ChatService()
            print("Enter FB email address: ")
            client_email = input()
            print("Enter FB password: ")
            client_password = input()
            client = Client(client_email, client_password)
            print("enter group id: ")
            group_id = input()
            chat_serv.message_score_sheet_status(client, group_id)
            chat_serv.message_next_game(game, client, group_id)
            chat_serv.get_lowest_paid(client, group_id)
            break

