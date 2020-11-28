

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
        """
            Creates array for throws of scores
        """

    def throw(self,pins):
        self.throws.append(pins)
        """
            Uses pins for a throw out of 10
        """


    def calculate_score(self):
        """
            simple function for a throw, strike and spare        
        """
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

             # fixed throw to throws in elif and else
 
BowlingGame.__doc__ = "fixes to blowling game class"