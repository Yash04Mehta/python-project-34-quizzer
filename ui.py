THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, statement: QuizBrain):
        self.quiz = statement
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_lb = Label(text="Score :0", bg=THEME_COLOR, fg="white")
        self.score_lb.grid(row=0, column=1)

        self.canvas = Canvas(bg="white" , width=300 , height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, bg=THEME_COLOR, command=self.pass_true)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, bg=THEME_COLOR, command=self.pass_false)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def pass_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pass_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_lb.config(text=f"Score : {self.quiz.score}")

        self.window.after(1000, self.get_next_question)
