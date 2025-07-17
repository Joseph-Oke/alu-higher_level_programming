#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

# Case 1
my_rectangle = Rectangle(2, 4)
print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area()))

# Case 2
my_rectangle = Rectangle(2, 4)
print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.perimeter()))

# Case 3
my_rectangle = Rectangle(10, 10)
print("{} - {} => {} / {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area(), my_rectangle.perimeter()))

# Case 4
my_rectangle = Rectangle(10)
print("{} - {} => {} / {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area(), my_rectangle.perimeter()))

# Case 5
my_rectangle = Rectangle()
print("{} - {} => {} / {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area(), my_rectangle.perimeter()))
