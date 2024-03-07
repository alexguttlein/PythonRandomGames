from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def cargar_preguntas():
    question_bank = []
    '''for i in range(len(question_data)):
        txt = (question_data[i].get("text"))
        ans = (question_data[i].get("answer"))
        question = Question(txt, ans)
        question_bank.append(question)'''
    for quest in question_data:
        question_text = quest["text"]
        question_answer = quest["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank



question_bank = cargar_preguntas()
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"TOTAL SCORE: {quiz_brain.score}/{len(quiz_brain.question_list)}")