#!/usr/bin/python3

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1: # Arrive at cell
                perimeter += 4 # Add 4 edges initally

                """ Check if there's land above"""
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1 # Remove shared edges

                """ Check if there's land below"""
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1 # Remove shared edge

                """ Check if there's land ot the left"""
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1 # Remove shared edge

                """ Check if there's land to the right"""
                if c <cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1 # Remove shared edge

    return perimeter

