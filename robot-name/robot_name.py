import string
import random
from datetime import datetime

class Robot(object):
    def __init__(self):
        self.name = self.name_it()
    def reset(self):
        self.name = self.name_it()
    def name_it(self):
        random.seed(str(datetime.now()))
        return(''.join(random.choice(string.uppercase) for i in range(2)) + str(random.randint(100, 999)))




