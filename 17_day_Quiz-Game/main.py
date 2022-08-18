from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for item in question_data:
    new_question=Question(item['text'],item['answer'])
    # print(obj.text)
    # print(obj.answer)
    question_bank.append(new_question)

# print(question_bank[10].text)

quiz=QuizBrain(question_bank)

while quiz.still_has_quistions():
    quiz.next_question()

print('You have completed the quiz')
print(f"Your final score is {quiz.score}/{quiz.question_number}")
