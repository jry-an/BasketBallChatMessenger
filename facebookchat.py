from fbchat.models import *
from Sheet import Sheet
import random as rand
from datetime import date

class ChatService:
    def message_score_sheet_status(self, client, group_id):
        sheet = Sheet()
        player_list = sheet.get_player_list()
        message = "Score Sheet Tally: \n" + ''.join(str(e.name + " " + e.timesPaid + "\n") for e in player_list)
        client.send(Message(text=message), thread_id=group_id, thread_type=ThreadType.GROUP)
        # read_id='3572303616120429', thread_type=ThreadType.GROUP

    def get_lowest_paid(self, client, group_id):
        sheet = Sheet()
        player_list = sheet.get_player_list()
        # select who is paying team sheet
        min_times_paid = []
        lowest_times_paid = 100
        for player in player_list:
            if int(player.timesPaid) < lowest_times_paid:
                lowest_times_paid = int(player.timesPaid)

        for player in player_list:
            if int(player.timesPaid) == lowest_times_paid:
                min_times_paid.append(player.name)

        secure_random = rand.SystemRandom()
        message = "Player to pay next is: " + secure_random.choice(min_times_paid)
        client.send(Message(text=message), thread_id=group_id, thread_type=ThreadType.GROUP)

    def message_next_game(self, game, client, group_id):
        current_date = date.today().strftime("%d/%m/%y") + " (Mon)"
        print("Current date == " + current_date)

        for x in game:
            if x.date == current_date:
                message = ("Today's game is: " + x.date + "\nTime: " + x.time + "\nVenue: " + x.location)
                print(x.date + " " + x.location + " " + x.time)
                client.send(Message(text=message), thread_id=group_id, thread_type=ThreadType.GROUP)
