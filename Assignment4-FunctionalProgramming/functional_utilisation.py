import functools, operator, itertools

def generator_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


def main():
    even = generator_even(100)   # Generator of even nos. till 100
    print(next(even))
    print(next(even))
    print(next(even))
    print(next(even))

    text = "some text to test built-in function"
    print(text.upper())         # Utilizing builtin function upper()

    myList = [23,45,12,67,34,21,90]
    print(max(myList))              # Utilizing builtin function max() to find max amongst the elements of list
    print(min(myList))              # Utilizing builtin function min() to find min amongst the elements of list

    for i in enumerate(myList):                         # Using enumerate()
        print(f"Element at {i[0]} index is {i[1]} ")


    # Using functools and operators

    print("Sum of all elements=",functools.reduce(operator.add, myList, 0))  
    print("Multiplication of all elements=",functools.reduce(operator.mul, myList, 1))  

    # Using itertools
    print(list(itertools.combinations(myList,2)))    # Returns all possible combinations of 2nd no. of elements
    print(list(itertools.permutations([1,2,3])))  # Returns permutations

main()