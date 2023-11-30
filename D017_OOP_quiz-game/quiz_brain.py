class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)?: ").lower()
        if answer == "f":
            answer = "false"
        elif answer == "t":
            answer = "true"
        if self.check_answer(answer):
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        self.question_number += 1
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    def check_answer(self, answer):
        current_answer = (self.question_list[self.question_number]).answer
        return answer == current_answer.lower()

    def should_continue(self):
        return self.question_number < len(self.question_list)
