import time
import random
import math
import heapq
import sys

instances = 50
iterations = 25000

def dynamic_programming_partition(sequence):
    total_sum = sum(sequence)
    half_sum = total_sum // 2

    # Initialize a table where table[i][j] will be True if a subset of the first i numbers can sum to j
    table = [[False] * (half_sum + 1) for _ in range(len(sequence) + 1)] 
    
    # Set of 0 numbers sum to 0 
    table[0][0] = True 
    
    # Populate the table
    for i in range(1, len(sequence) + 1):
        for j in range(half_sum + 1):
            if sequence[i-1] <= j:
                # Include sequence[i-1] in the subset or exclude it
                table[i][j] = table[i-1][j] or table[i-1][j-sequence[i-1]]
            else:
                # Exclude sequence[i-1] from the subset
                table[i][j] = table[i-1][j]
    
    # Find the maximum value j for which table[len(sequence)][j] is True, where j is not greater than half of the total sum
    for j in range(half_sum, -1, -1):
        if table[len(sequence)][j]:
            return total_sum - 2*j  
    return None

def kk(array):
    size = len(array)

    # Remove elements for a max-heap behavior with min-heap structure
    ignored = [-x for x in array] 
    heapq.heapify(ignored)

    # Repeatedly combines two largest elements until one remains
    for i in range(size-1):
        max = heapq.heappop(ignored)
        second_max = heapq.heappop(ignored)
        heapq.heappush(ignored, (max-second_max))
    return -ignored[0]

def generate_random_instance(array):
    # Generates a random solution sequence of +1 and -1 for the input array.
    size = len(array)
    random_sequence = []
    for i in range(size):
        choose = random.choice([1, -1])
        random_sequence.append(choose)
    return random_sequence

def calculate_residue(array, sequence):
    size = len(array)
    residue = 0
    for i in range(size):
        residue += array[i] * sequence[i]
    return abs(residue)

def repeated_random(array):
    # Applies the repeated random heuristic to find a solution with minimum residue.
    best = generate_random_instance(array)
    for i in range(iterations):
        current = generate_random_instance(array)
        if calculate_residue(array, current) < calculate_residue(array, best):
            best = current
    return calculate_residue(array, best)

def find_neighbor(sequence):
    size = len(sequence)
    rand_i, rand_j = random.sample(range(size), 2)
    neighbor = sequence.copy()
    neighbor[rand_i] = rand_j
    return neighbor

def hill_climbing(array):
    best = generate_random_instance(array)
    for i in range(iterations):
        current_neighbor = find_neighbor(best)
        if calculate_residue(array, current_neighbor) < calculate_residue(array, best):
            best = current_neighbor
    return calculate_residue(array, best)

def find_threshold(array, i, current, neighbor):
    nom = math.exp(-(calculate_residue(array, neighbor) -
                   calculate_residue(array, current)))
    denom = ((10**10) * (0.8 ** (i//300)))
    return nom/denom

def simulated_annealing(array):
    current = generate_random_instance(array)
    best = current.copy()
    for i in range(1, iterations+1):
        neighbor = find_neighbor(current)
        if calculate_residue(array, neighbor) < calculate_residue(array, current):
            current = neighbor
        else:
            # calculate probability of annealing
            threshold = find_threshold(array, i, current, neighbor)
            if random.random() < threshold:
                current = neighbor
        if calculate_residue(array, current) < calculate_residue(array, best):
            best = current
    return calculate_residue(array, best)

def generate_random_partitioned_instance(array):
    # Generates a random partition of the array by assigning each element a random group
    size = len(array)
    random_sequence = []
    for i in range(size):
        choose = random.randint(0, size-1)
        random_sequence.append(choose)
    return random_sequence

def calculate_partitioned_residue(array, sequence):
    # Calculates the residue of a partitioned solution by grouping elements and applying KK algorithm
    size = len(array)
    modified_array = [0] * size
    for i in range(size):
        modified_array[sequence[i]] += array[i]
    return (kk(modified_array))

def partitioned_repeated_random(array):
     # Heuristic for partitioned solutions that repeatedly generates random partitions to minimize residue
    best = generate_random_partitioned_instance(array)
    for i in range(iterations):
        current = generate_random_partitioned_instance(array)
        if calculate_partitioned_residue(array, current) < calculate_partitioned_residue(array, best):
            best = current
    return calculate_partitioned_residue(array, best)

def find_partitioned_neighbor(sequence):
    # Generates a neighbor of a partitioned solution by reassigning an element to a different group
    size = len(sequence)
    rand_i, rand_j = random.sample(range(size), 2)
    neighbor = sequence.copy()
    neighbor[rand_i] = -sequence[rand_i]
    neighbor[rand_j] = random.choice([sequence[rand_j], -sequence[rand_j]])
    return neighbor

def partitioned_hill_climbing(array):
    # Similar to hill climbing but for partitioned solutions, aims to find a better grouping to minimize residue
    best = generate_random_partitioned_instance(array)
    for i in range(iterations):
        current_neighbor = find_partitioned_neighbor(best)
        if calculate_partitioned_residue(array, current_neighbor) < calculate_partitioned_residue(array, best):
            best = current_neighbor
    return calculate_partitioned_residue(array, best)

def partitioned_find_threshold(array, i, current, neighbor):
    nom = math.exp(-(calculate_partitioned_residue(array, neighbor) -
                   calculate_partitioned_residue(array, current)))
    denom = ((10**10) * (0.8 ** (i//300)))
    return nom/denom

def partitioned_simulated_annealing(array):
    # Simulated annealing adapted for partitioned solutions to avoid local minima
    current = generate_random_partitioned_instance(array)
    best = current.copy()
    for i in range(1, iterations+1):
        neighbor = find_partitioned_neighbor(current)
        if calculate_partitioned_residue(array, neighbor) < calculate_partitioned_residue(array, current):
            current = neighbor
        else:
            # calculate probability of annealing
            threshold = partitioned_find_threshold(array, i, current, neighbor)
            if random.random() < threshold:
                current = neighbor
        if calculate_partitioned_residue(array, current) < calculate_partitioned_residue(array, best):
            best = current
    return calculate_partitioned_residue(array, best)

def generate_test():
    # Generates a test array of 100 large random numbers
    size = 100
    array = []
    for i in range(size):
        array.append(random.randint(1, 10**12))
    return array

def main(flags):
    array = []
    if len(flags) > 2:
        with open(flags[2], "r") as file:
            array = [int(line.strip()) for line in file]

    algorithm_map = {
        '0': kk,
        '1': repeated_random,
        '2': hill_climbing,
        '3': simulated_annealing,
        '11': partitioned_repeated_random,
        '12': partitioned_hill_climbing,
        '13': partitioned_simulated_annealing,
        'dp': dynamic_programming_partition  
    }

    algorithm_code = flags[1]
    if algorithm_code in algorithm_map:
        start_time = time.perf_counter()
        result = algorithm_map[algorithm_code](array)
        end_time = time.perf_counter()
        print(f"Residue: {result}, Time: {end_time - start_time}")
    else:
        print("Invalid algorithm code provided.")

if __name__ == "__main__":
    main(sys.argv)

