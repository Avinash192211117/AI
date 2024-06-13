# Define the map and colors
regions = ["A", "B", "C", "D"]
adjacent_regions = {
    "A": ["B", "C","D"],
    "B": ["A", "C"],
    "C": ["B","A"],
    "D": ["A"],
}
colors = ["Red", "Green", "Blue"]

def is_valid(coloring, region, color):
    """Check if the color assignment is valid"""
    for neighbor in adjacent_regions[region]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def solve_map_coloring(coloring, regions, index):
    """Solve the map coloring problem using backtracking"""
    if index == len(regions):
        return True

    region = regions[index]
    for color in colors:
        if is_valid(coloring, region, color):
            coloring[region] = color
            if solve_map_coloring(coloring, regions, index + 1):
                return True
            del coloring[region]  # Backtrack

    return False

def map_coloring():
    """Main function to initiate map coloring"""
    coloring = {}
    if solve_map_coloring(coloring, regions, 0):
        return coloring
    else:
        return None

# Run the map coloring algorithm
solution = map_coloring()
if solution:
    for region in regions:
        print(f"{region}: {solution[region]}")
else:
    print("No solution found")
