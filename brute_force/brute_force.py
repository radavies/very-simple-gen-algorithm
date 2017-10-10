import datetime

from util import util


class BruteForce:

    def __init__(self, text):
        self.text = text
        self.start_time = datetime.datetime.utcnow()
        self.options_tried = 0
        self.run_time = None

    def start(self):
        print("Trying brute force to solve for {0}".format(self.text))
        solved = False

        while not solved:
            generated_text = util.create_text(len(self.text))

            print("Generated text: {0}".format(generated_text))

            self.options_tried = self.options_tried + 1
            solved = self.evaluate(generated_text)

        return self.options_tried, self.run_time

    def evaluate(self, created_text):
        if created_text == self.text:
            end_time = datetime.datetime.utcnow()
            self.run_time = end_time - self.start_time
            print("Text match found in {0}".format(self.run_time))
            print("Options tried {0}".format(self.options_tried))
            return True
        else:
            return False


