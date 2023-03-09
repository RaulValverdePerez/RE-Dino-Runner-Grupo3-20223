
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird (Obstacle):
    BIRDS = {
        "LARGE":(BIRD, 250)
    }
    def __init__(self, bird_type):
        image, bird_pos = self.BIRDS[bird_type]
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = bird_pos