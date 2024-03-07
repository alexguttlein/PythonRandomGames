class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = ""
        while answer != "true" and answer != "false":
            answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
            answer = answer.lower()
        self.check_answer(answer, current_question.answer)
        self.question_number += 1
    
    def still_has_questions(self):
        '''if(len(self.question_list) > self.question_number):
            return True
        return False'''
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer:
            print("CORRECT!!!")
            self.score += 1
        else:
            print("INCORRECT!!!")