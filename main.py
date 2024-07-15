import random
bot_choose_list = ["r", "p", "s"]
mode = input("2 players = 2/ 1 player= 1:")

if mode == "2":
    print("if you don't input right I will punish you by deducting the round without points")
    player1 = input("player 1 name:")
    player2 = input("player 2 name:")
    round_counter = 0
    player1_point = 0
    player2_point = 0
    for i in range(5):
        print("ROCK=R, PAPER=P, SCISSORS=S")
        player1_choose = input(f"{player1} choose:").lower()
        print("\n" * 12)
        print("ROCK=R, PAPER=P, SCISSORS=S")
        player2_choose = input(f"{player2} choose:").lower()
        valid_choices = ['r', 'p', 's']
        if player1_choose not in valid_choices or player2_choose not in valid_choices:
            print("Are you kidding me?")
            print("The round will be counted without points")
            continue
        print("")
        print("")
        print("")
        if player1_choose == "r" and player2_choose == "s":
            print(f"{player1} win this round!")
            player1_point += 1
        elif player2_choose == "r" and player1_choose == "s":
            print(f"{player2} win this round!")
            player2_point += 1
        elif player1_choose == "p" and player2_choose == "r":
            print(f"{player1} win this round!")
            player1_point += 1
        elif player1_choose == "r" and player2_choose == "p":
            print(f"{player2} win this round!")
            player2_point += 1
        elif player1_choose == "s" and player2_choose == "p":
            print(f"{player1} win this round!")
            player1_point += 1
        elif player1_choose == "p" and player2_choose == "s":
            print(f"{player2} win this round!")
            player2_point += 1
        elif player1_choose == player2_choose and player1_choose != "":
            print("tie this round!")
        round_counter += 1
        print(f"{player1} points: {player1_point}")
        print(f"{player2} points: {player2_point}")
        print("\n" * 3)

        if round_counter == 5:
            print(f"{player1} points:{player1_point}")
            print(f"{player2} points:{player2_point}")
            if player1_point > player2_point:
                print(f"{player1} WINS")
            elif player2_point > player1_point:
                print(f"{player2} WINS")
            elif player1_point == player2_point:
                print(f"TIE")
            break
if mode == "1":
    print("if you don't input right I will punish you by deducting the round without points")
    player = input("player name:")
    bot = "Steve"
    round_counter = 0
    player_point = 0
    bot_point = 0
    for i in range(5):
        print("ROCK=R, PAPER=P, SCISSORS=S")
        player_choose = input(f"{player} choose:").lower()
        print("ROCK=R, PAPER=P, SCISSORS=S")
        bot_choose = random.choice(bot_choose_list)
        print("steve choose:", bot_choose)
        valid_choices = ['r', 'p', 's']
        if player_choose not in valid_choices or bot_choose not in valid_choices:
            print("Are you kidding me?")
            print("The round will be counted without points")
            continue
        if player_choose == "r" and bot_choose == "s":
            print(f"{player} win this round!")
            player_point += 1
        elif bot_choose == "r" and player_choose == "s":
            print(f"{bot} win this round!")
            bot_point += 1
        elif player_choose == "p" and bot_choose == "r":
            print(f"{player} win this round!")
            player_point += 1
        elif player_choose == "r" and bot_choose == "p":
            print(f"{bot} win this round!")
            bot_point += 1
        elif player_choose == "s" and bot_choose == "p":
            print(f"{player} win this round!")
            player_point += 1
        elif player_choose == "p" and bot_choose == "s":
            print(f"{bot} win this round!")
            bot_point += 1
        elif player_choose == bot_choose and player_choose != "":
            print("tie this round!")
        round_counter += 1
        print(f"{player} points: {player_point}")
        print(f"{bot} points: {bot_point}")
        print("\n" * 2)

        if round_counter == 5:
            print(f"{player} points:{player_point}")
            print(f"{bot} points:{bot_point}")
            if player_point > bot_point:
                print(f"{player} WINS")
            elif bot_point > player_point:
                print(f"{bot} WINS")
            elif player_point == bot_point:
                print(f"TIE")
            break
