import datetime

from genetic import organism
from util import util


class Algorithm:

    def __init__(self, text, population_size, mutation_rate):
        self.text = text
        self.population_size = population_size
        self.population = []
        self.mutation_rate = mutation_rate
        self.start_time = datetime.datetime.utcnow()
        self.generations = 0
        self.run_time = None

    def start(self):
        print("Trying genetic algorithm to solve for {0}".format(self.text))

        self.generate_initial_population()

        solved = False
        while not solved:
            if self.evaluate():
                solved = True
            else:
                self.fitness_function()
                self.generate_new_generation()
                self.generations = self.generations + 1

    def generate_initial_population(self):
        for counter in range(0, self.population_size):
            new_text = util.create_text(len(self.text))
            self.population.append(organism.Organism(new_text))

    def generate_new_generation(self):
        # TODO: make this work
        return self.population

    def evaluate(self):
        for item in self.population:
            if item.text == self.text:
                end_time = datetime.datetime.utcnow()
                self.run_time = end_time - self.start_time
                print("Text match found in {0}".format(self.run_time))
                print("Match found in {0} generations".format(self.generations))
                print("Total options tried {0}".format(self.generations * self.population_size))
                return True
        return False

    def fitness_function(self):
        for item in self.population:
            score = 0
            for counter in range(0, len(self.text)):
                if item.text[counter] == self.text[counter]:
                    score = score + 1

            item.fitness = score
