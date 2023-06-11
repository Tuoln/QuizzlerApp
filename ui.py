import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuestionInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.title("Quiz Game")

        self.score_label = tkinter.Label(text="score: 0", bg=THEME_COLOR, fg="white", pady=20, font=("Arial", 12))
        self.score_label.grid(row=0, column=2)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=1, columnspan=2)
        self.question_text = self.canvas.create_text(150, 125, text="Question text", font=("Arial", 20, "italic")
                                                     , width=280)

        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(text="✔", image=true_image, width=80, height=80,
                                          command=self.true_pressed, bd=0)
        self.true_button.grid(row=2, column=1, pady=20)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(text="❌", image=false_image, width=80, height=80,
                                           command=self.false_pressed, bd=0)
        self.false_button.grid(row=2, column=2, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of the exam!")
            self.true_button["state"] = "disabled"
            self.false_button["state"] = "disabled"


    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)







