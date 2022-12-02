
opponent_moves = {
    "a": "rock",
    "b": "paper",
    "c": "scissors"
}

my_moves = {
    "x": "rock",
    "y": "paper",
    "z": "scissors"
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
        moves = line.split()
        opponent_move = opponent_moves.get(moves[0])
        my_move = my_moves.get(moves[1])

        total_score += shape_points.get(my_move)

        if opponent_move == 'rock':
            if my_move == 'rock':
                total_score += outcome_points.get("draw")
            elif my_move == 'paper':
                total_score += outcome_points.get("win")
            elif my_move == 'scissors':
                total_score += outcome_points.get("loss")
        elif opponent_move == 'paper':
            if my_move == 'rock':
                total_score += outcome_points.get("loss")
            elif my_move == 'paper':
                total_score += outcome_points.get("draw")
            elif my_move == 'scissors':
                total_score += outcome_points.get("win")
        elif opponent_move == 'scissors':
            if my_move == 'rock':
                total_score += outcome_points.get("win")
            elif my_move == 'paper':
                total_score += outcome_points.get("loss")
            elif my_move == 'scissors':
                total_score += outcome_points.get("draw")

    print(total_score)

