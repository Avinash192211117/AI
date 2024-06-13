import heapq

class PuzzleState:
    def __init__(self, board, moves=0, parent=None):
        self.board = board
        self.blank = self.find_blank()
        self.moves = moves
        self.parent = parent

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)

    def is_goal(self):
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal_state

    def manhattan_distance(self):
        distance = 0
        goal_pos = {value: (i, j) for i, row in enumerate([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) for j, value in enumerate(row)}
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    goal_i, goal_j = goal_pos[self.board[i][j]]
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    def neighbors(self):
        neighbors = []
        x, y = self.blank
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    def __lt__(self, other):
        return False

def a_star(initial_state):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (initial_state.manhattan_distance(), initial_state))

    while open_list:
        _, current_state = heapq.heappop(open_list)
        if current_state.is_goal():
            return current_state

        closed_list.add(tuple(map(tuple, current_state.board)))
        for neighbor in current_state.neighbors():
            if tuple(map(tuple, neighbor.board)) not in closed_list:
                heapq.heappush(open_list, (neighbor.manhattan_distance() + neighbor.moves, neighbor))

    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution.board)
        solution = solution.parent
    path = path[::-1]

    for board in path:
        for row in board:
            print(row)
        print()

if __name__ == "__main__":
    initial_board = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]
    initial_state = PuzzleState(initial_board)
    solution = a_star(initial_state)
    if solution:
        print("Solution found:")
        print_solution(solution)
        print(f"Total moves to solve the puzzle: {solution.moves}")
    else:
        print("No solution found.")
