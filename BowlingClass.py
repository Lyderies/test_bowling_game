

class BowlingGame(object):
    """Class for bowling frames

    Args:
        object ([self]): [
            Class has functions which allow the tests to check if a strike, spare or number of pins were counted
            ]
    """
    def __init__(self):
        self.throws= [] # change throw to throws 
        self.score= 0

    def throw(self,pins):
        self.throws.append(pins)


    def calculate_score(self):
        ball = 0
        for frames in range(10):
            if self.throws[ball]==10:
                self.score +=10 + self.throws[ball+1] + self.throws[ball +2]
                ball += 1
            elif self.throws[ball] + self.throws[ball+1] == 10:
                self.score += 10 + self.throws [ball +2]
                ball +=2
            else:
                self.score += self.throws[ball] + self.throws[ball + 1]
                ball += 2

            calculate_score.__doc__ = "fixed throw to throws in elif and else"
 
