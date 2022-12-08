"""
https://adventofcode.com/2022/day/1
"""

import sys

INPUT_FILE_PATH = "./input.txt"

def main():
    try:
        with open(INPUT_FILE_PATH) as input_raw:
            part_1(input_raw)
            part_2(input_raw)
    except IOError as ioe:
        print("{}\nError opening {}. Terminating process.".format(ioe, INPUT_FILE_PATH), file=sys.stderr)
        sys.exit(1)


def part_1(input_raw):
    shape_select_scores = {
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3  # Scissors
    }
    win_lose_draw_scores = {
    "A": {	# Rock
        "X": 3,	    # Rock
        "Y": 6,     # Paper
        "Z": 0      # Scissors
    },
    "B" : {	# Paper
        "X": 0,	    # Rock
        "Y": 3,     # Paper
        "Z": 6      # Scissors
    },
    "C": {	# Scissors
        "X": 6,	    # Rock
        "Y": 0,     # Paper
        "Z": 3      # Scissors
    }		
    }
    lines = [i for i in input_raw.read().strip().split("\n")]
    play_scores = []
    win_scores = []
    for line in lines:
        win_score = 0 # losing score = 0
        opponents_play = line[0]
        my_play = line[-1]
        play_scores.append(shape_select_scores.get(my_play))
        win_scores.append(win_lose_draw_scores.get(opponents_play).get(my_play))
        total_score = 0
        for j in range (0, len(play_scores)):
            total_score += play_scores[j]		
            total_score += win_scores[j]
    print(total_score)
    
def part_2(input_raw):
    move_scores = {
        "A": 1,
        "B": 2,
        "C": 3
    }
    win_lose_draw_scores = {
        "X": 0,	    # Lose
        "Y": 3,     # Draw
        "Z": 6      # Win	
    }
    lines = [i for i in input_raw.read().strip().split("\n")]
    play_scores = []
    win_scores = []
    total_score = 0
    for line in lines:
        opponents_play = line[0]
        outcome = line[-1]
        win_scores.append(win_lose_draw_scores.get(outcome))
        my_move = None
        if opponents_play == "A":    # Rock
            if outcome == "X":       # Lose
                my_move = "C"
            elif outcome == "Y":     # Draw
                my_move = "A"
            elif outcome == "Z":     # Win
                my_move = "B"
        elif opponents_play == "B":  # Paper
            if outcome == "X":       # Lose
                my_move = "A"
            elif outcome == "Y":     # Draw
                my_move = "B"
            elif outcome == "Z":     # Win
                my_move = "C"
        elif opponents_play == "C":  # Scissors
            if outcome == "X":       # Lose
                my_move = "B"
            elif outcome == "Y":     # Draw
                my_move = "C"
            elif outcome == "Z":     # Win
                my_move = "A"
        play_scores.append(move_scores.get(my_move))
    for j in range (0, len(play_scores)):
        total_score += play_scores[j]		
        total_score += win_scores[j]
    print(total_score)
    
    
if __name__ == '__main__':
    main()
