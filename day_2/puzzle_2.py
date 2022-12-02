opponent_moves = {
    "a": "rock",
    "b": "paper",
    "c": "scissors"
}

desired_outcome = {
    "x": "loss",
    "y": "draw",
    "z": "win"
}

shape_points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

outcome_points = {
    "loss": 0,
    "draw": 3,
    "win": 6
}

if __name__ == "__main__":
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    total_score = 0

    for line in lines:
        line = line.replace("\n", "").strip().lower()
        round = line.split()
        opponent_move = opponent_moves.get(round[0])
        outcome = desired_outcome.get(round[1])

        total_score += outcome_points.get(outcome)

        if outcome == 'win':
            if opponent_move == 'rock':
                total_score += shape_points.get("paper")
            elif opponent_move == 'paper':
                total_score += shape_points.get("scissors")
            elif opponent_move == 'scissors':
                total_score += shape_points.get("rock")
        elif outcome == 'loss':
            if opponent_move == 'rock':
                total_score += shape_points.get("scissors")
            elif opponent_move == 'paper':
                total_score += shape_points.get("rock")
            elif opponent_move == 'scissors':
                total_score += shape_points.get("paper")
        elif outcome == 'draw':
            if opponent_move == 'rock':
                total_score += shape_points.get("rock")
            elif opponent_move == 'paper':
                total_score += shape_points.get("paper")
            elif opponent_move == 'scissors':
                total_score += shape_points.get("scissors")

    print(total_score)
