class VacuumCleaner:
    def __init__(self, room, start_pos):
        self.room = room  # The grid representing the room
        self.x, self.y = start_pos  # Starting position of the vacuum cleaner
        self.cleaned = 0  # Counter for the number of cleaned spots

    def clean(self):
        if self.room[self.x][self.y] == 1:
            self.room[self.x][self.y] = 0  # Clean the spot
            self.cleaned += 1
            print(f"Cleaned spot at ({self.x}, {self.y})")

    def move(self, direction):
        if direction == 'up' and self.x > 0:
            self.x -= 1
        elif direction == 'down' and self.x < len(self.room) - 1:
            self.x += 1
        elif direction == 'left' and self.y > 0:
            self.y -= 1
        elif direction == 'right' and self.y < len(self.room[0]) - 1:
            self.y += 1

    def run(self):
        # Simple strategy: move in a zigzag manner across the grid
        for i in range(len(self.room)):
            for j in range(len(self.room[0])):
                self.clean()
                if j < len(self.room[0]) - 1:
                    self.move('right')
            if i < len(self.room) - 1:
                self.move('down')
                if i % 2 == 1:  # Zigzag downwards
                    for _ in range(len(self.room[0]) - 1):
                        self.move('left')
                else:  # Zigzag upwards
                    for _ in range(len(self.room[0]) - 1):
                        self.move('right')

        print(f"Total spots cleaned: {self.cleaned}")

# Define the room grid
room = [
    [1, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 1]
]

# Starting position of the vacuum cleaner
start_pos = (0, 0)

vacuum = VacuumCleaner(room, start_pos)
vacuum.run()
