class Game(object):
    def __init__(self):
        self._rolls = [0 for i in range(21)]
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    def score(self):
        score = 0
        frame_index = 0
        for frame in range(10):
            if self.is_strike(frame_index):
                score += self.strike_score(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                score += self.spare_score(frame_index)
                frame_index += 2
            else:
                score += self.frame_score(frame_index)
                frame_index += 2
        return score
    
    def is_strike(self, frame_index):
        return self._rolls[frame_index] == 10

    def is_spare(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1] == 10

    def strike_score(self, frame_index):
        return 10 + self._rolls[frame_index + 1] + self._rolls[frame_index + 2]

    def spare_score(self, frame_index):
        return 10 + self._rolls[frame_index + 2]

    def frame_score(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1]
