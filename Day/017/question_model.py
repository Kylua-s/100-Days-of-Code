class Question:

    def __init__(self, text, answer):
        global question_number
        question_number += 1
        self.q_number = question_number
        self.text = text
        self.answer = answer


question_number = 0
