import unittest
import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        else:
            balls = []
            for i in range(num):
                ball = random.choice(self.contents)
                balls.append(ball)
                self.contents.remove(ball)
            return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if balls.count(key) < value:
                break
        else:
            M += 1
    return M / num_experiments

if __name__ == '__main__':
    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    unittest.main(module='test', exit=False)