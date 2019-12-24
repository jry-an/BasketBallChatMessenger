import requests
import lxml.html as lh
from Game import Game


class FoxDataService:
    def get_games(self):

        print("enter team url")
        url = input()
        page = requests.get(url)
        # Store the contents of the website under doc
        doc = lh.fromstring(page.content)  # Parse data that are stored between <tr>..</tr> of HTML
        tr_elements = doc.xpath('//tr')

        # Create empty list
        game_list = []
        col = []
        i = 0  # For each row, store each first element (header) and an empty list
        for t in tr_elements[0]:
            i += 1
            text = t.text_content()
            col.append((text, []))

        for j in range(1, len(tr_elements)):
            # T is our j'th row
            T = tr_elements[j]

            # i is the index of our column
            i = 0
            date = ""
            time = ""
            location = ""

            # Iterate through each element of the row
            for t in T.iterchildren():
                data = t.text_content()
                if not data == 'View':
                    # Append the data to the empty list of the i'th column
                    col[i][1].append(data)
                    if i == 1:
                        date = data
                    if i == 2:
                        time = data
                    if i == 3:
                        location = data
                    # Increment i for the next column
                    i += 1
            new_game = Game(date, time, location)
            game_list.append(new_game)
        return game_list
