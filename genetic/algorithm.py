import datetime, random

from genetic import organism
from util import util


class Algorithm:

    def __init__(self, text, population_size):
        self.text = text
        self.population_size = population_size
        self.population = []
        self.start_time = datetime.datetime.utcnow()
        self.generations = 1
        self.run_time = None

    def start(self):
        print("Trying genetic algorithm to solve for {0}".format(self.text))

        print("Generating initial population")
        self.generate_initial_population()
        self.print_population()

        solved = self.evaluate()

        while not solved:
            print("Starting generation {0}".format(self.generations))
            self.fitness_function()
            self.generate_new_generation()
            self.print_population()

            if self.evaluate():
                solved = True
            else:
                self.generations = self.generations + 1

        return (self.generations * self.population_size), self.run_time

    def generate_initial_population(self):
        for counter in range(0, self.population_size):
            new_text = util.create_text(len(self.text))
            self.population.append(organism.Organism(new_text))

    def generate_new_generation(self):
        self.population.sort(key=lambda item: item.fitness, reverse=True)

        print("Last generation highest fitness {0}".format(self.population[0].fitness))

        to_reproduce = self.population[0:int(len(self.population) / 2)]

        self.population = []

        for counter in range(0, self.population_size):
            index_one = random.randint(0, len(to_reproduce) - 1)
            index_two = random.randint(0, len(to_reproduce) - 1)

            while index_one == index_two:
                index_two = random.randint(0, len(to_reproduce) - 1)

            new_organism = self.reproduce(to_reproduce[index_one], to_reproduce[index_two])

            self.population.append(new_organism)

    def reproduce(self, parent_one, parent_two):
        new_text = []
        for counter in range(0, len(self.text)):
            rand = random.randint(0, 100)

            if rand <= 45:
                # use parent_one
                new_text.append(parent_one.text[counter])
            elif 45 < rand <= 90:
                # use parent_two
                new_text.append(parent_two.text[counter])
            else:
                # mutate
                new_text.append(util.get_random_char())

        return organism.Organism("".join(new_text))

    def evaluate(self):
        for item in self.population:
            if item.text == self.text:
                end_time = datetime.datetime.utcnow()
                self.run_time = end_time - self.start_time
                print("Text match found in {0}".format(self.run_time))
                print("Match found in {0} generations".format(self.generations))
                print("Total options tried {0}".format(self.generations * self.population_size))
                print(item.text)
                return True
        return False

    def fitness_function(self):
        for item in self.population:
            score = 0
            for counter in range(0, len(self.text)):
                if item.text[counter] == self.text[counter]:
                    score = score + 1

            item.fitness = score

    def print_population(self):
        print(", ".join([item.text for item in self.population]))
