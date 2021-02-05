from random import random, sample
from random import seed
from random import randint
from random import choice


def input2():
    test = [1, 2, 3, 4, 5, 6]
    return test


def generate():
    sequence = [i for i in range(1, 53)]
    # print(sequence)
    # make choices from the sequence
    for _ in range(1):
        # selection = choice(sequence)
        selection = sorted(sample(sequence, 6))
        # sorted(sequence)
        # print((selection))
        return selection


def compare(user_input, generated_output):
    for i in range(len(user_input)):
        cc:list [i] = user_input[i] - generated_output[i]
    print(cc)
    return cc


def output():
    pass


def main():
    print(generate())
    print(input2())
    print(compare(input2(), generate()))


if __name__ == "__main__":
    main()
