import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move="", g=0):
        self.board = board            # 2D tuple representing the 3x3 board (0 represents empty space)
        self.parent = parent          # Pointer to parent node to reconstruct path
        self.move = move              # The move taken to reach this state ('Up', 'Down', 'Left', 'Right')
        self.g = g                    # Cost from start to current node
        self.h = self.calculate_h()   # Manhattan Distance heuristic
        self.f = self.g + self.h      # Total estimated cost f(n) = g(n) + h(n)

    def calculate_h(self):
        """Calculates total Manhattan Distance of all tiles from their goal positions."""
        # Goal positions map: value -> (row, col)
        goal_positions = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 0: (2, 2)
        }
        
        distance = 0
        for r in range(3):
            for c in range(3):
                val = self.board[r][c]
                if val != 0:  # Skip the blank tile
                    target_r, target_c = goal_positions[val]
                    distance += abs(r - target_r) + abs(c - target_c)
        return distance

    def find_blank(self):
        """Finds the (row, col) position of the blank tile (0)."""
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    return r, c

    def get_neighbors(self):
        """Generates valid successor states by moving the blank tile."""
        neighbors = []
        r, c = self.find_blank()
        
        # Possible moves: (row_offset, col_offset, move_name)
        moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

        for dr, dc, move_name in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                # Create a new board configuration by swapping
                new_board = [list(row) for row in self.board]
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                
                # Convert back to tuple for hashability
                tuple_board = tuple(tuple(row) for row in new_board)
                neighbors.append(PuzzleState(tuple_board, self, move_name, self.g + 1))
                
        return neighbors

    def __lt__(self, other):
        """Comparator for the priority queue based on f-score."""
        return self.f < other.f


def is_solvable(board_tuple):
    """Checks if the given 8-puzzle board configuration is solvable."""
    # Flatten board ignoring the empty tile (0)
    flat = [val for row in board_tuple for val in row if val != 0]
    
    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
                
    # An 8-puzzle configuration is solvable if and only if the inversion count is even
    return inversions % 2 == 0


def solve_8_puzzle(start_board):
    if not is_solvable(start_board):
        return None, "This puzzle configuration is unsolvable!"

    start_state = PuzzleState(start_board)
    
    # Priority Queue for A* search: stores (f_score, state)
    open_set = []
    heapq.heappush(open_set, start_state)
    
    # Keep track of visited boards with their minimum cost g(n)
    visited = {start_board: 0}

    while open_set:
        current = heapq.heappop(open_set)

        # Check if goal state is reached (0 is in the bottom-right corner)
        if current.h == 0:
            path = []
            while current.parent:
                path.append((current.move, current.board))
                current = current.parent
            path.reverse()
            return path, "Solved!"

        for neighbor in current.get_neighbors():
            # If not visited or found a shorter path to this state
            if neighbor.board not in visited or neighbor.g < visited[neighbor.board]:
                visited[neighbor.board] = neighbor.g
                heapq.heappush(open_set, neighbor)

    return None, "No solution found."


def print_board(board):
    """Utility function to display the board nicely."""
    for row in board:
        print(" ".join(str(val) if val != 0 else "_" for val in row))
    print()


# --- Example Usage ---
if __name__ == "__main__":
    # Define initial state (0 represents the blank space)
    # Target state:
    # 1 2 3
    # 4 5 6
    # 7 8 _
    
    initial_board = (
        (1, 2, 3),
        (4, 0, 6),
        (7, 5, 8)
    )

    print("Initial Board State:")
    print_board(initial_board)

    moves, status = solve_8_puzzle(initial_board)

    if moves:
        print(f"Solution found in {len(moves)} steps:\n")
        for step, (move, board) in enumerate(moves, 1):
            print(f"Step {step}: Move Blank {move}")
            print_board(board)
    else:
        print(status)
