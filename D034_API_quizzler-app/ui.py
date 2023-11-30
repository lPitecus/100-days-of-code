from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

#TODO: Descobrir como adicionar mais de uma janela no tkinter
#TODO: Fazer com que o usuário escolha a quantidade de perguntas e a categoria


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain  # atributo que permite usar tudo de um objeto da classe QuizBrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # label
        self.questions_label = Label(
            text=f"Question {self.quiz.question_number + 1}/{len(self.quiz.question_list)}",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 15, "bold")
        )
        self.questions_label.grid(row=0, column=0, columnspan=2)
        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="test",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(
            image=true_image,
            bd=0,
            highlightthickness=0,
            activebackground=THEME_COLOR,
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(
            image=false_image,
            bd=0,
            highlightthickness=0,
            activebackground=THEME_COLOR,
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
            self.questions_label.config(text=f"Question {self.quiz.question_number}/{len(self.quiz.question_list)}")

        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz Completed!\nFinal Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.get_next_question)

        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.get_next_question)
