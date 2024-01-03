import numpy as np

class Rubik:
    
    def __init__(self):
        self.cube = np.array([  [['g', 'g', 'g'],
                                ['g', 'g', 'g'],
                                ['g', 'g', 'g']], #left
            
                                [['w', 'w', 'w'],
                                ['w', 'w', 'w'],
                                ['w', 'w', 'w']], #front

                                [['b', 'b', 'b'],
                                ['b', 'b', 'b'],
                                ['b', 'b', 'b']], #right

                                [['y', 'y', 'y'],
                                ['y', 'y', 'y'],
                                ['y', 'y', 'y']], #back

                                [['o', 'o', 'o'],
                                ['o', 'o', 'o'],
                                ['o', 'o', 'o']], #top
                            
                                [['r', 'r', 'r'], 
                                ['r', 'r', 'r'], 
                                ['r', 'r', 'r']] #bottom

                        ])
        
    def get_front(self):
        return self.cube[0]
        
    def get_bottom(self):
        return self.cube[1]
        
    def get_back(self):
        return self.cube[2]
        
    def get_top(self):
        return self.cube[3]
        
    def get_left(self):
        return self.cube[4]
    
    def get_right(self):
        return self.cube[5]
        
    def rotate(self, axis: str, axis_column: int, direction: int):

        if axis_column > 2 or axis_column < 0:
            raise ValueError
        
        new_cube = self.cube.copy()
        
        if axis == "left":

            vertical_sides = [1, 5, 3, 4]
            for side_index in range(4):
                if direction % 4 == 0:
                    break
                new_side = vertical_sides[(side_index + direction) % 4]
                for row in range(3):
                    if new_side == 3:
                        new_cube[vertical_sides[side_index]][row][axis_column] = self.cube[new_side][-1-row][-1-axis_column]
                    elif vertical_sides[side_index] == 3:
                        new_cube[vertical_sides[side_index]][-1-row][-1-axis_column] = self.cube[new_side][row][axis_column]
                    else:
                        new_cube[vertical_sides[side_index]][row][axis_column] = self.cube[new_side][row][axis_column]

            if axis_column == 0:
                new_cube[0] = np.rot90(self.cube[0], direction)

            elif axis_column == 2:
                new_cube[2] = np.rot90(self.cube[2], -direction)

        if axis == "top":

            for side in range(4):
               new_side = (side - direction) % 4
               new_cube[side][axis_column] = self.cube[new_side][axis_column]

            if axis_column == 0:
                new_cube[4] = np.rot90(self.cube[4], direction)

            elif axis_column == 2:
                new_cube[5] = np.rot90(self.cube[5], -direction)

        if axis == "front":

            vertical_sides = [0, 4, 2, 5]

            new_cube[0] = np.rot90(self.cube[0], 1)
            new_cube[4] = np.rot90(self.cube[4], 2)
            new_cube[2] = np.rot90(self.cube[2], -1)

            self.cube[0] = np.rot90(self.cube[0], 1)
            self.cube[4] = np.rot90(self.cube[4], 2)
            self.cube[2] = np.rot90(self.cube[2], -1)

            for side_index in range(4):
               new_side = vertical_sides[(side_index + direction) % 4]
               new_cube[vertical_sides[side_index]][axis_column] = self.cube[new_side][axis_column]

            new_cube[0] = np.rot90(new_cube[0], -1)
            new_cube[4] = np.rot90(new_cube[4], 2)
            new_cube[2] = np.rot90(new_cube[2], 1)

            if axis_column == 0:
                new_cube[1] = np.rot90(self.cube[1], direction)

            elif axis_column == 2:
                new_cube[3] = np.rot90(self.cube[3], -direction)

        self.cube = new_cube

if __name__ == "__main__":
    rubik = Rubik()
    while(True):
        print(rubik.cube)
        instruction = input("Rotate: ").split()
        if instruction[0] in ["top", "left", "front"]:
            rubik.rotate(instruction[0], int(instruction[1]), int(instruction[2]))
        elif instruction[0] == "exit":
            break
        else:
            print(f"No known axis named {instruction[0]}")
