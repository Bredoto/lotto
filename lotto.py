from random import random, sample
from random import seed
from random import randint
from random import choice


def input():
    test = [4, 8, 15, 16, 23, 42]
    return test


def generate():
    sequence = [i for i in range(1, 53)]
    # print(sequence)
    # make choices from the sequence
    selection = list(sorted(sample(sequence, 6)))
    print(selection)
    # selection = [1,2,11,12,13,14]
    return selection


def compare(user_input, generated_output):
    counter = 0
    for i in range(0, 6):
        for j in range(0, 6):
            if user_input[i] == generated_output[j]:
                counter = counter + 1
    return counter



def main():
    print(input())
    counter = 0
    while 1:
        counter = counter + 1
        if compare(input(), generate()) >= 5:
            break
        print(counter)



if __name__ == "__main__":
    main()
