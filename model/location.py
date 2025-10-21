class Location:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def normalize_position(self, x, y):
        return x % self.width, y % self.height

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def display(self):
        print("\n" + "=" * (self.width * 2 + 1))
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                cell = self.grid[y][x]
                line += (cell.symbol if cell else ".") + " "
            print(line)
        print("=" * (self.width * 2 + 1) + "\n")

    def is_empty(self, x, y):
        x, y = self.normalize_position(x, y)
        return self.grid[y][x] is None

    def place_agent(self, agent, x, y):
        x, y = self.normalize_position(x, y)
        if not self.is_empty(x, y):
            return False
        self.grid[y][x] = agent
        agent.x = x
        agent.y = y
        return True

    def remove_agent(self, agent):
        if 0 <= agent.y < self.height and 0 <= agent.x < self.width:
            self.grid[agent.y][agent.x] = None

    def move_agent(self, agent, new_x, new_y):
        new_x, new_y = self.normalize_position(new_x, new_y)
        if not self.is_empty(new_x, new_y):
            return False

        # clear old cell
        self.grid[agent.y][agent.x] = None

        # place in new cell
        self.grid[new_y][new_x] = agent

        # update agent coordinates
        agent.x = new_x
        agent.y = new_y

        return True
