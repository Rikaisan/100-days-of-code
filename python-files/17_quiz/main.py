import json
from colorize import colorize

# ----------------------------------------------------------------------------------------------------
with open("data.json") as file:
    questions = json.load(file)
# ----------------------------------------------------------------------------------------------------


class Question:
    def __init__(self, question_dict, question_index):
        self.text = question_dict.get("text")
        self.answer = question_dict.get("answer")
        self.number = question_index

    def check_answer(self, answer):
        answer = answer
        if answer == self.answer:
            return True
        return False

    def ask(self):
        print(colorize(f"[{self.number}]", "magenta"), self.text)
        while True:
            answer = input().lower().strip()
            if answer:
                if answer[0] == 't':
                    answer = 'True'
                    break
                elif answer[0] == 'f':
                    answer = 'False'
                    break
            print(colorize("Invalid answer, use True or False!", "red"))
        if self.check_answer(answer):
            print(colorize("Correct!", "green"))
            return True
        print(colorize("Incorrect!", "red"))
        return False


# ----------------------------------------------------------------------------------------------------
score = 0
total = len(questions)
question_number = 1
print(colorize("\nWelcome to your True or False quiz!", "magenta"))
for question in questions:
    current_question = Question(question, question_number)
    question_number += 1
    print(colorize(f"Score: {score}/{total}", "yellow"))
    if current_question.ask():
        score += 1

print(f"Thank you for playing! Your final score is: {colorize(f'{score}/{total}','cyan')}")
