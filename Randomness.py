class Randomness:
    def __init__(self):
        # Initialises all of the possible trigrams
        self.data_dict = {"000": "0,0",
                    "001": "0,0",
                    "010": "0,0",
                    "011": "0,0",
                    "100": "0,0",
                    "101": "0,0",
                    "110": "0,0",
                    "111": "0,0"}
        self.points = 50  # Starting points for the game
        self.data = self.user_data()
        self.create_trigrams(self.data)
        self.game()


    def user_data(self):
        input_data = ""
        print("Please provide the computer with some data... ")
        # Takes in at least 100 digits of user's data in order to form the trigrams
        while len(input_data) < 100:
            print(f"The current data length is {len(input_data)}, {100 - len(input_data)} symbols left.")
            user_input = input("Print a random string containing 0 or 1:\n")
            for number in user_input:
                # Ensures data is valid
                if number in "10":
                    input_data += number
        print(f"\nFinal data string:\n{input_data}\n")
        return input_data


    def create_trigrams(self, user_string):
        # Creates the trigrams for the frequency analysis at initialisation and when called later updates trigrams with new data
        for i in range(len(user_string) - 3):
            three_letters = f"{user_string[i]}{user_string[i + 1]}{user_string[i + 2]}"
            values = self.data_dict[three_letters]
            if user_string[i + 3] == "0":
                self.data_dict[three_letters] = f"{int(values.split(',')[0]) + 1}, {values.split(',')[-1]}".replace(" ", "")
            if user_string[i + 3] == "1":
                self.data_dict[three_letters] = f"{values.split(',')[0]}, {int(values.split(',')[-1]) + 1}".replace(" ", "")


    def game(self):
        print("""You have 50 points.
Every time the system successfully predicts your next press, you lose 1 point.
Every time the system unsuccessfully predicts your next press, you earn 1 point.
Your input needs to be at least four characters as the computer will predict every character chosen after the first three. 
Print 'exit' to leave the game.""")

        while True:
            while True:
                # Starts the game and does input sanitation
                prediction = ""
                flag = True
                test_string = input("\nPrint a random string containing 0 or 1:\n")
                if test_string == "exit":
                    print(f"\nGame over! You finished with {self.points} points.")
                    exit()
                elif len(test_string) >= 4:
                    for x in test_string:
                        if x not in "10":
                            flag = False
                            continue
                    if flag:
                        break
            # Creates a prediction
            for i in range(len(test_string) - 3):
                testing_triad = f"{test_string[i]}{test_string[i + 1]}{test_string[i + 2]}"
                value_1 = int(self.data_dict[testing_triad].split(',')[0])
                value_2 = int(self.data_dict[testing_triad].split(',')[-1])
                if value_1 > value_2:
                    prediction += "0"
                else:
                    prediction += "1"
            self.play_round(test_string, prediction)
    
    def update_score(self, user_string, prediction):
        # Calculate score based on how accurate the prediction is
        score = 0
        OFFSET = 3
        for index in range(len(prediction)):
            if prediction[index] == user_string[index + OFFSET]:
                score += 1
        return score


    def play_round(self, user_string, prediction):
        score = self.update_score(user_string, prediction)  # Keeps score
        print(f"Predictions:\n{prediction}\n")
        print(f"Computer guessed {score} out of {len(prediction)} symbols right ({round(score / len(prediction) * 100, 2)}%)")
        self.points += len(prediction) - 2 * score  # If the score of the computer is less than half of the prediction, the user gains points
        self.create_trigrams(user_string)
        # Checks if points reach 0
        if self.points <= 0:
            print("Game over! You ran out of points.")
            exit()
        print(f"You now have {self.points} points!")

def main():
    Randomness()


if __name__ == "__main__":
    main()