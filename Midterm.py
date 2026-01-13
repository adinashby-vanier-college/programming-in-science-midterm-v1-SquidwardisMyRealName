import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area_of_circle = round(math.pi * radius ** 2, 2) 
    
    return area_of_circle

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    total_shape = ""

    for row_number in range(1, n + 1):
        if n < 4:
            return "The triangle height should be at least 4."
        else:
            total_shape += "*"

        for space_number in range(1, row_number - 1):
            if row_number != n: 
                total_shape += " "
            
        if row_number == 1 or row_number == n:
            total_shape += ""    
        else: 
            total_shape += "*"

        if row_number == n:
            total_shape += "*" * (n - 1)
        else:
            total_shape += ""  

        total_shape += "\n"
        
    return total_shape.rstrip()

            

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    total_shape = ""

    for row_number in range(1, n + 1):
        if n < 3:
            return "The pyramid height should be at least 3."

        else:
            for space_number in range(1, row_number):
                total_shape += " "

            for star_index in range(1,  2 * n - 2 * row_number + 2):
                total_shape += "*"
           
            total_shape += "\n"
   
    return total_shape.rstrip()
 




# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()
