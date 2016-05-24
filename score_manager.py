scores = []


class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def is_highscore(test_score):
    if len(scores) < 5 or test_score > scores[-1].score:
        return True
    return False


def add_score(new_score):
    global scores
    if len(scores) < 5:
        scores.append(new_score)
        save_scores()
        return
    if new_score.score > scores[-1].score:
        for i in range(5):
            if scores:
                if len(scores) > i and scores[i].score < new_score.score:
                    scores.insert(i, new_score)
                    scores = scores[:5]
                    save_scores()
                    return
            else:
                scores.append(new_score)
                save_scores()


def save_scores():
    with open("res/scores", "w") as file:
        for line in scores:
            file.write(str(line.name))
            file.write("\n")
            file.write(str(line.score))
            file.write("\n")


def load_scores():
    global scores
    with open("res/scores", "w+") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            name = lines[i]
            name = name.replace("\n", "")
            score = int(lines[i+1])
            scores.append(Score(name, score))
