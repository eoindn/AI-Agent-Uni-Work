# main.py
from model.agent import Agent
from model.location import Location

grid = Location(10, 10)
shark = Agent(1, 1, "S", "Shark")

grid.place_agent(shark, 1, 1)
print("Initial grid:")
grid.display()

print("Moving shark to (3, 1)...")
moved = grid.move_agent(shark, 3, 1)
print("Move success:", moved)
grid.display()

print("Moving shark to (3, 4)...")
moved = grid.move_agent(shark, 3, 4)
print("Move success:", moved)
grid.display()
