import datetime


class Algorithm:

    def __init__(self, text):
        self.text = text
        self.start_time = datetime.datetime.utcnow()
        self.options_tried = 0
        self.run_time = None

    def start(self):
        print("Trying genetic algorithm to solve for {0}".format(self.text))
        solved = False
