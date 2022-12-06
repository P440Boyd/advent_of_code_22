from typing import List
from read_input import read_input_from_daynum


class Round:
    def __init__(self, line) -> None:
        self.translation_dict = {
            "A": "rock",
            "B": "paper",
            "C": "scissors",
            "X": "rock",
            "Y": "paper",
            "Z": "scissors",
        }
        self.score_dict = {"rock": 1, "paper": 2, "scissors": 3}
        self.their_choice = line.split()[0]
        self.their_score = 0
        self.my_choice = line.split()[1]
        self.my_score = 0
        self._translate_inputs()

    def evaluate_scores(self):
        self.their_score = self.score_dict[self.their_choice]
        self.my_score = self.score_dict[self.my_choice]
        their_outcome, my_outcome = self.calculate_outcome()
        self.their_score += their_outcome
        self.my_score += my_outcome
        return self.their_score, self.my_score

    def _translate_inputs(self):
        self.their_choice = self.translation_dict[self.their_choice]
        self.my_choice = self.translation_dict[self.my_choice]

    def calculate_outcome(self):
        if self.my_choice == self.their_choice:
            return 3, 3
        elif self.my_choice == "rock":
            return (0, 6) if self.their_choice == "scissors" else (6, 0)
        elif self.my_choice == "paper":
            return (0, 6) if self.their_choice == "rock" else (6, 0)
        elif self.my_choice == "scissors":
            return (0, 6) if self.their_choice == "paper" else (6, 0)


def main():
    input_lines = read_input_from_daynum(2)
    overall_score = 0
    with open("game_results.txt", "w+") as result_fp:
        for line in input_lines:
            game_round = Round(line)
            _, my_score = game_round.evaluate_scores()
            overall_score += my_score
            result_fp.write(
                f"Their choice: {game_round.their_choice}. My choice: {game_round.my_choice}. My score: {game_round.my_score}.\n"
            )
        result_fp.write(f"Game is over. Final score: {overall_score}.")


if __name__ == "__main__":
    main()
