CHOICE_LIST = ('rock', 'paper', 'scissors')


def get_winner(choice_first: str, choice_second: str):
    combinations = {
        ("rock", "paper"): f"You Lose, i have {choice_second}",
        ("rock", "scissors"): f"You Win, i have {choice_second}",
        ("paper", "rock"): f"You Win, i have {choice_second}",
        ("paper", "scissors"): f"You Lose, i have {choice_second}",
        ("scissors", "paper"): f"You Win, i have {choice_second}",
        ("scissors", "rock"): f"You Lose, i have {choice_second}",
    }
    game_tuple = (choice_first, choice_second)
    if choice_first == choice_second:
        return "Draw"
    return combinations[game_tuple]
