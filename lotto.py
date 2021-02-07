from random import random, sample
from random import seed
from random import randint
from random import choice


def input2():
    test = [1, 2, 3, 4, 5, 6]
    return test

def input3():
    #test = [1, 2, 31, 41, 45, 34]
    test = [10, 20, 23, 45, 47, 48]
    return test

def generate2():
    sequence = [i for i in range(1, 53)]
    # print(sequence)
    # make choices from the sequence
    selection = list(sorted(sample(sequence, 6)))
    print(selection)
    #selection = [1,2,11,12,13,14]
    return selection


def compare(user_input, generated_output):
    counter = 0
    for i in range(0,6):
        for j in range(0,6):
            #print(i, j, user_input[i], generated_output[j])
            if user_input[i] == generated_output[j]:
                #print(i, j, user_input[i],generated_output[j] )
                counter = counter + 1
    return counter


def output():
    pass


def main():
    print(input2())
    #print(input3())
    print(compare(input2(), generate2()))
    #print(compare(input2(), input3()))


if __name__ == "__main__":
    main()
