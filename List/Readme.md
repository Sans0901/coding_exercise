List :

In Python, a list is a built-in data type used to store a collection of values. Lists are mutable, meaning that you can change their contents by adding, removing, or modifying elements.

Here's an example of how to create a list in Python:

my_list = [1, 2, 3, 4, 5]
This creates a list of integers with the values 1 through 5.

You can access individual elements of a list by their index, which starts at 0. For example:
print(my_list[0]) # prints 1
print(my_list[2]) # prints 3

You can also modify the values of elements in a list:
my_list[1] = 10
print(my_list) # prints [1, 10, 3, 4, 5]

To add an element to the end of a list, you can use the append() method:
my_list.append(6)
print(my_list) # prints [1, 10, 3, 4, 5, 6]

To remove an element from a list, you can use the remove() method:
my_list.remove(3)
print(my_list) # prints [1, 10, 4, 5, 6]




	  n = int
	  n1 = str(n)                                #converted into string
        n2 = n1[::-1]					   #reversed string
        number_list = list(str(n2))			   #converted into list
        number_list.sort(reverse=True)             #sorted list of string
        n3 = int(''.join(map(str, number_list)))   #converted into int 