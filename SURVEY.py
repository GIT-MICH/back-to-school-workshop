class SingleChoiceQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def ask(self):
        print(self.question)
        numbered_answers = [
            chr(97 + i) + ") " + a
            # f"{chr(97 + i)}) {a}"
            for i, a in enumerate(self.answers)
        ]
        print("\n".join(numbered_answers))
        while True:
            answer = input("Odpowiedź: ")
            if (
                    len(answer) == 1
                    and 97 <= ord(answer[0]) < 97 + len(self.answers)
            ):
                print("Dziękujemy! \n")
                return answer
            else:
                print('Brak takiej odpowiedzi. Wprowadź ponownie!')


class Questionnaire:
    def __init__(self, title):
        self.title = title
        self.qlist = []

    def add_question(self, q):
        self.qlist.append(q)

    def run(self):
        print(self.title)
        return [
            question.ask()
            for question in self.qlist
        ]


if __name__ == "__main__":
    questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa.')
    q1 = SingleChoiceQuestion('Matryca', ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali'])
    q2 = SingleChoiceQuestion('Rodzaj ekranu', ['matowy', 'błyszczący'])
    q3 = SingleChoiceQuestion('Czy polecisz go znajomemu?', ['zdecydowanie tak', 'raczej tak', 'nie mam zdania',
                                                             'raczej nie', 'zdecydowanie nie']
                              )
    questionnaire.add_question(q1)
    questionnaire.add_question(q2)
    questionnaire.add_question(q3)
    q_answers = questionnaire.run()

    print(q_answers)