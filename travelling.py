from itertools import permutations

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[-1]][route[0]]
    return total_distance

def brute_force_tsp(distances):
    n = len(distances)
    cities = list(range(1, n))
    shortest_route = None
    min_distance = float('inf')
    
    for perm in permutations(cities):
        current_route = [0] + list(perm)
        current_distance = calculate_distance(current_route, distances)
        
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = current_route
    
    shortest_route.append(0)
    return shortest_route, min_distance

distances = [
        [ 0, 12, 10, 19 ,8 ],  
        [ 12, 0, 3, 7 ,2 ],  
        [ 10, 3, 0, 6,20 ],  
        [ 19, 7, 6, 0,4 ],
        [ 8, 2, 20, 4,0 ]
        ]
route, total_distance = brute_force_tsp(distances)
print("Route:", route)
print("Total distance:", total_distance)
