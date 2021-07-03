from random import randint, choice
from time import sleep

from .gen import God, Question, Choice


questions = [
    Question("Would be a force of Evil or of Good?",
             [Choice("I dont like either", 1),
              Choice("I like good", 2),
              Choice("I like Evil!", 2)]),
    Question("Would be a force of Evil or of Good?",
             [Choice("I dont like either", 1),
              Choice("I like good", 2),
              Choice("I like Evil!", 2)]),
]


def create(name, power):
    g = God(
        name=name,
        power=power
    )
    return g


def run():
    name = input("Enter your god name: ")
    print("Computing god: ", end="")

    power = 0
    potential = len(questions)


    while potential > 0:
        sleep(1)
        q = choice(questions)
        questions.pop(questions.index(q))
        print(f"Q: {q.text}\n\tChoices:")
        for i, c in enumerate(q.choices):
            print(f"\t {i}: {c.text}")

        chosen = int(input(f"Your choice, {name}? "))
        power += q.choices[chosen].value
        potential -= 1

        #print("#", end="", flush=True)


    print("OK !")

    print(create(name, power))
