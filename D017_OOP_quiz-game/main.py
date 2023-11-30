import html

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    # criando um objeto a partir da classe Question() a cada item da lista de dados.
    new_question_object = Question(html.unescape(item["question"]), (item["correct_answer"]))
    question_bank.append(new_question_object)

quiz = QuizBrain(question_bank)

while quiz.should_continue():
    quiz.next_question()


print(f"You've completed the game with {quiz.score} right questions"
      f" from a total of {len(quiz.question_list)} questions!")



