import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to update the grid for each generation
def update_grid(grid):
    new_grid = np.zeros_like(grid)
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            # Count the number of alive neighbors
            num_alive_neighbors = np.sum(grid[max(0, i-1):min(rows, i+2), max(0, j-1):min(cols, j+2)]) - grid[i, j]
            # Apply the rules of the game
            if grid[i, j] == 1:
                if num_alive_neighbors < 2 or num_alive_neighbors > 3:
                    new_grid[i, j] = 0  # Dies due to underpopulation or overcrowding
                else:
                    new_grid[i, j] = 1  # Lives on to the next generation
            else:
                if num_alive_neighbors == 3:
                    new_grid[i, j] = 1  # A new cell is born
    return new_grid

# Function to initialize the grid randomly
def random_initialization(rows, cols):
    return np.random.randint(2, size=(rows, cols))

# Function to update the animation frames
def update_anim(frameNum, img, grid):
    new_grid = update_grid(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# Set the size of the grid
rows = 50
cols = 50

# Initialize the grid randomly
grid = random_initialization(rows, cols)

# Set up the animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(fig, update_anim, fargs=(img, grid), frames=100, blit=True, interval=50)

plt.show()