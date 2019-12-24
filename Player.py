class Player(object):
    def __init__(self, name, timesPaid):
        self.name = name
        self.timesPaid = timesPaid

    def get_name(self):
        return self.name

    def get_times_paid(self):
        return self.timesPaid
