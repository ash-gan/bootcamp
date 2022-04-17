class Quiz:

    def __init__(self, questions_list) -> None:
        self.questions = questions_list
        self.score = 0
        self.options = []
        self.next_question = None
        self.questions_number = 0

    def still_has_question(self):
        return self.questions_number < len(self.questions)

    def get_question_data(self):
        self.next_question = self.questions[self.questions_number]
        self.questions_number += 1
        return self.next_question

    def check_answer(self, answer):
        if self.next_question.options[answer-1].lower() == self.next_question.answer.lower():
            self.score += 10
            return True
        else:
            self.score -= 10
            return False
