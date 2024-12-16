import random
import customtkinter as ctk
from constants import *

answered_questions = []

score = 0
def new_question():
    global question_and_answer
    question_and_answer = random.choice(QUESTIONS)
    return question_and_answer

def delete_question(question_with_answer):
    QUESTIONS.remove(question_with_answer)





def show_qustions():
    global question_and_answer
    if len(QUESTIONS) > 0:
        question = new_question()["question"]
        question_label.configure(text=question)
    else:
        end_game()



def check_answer(user_answer):
    global score, question_and_answer
    answer = question_and_answer["answer"]

    if user_answer == answer:
        score += 1
    # if question_and_answer not in bin_of_questions:
    answered_questions.append(question_and_answer)
    delete_question(question_and_answer)
    show_qustions()
    
    
def answer_yes():
    check_answer("yes")


def answer_no():
     check_answer("no")



def end_game():
    global score
    question_label.configure(text= f"Game Over!\n Your score: {score}/{len(answered_questions)}")
    yes_button.pack_forget()
    no_button.pack_forget()
    play_again_button.pack(pady=20)

def play_again():
    global score, QUESTIONS, answered_questions
    score = 0
    answered_questions = []
    QUESTIONS = RAW_QUESTIONS.copy()
    play_again_button.pack_forget()
    yes_button.pack(side="right", padx=50, pady=10)
    no_button.pack(side="left", padx=50, pady=10)
    show_qustions()

game_screen = ctk.CTk()
game_screen.title("Trivia Master")
game_screen.geometry("450x250")

game_title_lable = ctk.CTkLabel(game_screen, text="Trivia Master", font=("monospaced", 30))
game_title_lable.pack(pady= 20)


question_label = ctk.CTkLabel(game_screen, text="", font=("monospaced", 18), wraplength=350)
question_label.pack(pady=20)



yes_button = ctk.CTkButton(game_screen, text="yes", hover=True, command=answer_yes )
yes_button.pack(side="right", padx=50, pady=10)

no_button = ctk.CTkButton(game_screen, text="no", hover=True, command=answer_no )
no_button.pack(side="left", padx=50, pady=10)

play_again_button = ctk.CTkButton(game_screen, text="Play Again", command=play_again)
play_again_button.pack()
play_again_button.pack_forget()

show_qustions()
game_screen.mainloop()