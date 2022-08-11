import random

ai_choices = ["rock", "paper", "scissors"]
end_game_message = "Player "


def play_round(end_game_message: str):

    print("(enter end to stop the game)")
    player_choice = input("Enter rock,paper or scissors: ")

    if player_choice.lower() == "end":
        print(f"\n\nGame has ended!")
        return False, False, "end"
    else:
        ai_choice = ai_choices[random.randint(0, len(ai_choices) - 1)]

        win_message = f"wins to AI with {player_choice} vs {ai_choice}"
        lose_message = f"loses to AI with {player_choice} vs {ai_choice}"
        draw_message = f"and AI are draw with {player_choice} vs {ai_choice}"

        did_player_win_round = False
        did_ai_win_round = False

        match player_choice.lower():
            # CHECK IF PLAYER HS PICKED ROCK
            case "rock":
                # CHECK AI CHOICE
                match ai_choice:
                    case "rock":
                        did_player_win_round = False
                        did_ai_win_round = False
                        end_game_message += draw_message
                    case "paper":
                        did_player_win_round = False
                        did_ai_win_round = True
                        end_game_message += lose_message
                    case "scissors":
                        did_player_win_round = True
                        did_ai_win_round = False
                        end_game_message += win_message

                    # CHECK IF PLAYER PICKED PAPER
            case "paper":
                # CHECK AI CHOICE
                match ai_choice:
                    case "scissors":
                        did_player_win_round = False
                        did_ai_win_round = True
                        end_game_message += lose_message
                    case "paper":
                        did_player_win_round = False
                        did_ai_win_round = False
                        end_game_message += draw_message
                    case "rock":
                        did_player_win_round = True
                        did_ai_win_round = False
                        end_game_message += win_message
            # CHECK IF PLAYER PICKED SCISSORS
            case "scissors":
                # CHECK AI CHOICE
                match ai_choice:
                    case "scissors":
                        did_player_win_round = False
                        did_ai_win_round = False
                        end_game_message += draw_message
                    case "paper":
                        id_player_win_round = True
                        did_ai_win_round = False
                        end_game_message += win_message
                    case "rock":
                        did_player_win_round = False
                        did_ai_win_round = True
                        end_game_message += lose_message
            case other:
                print(f"\n\n{player_choice} is not a valid option !!!\nOptions are: {'|'.join(ai_choices)}\n")
                return False, False, "continue"

        print(f"\n\n{end_game_message}")
        return did_player_win_round, did_ai_win_round, "continue"


def run(end_game_message: str):
    player_score = 0
    ai_score = 0

    while True:
        data = play_round(end_game_message)

        if data[2] == "end":
            break
        elif data[2] == "continue":
            if data[0] is True and data[1] is False:
                player_score += 1
            elif data[0] is False and data[1] is True:
                ai_score += 1

    score_message = f"\nPlayer score: "

    if player_score > ai_score:
        score_message += f"{player_score} WINNER!!!\nAI score: {ai_score}"
    elif ai_score > player_score:
        score_message += f"{player_score}\nAI score: {ai_score} WINNER!!!"
    else:
        score_message += f"{player_score}\nAI score: {ai_score}"

    print(score_message)

# execution of program
run(end_game_message)
