# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 10-10-2019
# purpose: Lab 4

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html(self.my_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        # your code goes here!
        fo.write('<span style="font-size: 10px"> HELLO </span>')

        fo.write('</div>\
            </body>\
            </html>')

    def create_dict(self):
        count = 0
        my_dict = {}
        my_dict1 = {'name0': 'Eghan', 'name3': 'Adam', 'name4': 'Jack'}
        word = input('Please input a word to add to the dictionary :')
        my_dict['property1'] = word
        print(my_dict)
        for k, v in my_dict1.items():
            my_dict[k] = v
        print(my_dict)
        string = str(my_dict)
        print(string)
        key = input('Please input key to search :')

        if key in string:
            count += 1
        else:
            count = 0
        print('The number of occurrences of the keyword is ' + str(count))

        print(eval(string), end='dictionary\n')
        # your code goes here:
        return my_dict

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary


wc = WordCloud()