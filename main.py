from data import question_data
from question_model import Question 
from quiz_brain import QuizBrain

#list with all questions
question_bank = [] 

for q in question_data:
  q_answer =q["answer"]
  q_text = q["text"]
  new_question = Question(q_text, q_answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
	quiz.next_question()

print("You have completed the quiz.") 
print(f"Your final score was {quiz.score}/{quiz.question_number}")



