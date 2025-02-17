import random
import json
import os
from typing import List, Literal

class Game:
    CACHE_FILE = './cache/game_state.json'
    BEST_SCORE_FILE = './cache/best_score.json'

    def __init__(self, width = 4, height = 4, cache=True) -> None:
        """
        Creates new grid width default dimentions 4x4 or specified by user.
        After this it adds two random elements in the grid in empty cells
        """
        self.width = width
        self.height = height
        self.points = 0
        self.grid = [[0] * self.width for _ in range(self.height)]

        self.__spawn_random_number()
        self.__spawn_random_number()

        # load game state from cache
        if cache:
            self.load_state()

        # load best score
        self.best_score = self.load_best_score()

        
    def __spawn_random_number(self) -> None:
        """
        Spawns random element on the grid
        """
        empty_cells = []

        for y in range(self.height):
            for x in range(self.width):
                if self.grid[x][y] == 0:
                    empty_cells.append((x, y))

        rx, ry = random.choice(empty_cells)
        random_value = 2 if random.random() > 0.1 else 4

        self.grid[rx][ry] = random_value

    def __merge(self, arr: List[int]) -> List[int]:
        """
        Merges elements in array. Note that it can only perform 1 level of merging
        """
        elements = [el for el in arr if el != 0]

        if len(elements) < 2:
            return elements
        
        l, r = 0, 1
        while r < len(elements):
            if elements[l] == elements[r]:
                elements[l] = elements[l] * 2
                del elements[r]

                self.points += elements[l] # accumulate points on merge

            l += 1
            r += 1

        return elements
    
    def __fill_cells(self, arr: List[int]) -> List[int]:
        """
        Fills not taken cells with 0s
        """
        new_elements = [0] * (self.width - len(arr))
        return arr + new_elements


    def __move_left(self) -> None:
        """
        Moves elements to the left by going through each row, merging them and then filling with 0s
        """
        for row in range(self.height):
            self.grid[row] = self.__fill_cells(self.__merge(self.grid[row]))


    def __move_right(self) -> None:
        """
        Moves elements in a row to the right
        """
        for row in range(self.height):
            self.grid[row] = list(reversed(
                self.__fill_cells(self.__merge(self.grid[row][::-1]))
            ))

    
    def __move_up(self) -> None:
        """
        Transposes the matrix and merges elements like in move left, then transposes it back to original shape
        """
        transposed = list(map(list, zip(*self.grid)))

        for col in range(self.height):
            transposed[col] = self.__fill_cells(self.__merge(transposed[col]))
        
        self.grid = list(map(list, zip(*transposed)))


    def __move_down(self) -> None:
        """
        Transposes the matrix and merges elements like in move right, then transposes it back to original shape
        """

        transposed = list(map(list, zip(*self.grid)))

        for col in range(self.height):
            transposed[col] = list(reversed(
                self.__fill_cells(self.__merge(transposed[col][::-1]))
            ))

        self.grid = list(map(list, zip(*transposed)))


    def show_grid(self) -> None:
        """
        Shows current grid
        """
        print(f"Points: {self.points}", end=", ")
        print(f"Best Score: {self.best_score}")

        for row in self.grid:
            print('\n')
            for col in row:
                print(f'   {col}   ', end='')
            print('\n')
        print()

    
    def make_move(self, move: Literal['UP', 'DOWN', 'LEFT', 'RIGHT']) -> None:
        """
        Performs a move in a given direction
        """
        if move == 'LEFT':
            self.__move_left()
        elif move == 'RIGHT':
            self.__move_right()
        elif move == 'UP':
            self.__move_up()
        else:
            self.__move_down()

        self.__spawn_random_number()

        if self.points > self.best_score:
            self.best_score = self.points
            self.save_best_score(self.best_score)


    def can_move(self) -> bool:
        """
        Checks if next move is possible. The game is ended if the following is true:
        1. All cells are marked
        2. No adjecent cells are of the same value
        """

        # check if there are any free empty cells first
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    return True
                
        neighbours = [
            (-1,-1),
            (0,-1),
            (1,-1),
            (-1, 0),
            (1,0),
            (-1,1),
            (0,1),
            (1,1),
        ]

        # check if adjecent elements are the same
        for y in range(self.height):
            for x in range(self.width):
                for nx, ny in neighbours:
                    if (0 <= x + nx < self.width and 
                        0 <= y + ny < self.height and 
                        self.grid[y][x] == self.grid[y + ny][x + nx]):
                        return True
                
        return False
    

    def save_state(self) -> None:
        """
        Saves current game state to json file
        """
        os.makedirs(os.path.dirname(self.CACHE_FILE), exist_ok=True)

        with open(self.CACHE_FILE, 'w') as f:
            json.dump({
                'grid': self.grid,
                'points': self.points,
            }, f)


    def load_state(self) -> None:
        """
        Loads game state from cache file
        """
        if os.path.exists(self.CACHE_FILE):
            with open(self.CACHE_FILE, 'r') as f:
                state = json.load(f)
                self.grid = state['grid']
                self.points = state['points'] 

    def clear_cache(self) -> None:
        """
        Clears the state cache by removing the cache file
        """
        if os.path.exists(self.CACHE_FILE):
            os.remove(self.CACHE_FILE)


    def save_best_score(self, score: int) -> None:
        """
        Saves player's best score ever achieved
        """
        os.makedirs(os.path.dirname(self.BEST_SCORE_FILE), exist_ok=True)

        with open(self.BEST_SCORE_FILE, 'w') as f:
            json.dump({'score': score}, f)

    
    def load_best_score(self) -> int:
        """
        Loads best score achieved by player
        """
        if os.path.exists(self.BEST_SCORE_FILE):
            with open(self.BEST_SCORE_FILE, 'r') as f:
                score_state = json.load(f)
                return score_state['score']
        else:
            return 0