'''Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''
grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
grades.sort(key = lambda tup: tup[1])
print(grades)

'''Write a lambda function to cube every element of a list.
Original list: [3,6,9,2] List after lambda function: [27,216,729,8]'''

cubed = lambda  lst: [e**3 for e in lst]

print (cubed([3,6,9,2]))


'''Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]'''

even_or_odd = lambda num: True if num%2 == 0 else False
even_or_odd_lst = [even_or_odd(e) for e in [3,6,9,2]]
print(even_or_odd_lst)