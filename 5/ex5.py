def ex_5_1_park():
    age = int(input("enter your age: "))
    if age >= 12:
        print("you can enter the park")
    else:
        print("you can't enter the park")

def ex_5_2_park():
    age = int(input("enter your age: "))
    height = int(input("enter your height: "))
    if age >= 12 and age <= 100 and height >= 130:
        print("you can enter the park")
    else:
        print("you can't enter the park")

def ex_5_3_game():
    player1 = input("player1, choose rock, paper or scissors: ")
    player2 = input("player2, choose rock, paper or scissors: ")
    if player1 == player2:
        print("tie")
    if player1 == "rock" and player2 == "scissors":
        print("player1 won")
    if player1 == "scissors" and player2 == "rock":
        print("player2 won")
    if player1 == "paper" and player2 == "rock":
        print("player1 won")
    if player1 == "rock" and player2 == "paper":
        print("player2 won")
    if player1 == "scissors" and player2 == "paper":
        print("player1 won")
    if player1 == "paper" and player2 == "scissors":
        print("player2 won")

def ex_5_4_text():
    text = input("enter a string: ")
    if not len(text) != 0:
        print("empty string")
    else:
        print(text)

ex_5_1_park()
ex_5_2_park()
ex_5_3_game()
ex_5_4_text()
