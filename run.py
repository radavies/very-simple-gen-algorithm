from brute_force import brute_force
from genetic import algorithm


def run():

    text = input("What text would you like to try and solve?\n")
    text = text.lower()

    force = brute_force.BruteForce(text)
    brute_force_result = force.start()

    gen = algorithm.Algorithm(text)
    gen_result = gen.start()

    print("Done...")


if __name__ == "__main__":
    run()
