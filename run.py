from brute_force import brute_force
from genetic import algorithm


def run():

    text = input("What text would you like to try and solve (suggest to start small)?\n")
    text = text.lower()

    run_brute_force = input("Do you want to run the brute force as a bench mark (can be very slow)? (Y/N)\n")

    if run_brute_force.upper() == "Y":

        force = brute_force.BruteForce(text)
        brute_force_result = force.start()

    gen = algorithm.Algorithm(text, 100)
    gen_result = gen.start()

    if run_brute_force.upper() == "Y":

        if gen_result[0] < brute_force_result[0]:
            print(
                "Genetic algorithm evaluated fewer options - {0} vs {1} options.".format(gen_result[0], brute_force_result[0])
            )
        elif gen_result[0] > brute_force_result[0]:
            print(
                "Brute force evaluated fewer options - {0} vs {1} options.".format(brute_force_result[0], gen_result[0])
            )
        else:
            print(
                "It was a draw, both evaluated {0} options.".format(brute_force_result[0])
            )

        if gen_result[1] < brute_force_result[1]:
            print(
                "Genetic algorithm was faster - {0} vs {1}.".format(gen_result[1], brute_force_result[1])
            )
        elif gen_result[1] > brute_force_result[1]:
            print(
                "Brute force was faster - {0} vs {1}.".format(brute_force_result[1], gen_result[1])
            )
        else:
            print(
                "It was a draw, both finished in {0}.".format(brute_force_result[1])
            )

    print("Done...")


if __name__ == "__main__":
    run()
