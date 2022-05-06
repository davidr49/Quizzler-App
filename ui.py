from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='ADD QUESTIONS HERE', font=('arial', 0, 'italic'),
                                                     width=280,
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text=f'Score:', font=('arial', 10, 'bold'), bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)

        self.check_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=self.check_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.cross_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=self.cross_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
