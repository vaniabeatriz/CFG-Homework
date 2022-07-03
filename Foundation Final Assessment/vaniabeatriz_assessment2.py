'''

Question 8 - MySQL

SELECT customer_id,  MAX(purch_amt)
FROM ORDERS
WHERE customer_id BETWEEN 3002 AND 3007
GROUP BY customer_id
HAVING MAX(purch_amt) > 1000;

'''


def squared_number_list(array):
    squared_numbers = []
    for i in array:
        squared_numbers.append(i * i)
        squared_numbers.sort()
    return squared_numbers


result = squared_number_list([1, 2, 3, 4, 5, 6, 7])

print(result)



def check_target(array, target):
    for idx_i, i in enumerate(array):
        for idx_j, j in enumerate(array):
            if idx_i is not idx_j and i + j == target:
                return [i, j]
    return []


result = check_target([2, 4, 5, 6, 9, 11, -10, ], 7)

print(result)

