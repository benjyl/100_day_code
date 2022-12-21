class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q{self.question_number}: {current_question.text} (True/False)?"
        )
        actual_answer = current_question.answer
        self.check_answer(user_answer, actual_answer)

    def check_answer(self, user_ans, act_ans):
        if user_ans.lower() == act_ans.lower():
            print("Correct answer")
            self.user_score += 1
        else:
            print("Wrong answer")
        print(f"The correct answer was: {act_ans}")
        print(f"Your current score is: {self.user_score}/{self.question_number}\n")
