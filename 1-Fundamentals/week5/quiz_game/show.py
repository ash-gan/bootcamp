
import re


class Show:

    def print(self, question_data):
        print(question_data.question)
        i = 1
        for option in question_data.options:
            print(i, ") ", option)
            i += 1

    def show_message(self, result, question_data):
        if result:
            print("You are on a roll, keep going!!!")
        else:
            print("the correct answer is ", question_data.answer)
