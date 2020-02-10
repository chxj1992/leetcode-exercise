import unittest
from typing import List, Dict


class Solution:

    def __init__(self) -> None:
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.direction = (0, 1)
        self.position = (0, 0)
        self.max_distance = 0
        self.obstacle_x_map: Dict[int:List] = {}
        self.obstacle_y_map: Dict[int:List] = {}

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        for o in obstacles:
            self.obstacle_x_map[o[0]] = self.obstacle_x_map[o[0]] if o[0] in self.obstacle_x_map else []
            self.obstacle_x_map[o[0]].append(o)
            self.obstacle_y_map[o[1]] = self.obstacle_y_map[o[1]] if o[1] in self.obstacle_y_map else []
            self.obstacle_y_map[o[1]].append(o)

        for command in commands:
            if command == -1:
                self.turn_right()
            elif command == -2:
                self.turn_left()
            else:
                self.move(command)
        return self.max_distance

    def move(self, step: int):
        position = (self.position[0] + self.direction[0] * step, self.position[1] + self.direction[1] * step)

        if self.direction == (0, 1) and self.position[0] in self.obstacle_x_map:
            for o in self.obstacle_x_map[self.position[0]]:
                if self.position[1] < o[1] <= position[1]:
                    position = (o[0], o[1] - 1)
                    break

        if self.direction == (0, -1) and self.position[0] in self.obstacle_x_map:
            for o in self.obstacle_x_map[self.position[0]]:
                if position[1] <= o[1] < self.position[1]:
                    position = (o[0], o[1] + 1)
                    break

        if self.direction == (1, 0) and self.position[1] in self.obstacle_y_map:
            for o in self.obstacle_y_map[self.position[1]]:
                if self.position[0] < o[0] <= position[0]:
                    position = (o[0] - 1, o[1])
                    break

        if self.direction == (-1, 0) and self.position[1] in self.obstacle_y_map:
            for o in self.obstacle_y_map[self.position[1]]:
                if position[0] <= o[0] < self.position[0]:
                    position = (o[0] + 1, o[1])
                    break

        self.position = position
        self.calc_distance()

    def turn_left(self):
        index = self.directions.index(self.direction)
        if index > 0:
            index -= 1
        else:
            index = 3
        self.direction = self.directions[index]

    def turn_right(self):
        index = self.directions.index(self.direction)
        if index < 3:
            index += 1
        else:
            index = 0
        self.direction = self.directions[index]

    def calc_distance(self):
        self.max_distance = max(self.max_distance,
                                self.position[0] * self.position[0] + self.position[1] * self.position[1])


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(25, s.robotSim([4, -1, 3], []))

    def test2(self):
        s = Solution()
        self.assertEqual(65, s.robotSim([4, -1, 4, -2, 4], [[2, 4]]))


if __name__ == '__main__':
    unittest.main()
