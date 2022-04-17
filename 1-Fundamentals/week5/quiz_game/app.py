from quiz import Quiz
from question_model import Question
from quiz_data import GetData
from show import Show
from user import User

# get_question_data
question_data = GetData().get_csv_data()
questions_list = []
for question in question_data:
    questions_list.append(Question(
        question['question'], question['options'], question['answer']))

# initialize quiz game
quiz = Quiz(questions_list=questions_list)

# get user login details
player = User()
player_name = input("Enter your user name:")
player_password = input("Enter your password:")

authoried_user = False

if player.login(player_name, player_password) == "invalid password":
    print("Please check your password.")
elif player.login(player_name, player_password) == "user not found":
    register = player.register(player_name, player_password)
    if register:
        authoried_user = True
else:
    authoried_user = True

if authoried_user == True:
    while quiz.still_has_question():
        question = quiz.get_question_data()
        Show().print(question)
        user_answer = input(
            "Enter your answer choice 1, 2, 3 or 4, enter 'X' to save and exit: ")
        if user_answer.lower() == 'x':
            player.update_user_game()
            print("Thank you for Playing, you can resume when you come back! Good day!")
            break
        result = quiz.check_answer(int(user_answer))
        Show().show_message(result, question)
    print("Your total score is: ", quiz.score)
