"""
from hackerrank

Given: non-empty arr of distinct integers
And a target int

Find all triplets in arr that sum up to target sum

Return a 2D arr of all these triplets
With each inner arr sorted in ascending order
And triplets ordered in ascending order by first triplet el
secondary: smallest 2nd el
tertiary: smallest third el

If no triplets, return empty arr

Example:
[12, 3, 1, 2, -6, 5, -8, 6], 0
Return [[-8,2,6], [-8, 3, 5], [-6,1,5]]
"""
# Generate all triplets
# Check to see if their sum is target
# If so, add to output_arr
# Sort output arr
from itertools import combinations


def threeNumberSum(arr, target):
    # Try out doubles, to see if it's faster:
    double_combos = combinations(arr, 2)
    doubles = [combo for combo in double_combos]
    # print(doubles)

    # Generate lookup table to store what is needed to reach target for each double:
    lookup = {}
    for double in doubles:
        # print(double[0] + double[1])

        if (double[0] + double[1]) not in lookup:
            lookup[double[0] + double[1]] = [double]
        else:
            lookup[double[0] + double[1]].append(double)

    # print(lookup)

    # Loop thru arr to see if the target - num exists in the dictionary. If so, make a triplet with each of the values
    # for that number with num.
    my_triplets = []
    for num in arr:
        if (target - num) in lookup:
            for double in lookup[target - num]:
                if num != double[0] and num != double[1]:
                    triplet = [num, double[0], double[1]]
                    triplet.sort()
                    if triplet not in my_triplets:
                        my_triplets.append(triplet)
    my_triplets.sort()
    print(my_triplets)

    # Generate triplets:
    '''
    triplets = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                # print("i, j, k: " + str(arr[i]) +
                #      " " + str(arr[j]) + " " + str(arr[k]))
                triplets.append([arr[i], arr[j], arr[k]])
    # print(triplets)
    print("triplets length: " + str(len(triplets)))
    '''
    '''
    # Tryint out combinations():
    #print(str(combinations(arr, 3)))
    # print(help(combinations))
    combos = combinations(arr, 3)
    combos_arr = [list(i) for i in combos]
    # print([list(i) for i in combos])
    print("Combos length: " + str(len(combos_arr)))
    
    '''
    # This way uses combinations:
    combos = combinations(arr, 3)
    triplets = [list(combo) for combo in combos]

    # Find winning triplets
    totals = []
    winners = []
    for triplet in triplets:
        total = triplet[0] + triplet[1] + triplet[2]
        totals.append(total)
        if total == target:
            print("Found one!")
            # Sort triplet
            triplet.sort()
            winners.append(triplet)
    # print(totals)
    print(winners)

    # sort winners
    winners.sort()
    print(winners)


threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
