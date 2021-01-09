class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"\nQ.{self.question_number}: {current_question.text} (True/False): ")
        if answer.lower() in ["true", "false", "t", "f"]: # user validation
            self.check_answer(answer, current_question.answer)
        else:
            print("Wrong input try again")
            self.question_number -= 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() in correct_answer:
            print("You got it right")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"The correct answer was: {correct_answer[0].title()}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
