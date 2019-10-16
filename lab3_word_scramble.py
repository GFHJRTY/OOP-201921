# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        self.user_input1= input('Please give me another sentence: ')

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word

        new = self.user_input.replace('l', 'e', 1)

        new = new.replace('e', 'l', 1)

        print('The sentence user input was: ' + new)

        # reverse two indices

        print('The reversed string is :',self.user_input[::-1])

        print('The reversed string is :', self.user_input1[::-1])

        # particularly good to use is to switch the first two

        list1 = self.user_input.split()

        temp = list1[0]
        list1[0] = list1[1]
        list1[1] = temp

        print(list1)


        # and the last two

        d = len(list1)

        temp = list1[d - 2]
        list1[d - 2] = list1[d - 1]
        list1[d - 1] = temp

        print(list1)


        # this only makes sense if you have a world that is longer than 3
        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation
        array = self.user_input.split()
        temp = array[1]
        array[1] = array[2]
        array[2] = temp
        string = ' '.join(array)
        print(string)


word_scrambler = WordScramble()
word_scrambler.scramble()

