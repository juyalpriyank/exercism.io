class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[len(self.scores) - 1]

    def personal_best(self):
        top = self._sort()
        return top[0]

    def personal_top_three(self):
        top_3 = self._sort()
        return top_3

    def _sort(self):
        self.scores.sort(reverse=True)
        return self.scores[:3]
