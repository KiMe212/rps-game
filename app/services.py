from .settings import config


def get_message_from_game_result(first_choice, second_choice):
    if first_choice == second_choice:
        return "Draw"
    game_tuple = (first_choice, second_choice)
    return config.WIN_AND_LOSE_COMBINATIONS[game_tuple]


# def get_winner(choice_first: str, choice_second: str):
#     combinations = {
#         ("rock", "paper"): f"You Lose, i have {choice_second}",
#         ("rock", "scissors"): f"You Win, i have {choice_second}",
#         ("paper", "rock"): f"You Win, i have {choice_second}",
#         ("paper", "scissors"): f"You Lose, i have {choice_second}",
#         ("scissors", "paper"): f"You Win, i have {choice_second}",
#         ("scissors", "rock"): f"You Lose, i have {choice_second}",
#     }
#     game_tuple = (choice_first, choice_second)
#     if choice_first == choice_second:
#         return "Draw"
#     return combinations[game_tuple]
