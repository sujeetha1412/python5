class InvalidoptionError(Exception):
    pass
class quiz:
    def __init__(self):
        self.questions = [
            "1. Largest planet?\nA. Earth\nB. Mars\nC. Jupiter",
            "2. 5+3=?\nA. 6\nB. 8\nC. 10",
            "3. Largest ocean?\nA. Atlantic\nB. Indian\nC. Pacific",
            "4. 10/2=?\nA. 2\nB. 5\nC. 10",
            "5. Water Formula?\nA. CO2\nB. H2O\nC. O2",
            "6. 9*2=?\nA. 18\nB. 16\nC. 20",
            "7. 3*3=?\nA. 6\nB. 9\nC. 12",
            "8. Square of 5?\nA. 10\nB. 25\nC. 20"
        ]
        # Added quotes to answers
        self.answers = ['C', 'B', 'C', 'B', 'B', 'A', 'B', 'B']
        self.score = 0
    def start_quiz(self):
        for i in range(len(self.questions)):
            while True:
                try:
                    print("\n" + self.questions[i])
                    user_ans = input("Enter option(A/B/C): ").upper()
                    if user_ans not in ['A', 'B', 'C']:
                        raise InvalidoptionError
                    if user_ans == self.answers[i]:
                        print("Correct!")
                        self.score += 1
                    else:
                        print("Incorrect!")
                    break
                except InvalidoptionError:
                    print("Invalid option! Please enter A, B, or C.")
    def display_score(self):
        print("\nFinal score:", self.score, "/", len(self.questions))
obj= quiz()
obj.start_quiz()
obj.display_score()
