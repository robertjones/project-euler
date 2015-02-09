# Start in centre (i=j=int(width/2))
# Move right (i+=1)
# If cell below is empty move down (j+=1) else move right
# Move down until cell to left is empty then move left
# Move left until cell above is empty then move up
# Move up until cell to the right is empty then move to the right
# Move to the right until cell below is empty them move down
# terminate when n == width * width

# up (0,-1), right (1,0) transformation i,j = -j,i

import itertools as it

def spiral(width):
    grid = [[None]*width for _ in range(width)]
    i=j=int(width/2)
    r, c = 0, -1
    for n in range(1,width**2+1):
        grid[j][i] = n
        (r,c) = (-c,r) if grid[j+r][i-c] == None else (r,c)
        (i,j) = (i+r,j+c)
    return grid

def diagonals(grid):
    return [el 
            for j, row in enumerate(grid)
            for i, el in enumerate(row)
            if i == j or i == len(row)-1-j]

print(sum(diagonals(spiral(1001))))