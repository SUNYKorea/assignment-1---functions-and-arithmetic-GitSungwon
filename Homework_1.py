# Name:Seongwon Woo
# SBUID: 112978020
import math

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 


# After getting variables in the fahrenheit2celsius, I created the formula in it.
# I forgot to put 'return' at the end of the method, but I eventually put it in. And then, 
# I made a code using if-elif-else material to divide the clothes by temperature. There is no
# print function in the main method, so I printed in the method what_to_wear.
def fahrenheit2celsius(fahrenheit): 
   C = (5 / 9) * (float(fahrenheit) - 32)
   return C


def what_to_wear(celsius):
   if float(celsius) <= -10:
       print("Puffy jacket")
   elif -10 < float(celsius) <= 0:
       print("Scarf")
   elif 0 < float(celsius) <= 10:
       print("Sweater")
   elif 10 < float(celsius) <= 20:
       print("Light jacket")
   else:
       print("T-shirt")

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

# I used the formula to type all the variables. I grouped this into tri and 
# prepared for when tri is - in an if-else statement to express the absolute value.
def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):    
    tri = ((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2))/2
    abstri = abs(tri) / 2
    return abstri

# I substituted four variables into the formula.
def euclidean_distance(x1, y1, x2, y2):
    return (((x1-x2)**2)+(y1-y2)**2)**(1/2)

#Using the above euclidean_distance method, I created a format to find the perimeter. 
def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = euclidean_distance(x1, y1, x2, y2)
    s2 = euclidean_distance(x2, y2, x3, y3)
    s3 = euclidean_distance(x3, y3, x1, y1)
    return s1 +s2 +s3


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

# I found the formula in the internet because changing to radian is not in the pdf file.
# And then, I use it in the method with importing math in order to use pi.
def deg2rad(deg):
    return deg * (math.pi / 180)

# The following formula was formed using the above deg2rad method. Also, I used tan by importing math.
def apothem(number_sides, length_side):
   return length_side / (2 * math.tan(deg2rad(180/number_sides)))

# The following formula was formed using the above apothem method.
def polygon_area(number_sides, length_side):
   return (number_sides * length_side * apothem(number_sides,length_side)) / 2


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# # Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# # # Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# # Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the apo is : " + str(apothem(number_sides, length_side)))
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))


