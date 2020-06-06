'''
https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
Given customers <- an array of pos ints representing a queue of customers. 
    The num is the time that customer takes to check out.
and n <- number of checkout tills.
Return the total time necessary for all customers to check out.
'''


def queue_time(customers, n):
    # If n is 1, just return the sum of the customers
    if n == 0:
        return sum(customers)
    # Initialize tills dict

    tills = {}
    for i in range(n):
        tills[i] = 0

    # Loop through customers
    while len(customers) > 0:
        # Find till with min value
        min_value = min(tills.values())
        min_key = [key for key, value in tills.items() if value ==
                   min_value][0]

        # Place customer in it
        tills[min_key] += customers[0]
        customers.remove(customers[0])

    # Return till with max sum
    return max(tills.values())


print(queue_time([5, 3, 4], 1))  # < - 12
print(queue_time([10, 2, 3, 3], 2))  # < - 10
print(queue_time([2, 3, 10], 2))  # < - 12
