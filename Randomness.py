data = ""
data_dict = {"000": "0,0",
             "001": "0,0",
             "010": "0,0",
             "011": "0,0",
             "100": "0,0",
             "101": "0,0",
             "110": "0,0",
             "111": "0,0"}
balance = 50
print("Please provide the computer with some data... ")
while len(data) < 100:
    print(f"The current data length is {len(data)}, {100 - len(data)} symbols left.")
    user_input = input("Print a random string containing 0 or 1:\n")
    for x in user_input:
        if x in "10":
            data += x

print(f"\nFinal data string:\n{data}\n")
options = ["000", "001", "010", "011", "100", "101", "110", "111"]
for i in range(len(data) - 3):
    three_letters = f"{data[i]}{data[i + 1]}{data[i + 2]}"
    values = data_dict[three_letters]
    if data[i + 3] == "0":
        data_dict[three_letters] = f"{int(values.split(',')[0]) + 1}, {values.split(',')[-1]}".replace(" ", "")
    if data[i + 3] == "1":
        data_dict[three_letters] = f"{values.split(',')[0]}, {int(values.split(',')[-1]) + 1}".replace(" ", "")
    three_letters = ""

print("You have 50 points. Every time the system successfully predicts your next press, you lose 1 point.\nOtherwise, you earn 1 point. Print 'exit' to leave the game. ")

while True:
    while True:
        score = 0
        prediction = ""
        flag = True
        test_string = input("\nPrint a random string containing 0 or 1:\n")
        if test_string == "exit":
            print(f"\nGame over! You finished with {balance} points.")
            exit()
        elif len(test_string) >= 4:
            for x in test_string:
                if x not in "10":
                    flag = False
                    continue
            if flag:
                break
    for i in range(len(test_string) - 3):
        testing_triad = f"{test_string[i]}{test_string[i + 1]}{test_string[i + 2]}"
        value_1 = int(data_dict[testing_triad].split(',')[0])
        value_2 = int(data_dict[testing_triad].split(',')[-1])
        if value_1 > value_2:
            prediction += "0"
        else:
            prediction += "1"
    print(f"predictions:\n{prediction}\n")
    for i in range(len(prediction)):
        if prediction[i] == test_string[i + 3]:
            score += 1
    print(f"Computer guessed {score} out of {len(prediction)} symbols right ({round(score / len(prediction) * 100, 2)}%)")
    balance += len(prediction) - score
    balance -= score
    if balance <= 0:
        print("Game over! You ran out of points.")
        exit()
    print(f"You now have {balance} points!")
