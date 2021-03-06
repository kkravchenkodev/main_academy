"""
Задача:
Выводить пользовалю по одному вопросу с вариантами ответов.
Просить пользователя ввести его вариант ответа.
Показать пользователю - правильно или нет.
Записать результат в файл. (пример в answers.txt)
"""


class Task:
    def __init__(self, question='', option1='', option2='', option3='', answer=''):
        self.__question = question
        self.__option1 = option1
        self.__option2 = option2
        self.__option3 = option3
        self.__answer = answer

    def set_question(self, question):
        self.__question = question

    def get_question(self):
        return self.__question

    def set_option1(self, option1):
        self.__option1 = option1

    def set_option2(self, option2):
        self.__option2 = option2

    def set_option3(self, option3):
        self.__option3 = option3

    def set_answer(self, answer):
        self.__answer = answer

    def get_answer(self):
        return self.__answer

    def __repr__(self):
        return f"\n{self.__question}{self.__option1}{self.__option2}{self.__option3}"


def get_exam():
    correct = 0
    questions = []
    with open('questions', 'r', encoding='UTF-8') as questions_file:
        text = questions_file.readlines()
        for i, line in enumerate(text):
            if i % 5 == 0:
                task = Task()
            if i in [*range(0, 50, 5)]:
                task.set_question(line)
            elif i in [*range(1, 50, 5)]:
                task.set_option1(line)
            elif i in [*range(2, 50, 5)]:
                task.set_option2(line)
            elif i in [*range(3, 50, 5)]:
                task.set_option3(line)
            elif i in [*range(4, 50, 5)]:
                task.set_answer(int(line.replace("Answer: ", "")))
            if i % 5 == 0:
                questions.append(task)

    with open('answers', 'w', encoding='UTF-8') as answers_file:
        answer = None
        for q in questions:
            print(q)
            answers_file.write(q.get_question())
            try:
                answer = int(input('Enter your answer:\n>>'))
            except ValueError as e:
                print(e)
                print("Entered answer in not an Integer")
                answers_file.write("Entered answer in not an Integer\n")
            if answer == q.get_answer():
                correct += 1
                print(f"Answer {{{answer}}} is CORRECT")
                answers_file.write(f"Answer {{{answer}}} is CORRECT\n\n")

            else:
                print(f"Answer {{{answer}}} is WRONG")
                print(f"Correct answer is - {q.get_answer()}")
                answers_file.write(f"Answer {{{answer}}} is WRONG\n\n")
        print(f'\nAmount of correct answers is {{{correct}}} from 10')
        print(f"Percent is {correct * 10}%")


if __name__ == '__main__':
    get_exam()
