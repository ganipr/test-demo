def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B, C, or D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_ans(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)


def check_ans(answer, guess):
    if answer == guess:
        print("Correct!!")
        return 1
    else:
        print("Wrong!!")
        return 0


def display_score(correct_guesses, guesses):
    print("---------------------")
    print("Results")
    print("---------------------")
    print("Answers: ", end='')
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    print("---------------------")
    print(f"Total score is: {(correct_guesses/len(guesses)) * 100}%")


def play_again():
    response = input("Do you want to play again?:(Yes or No):")
    response = response.upper()
    if response == 'YES':
        return True
    else:
        return False


questions = {"Who manufactures Lifebuoy?:": "A",
             "Who is the founder of apple?:": "B",
             "Which is the most valued Indian company?:": "C",
             "Who is the richest man in the World?:": "D"}

options = [["A. HUL", "B. Dabur", "C. ITC", "D. AWL"], ["A. Jeff B", "B. Steve Jobs", "C. Elon Musk", "D. Larry Page"],
            ["A. Infosys", "B. Adani", "C. RELIANCE", "D. TCS"], ["A. Jeff B", "B. Ambani", "C. Jack Ma", "D. Elon Musk"]]

new_game()
while play_again():
    new_game()
print("Have a great day")
