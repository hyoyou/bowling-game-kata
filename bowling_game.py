class Game(object):
    def __init__(self):
        self._rolls = [0 for i in range(21)]
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    def score(self):
        score = 0
        for frame_index in range(0, 20, 2):
            if self.is_spare(frame_index):
                score += 10 + self._rolls[frame_index + 2]
            else:
                score += self._rolls[frame_index] + self._rolls[frame_index + 1]
        return score
    
    def is_spare(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1] == 10