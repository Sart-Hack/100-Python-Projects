from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question_entry["text"], question_entry["answer"]) for question_entry in question_data]

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    answer = quiz.next_question()

print(f"You\'ve Completed the quiz. \n"
      f"Your final score is {quiz.score}/12")
