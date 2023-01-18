from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"],i["answer"]))

sample = QuizBrain(question_bank)
while sample.still_has_question():
    score=sample.next_question()
print("alright you have completed the challenge")
print(f"your final score is {score}/{len(question_bank)}")
