class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        if self.question_number >= len(self.question_list):
            return False
        return True

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        ans = input(f"Q.{self.question_number}:{current_question}(True/False)")
        self.check_answer(correct_answer,ans)
        return self.score

    def check_answer(self,correct_answer,user_answer):
        if correct_answer.lower()==user_answer.lower():
            self.score+=1
            print(f"That's right! your current score: {self.score}/{self.question_number}")
        else:
            print(f"Oh thats wrong! give another try.your current score: {self.score}/{self.question_number}")