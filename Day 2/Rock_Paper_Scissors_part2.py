from read_input import read_input_from_daynum
from typing import List


class Round:
    def __init__(self, line: str) -> None:
        self.translation_dict = {
            "A": "rock",
            "B": "paper",
            "C": "scissors",
            "X": "lose",
            "Y": "draw",
            "Z": "win",
        }
        self.choice_score_dict = {"rock": 1, "paper": 2, "scissors": 3}
        self.result_score_dict = {"win": 6, "draw": 3, "lose": 0}
        self.their_choice = line.split()[0]
        self.desired_outcome = line.split()[1]
        self.my_choice = ""
        self.my_score = 0
        self._translate_inputs()

    def _translate_inputs(self):
        self.their_choice = self.translation_dict[self.their_choice]
        self.desired_outcome = self.translation_dict[self.desired_outcome]

    def evaluate_scores(self):
        my_choice = self._calculate_my_choice()
        return (
            self.choice_score_dict[my_choice]
            + self.result_score_dict[self.desired_outcome]
        )

    def _calculate_my_choice(self):
        if self.their_choice == "paper":
            if self.desired_outcome == "draw":
                return "paper"
            elif self.desired_outcome == "lose":
                return "rock"
            elif self.desired_outcome == "win":
                return "scissors"
        elif self.their_choice == "rock":
            if self.desired_outcome == "draw":
                return "rock"
            elif self.desired_outcome == "lose":
                return "scissors"
            elif self.desired_outcome == "win":
                return "paper"
        elif self.their_choice == "scissors":
            if self.desired_outcome == "draw":
                return "scissors"
            elif self.desired_outcome == "lose":
                return "paper"
            elif self.desired_outcome == "win":
                return "rock"


def main():
    input_lines = read_input_from_daynum(2)
    overall_score = 0
    with open("game_results.txt", "w+") as result_fp:
        for line in input_lines:
            game_round = Round(line)
            my_score = game_round.evaluate_scores()
            overall_score += my_score
            result_fp.write(
                f"Their choice: {game_round.their_choice}. Desired outcome is: {game_round.desired_outcome}. My score: {my_score}.\n"
            )
        result_fp.write(f"Game is over. Final score: {overall_score}.")


if __name__ == "__main__":
    main()
