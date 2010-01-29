5 + 5
5 + 2.3
3*2
3.0*2
3.5*10 + 7
3.5*(10 + 7)
# strings
"hello"
'hello there, "world"!'
print 'hello, there world'
print """This
is a triple-
quoted string that can
span multiple lines."""
print 6
#types
type(3)
type(3.0)
type("hi")
#operations
"hi"*3
"hi" + 5
"hi" + ", there"
"1" + "2"
"1" + 2
"1" + str(2)
str(2)
int("1") + 2
int("1")
2/3
10 % 3
11 % 3
12 % 3
#variables
radius = 2
radius = 1.5*4
circum = 2*radius*3.141592653589793
print circum
radius = 4
print circum
another_variable = radius
print radius
print another_variable
radius = 10
print radius
print another_variable
print locals()
a = "some string"
print locals()
3.15*10 + 7
print locals()
print globals()
del circum
del a
print locals()
print bogus
#dynamictyping
type(radius)
copy_of_radius = radius
radius="the distance from the center of a circle to a point on the circle"
type(radius)
type(copy_of_radius)
#functions
def calc_circumference(radius):
    circumference =  2*radius*3.141592653589793
    return circumference

type(calc_circumference)
type(circumference)
calc_circumference(2)
calc_circumference(4)
x = calc_circumference(4)
type(x)
#scope
locals()
globals()
def calc_circumference_verbose(radius):
    print locals()
    circumference =  2*radius*3.141592653589793
    print locals()
    return circumference
locals()
calc_circumference_verbose()
#multiargs
def square_prism_volume(square_length, height):
    """Returns the volume of a rectangular prism with two sides that have a
    length of `square_length`. The length in the third dimension is `height`."""
    return square_length*square_length*height
help(square_prism_volume)
square_prism_volume(4, 10)
square_prism_volume(10, 4)
square_prism_volume(height=10, square_length=4)
def prism_volume(x, y, z):
    """Returns the volume of a rectangular prism with side lengths `x`, `y`, and `z`"""
    print "x =", x, ", y =", y, ", z =", z
    return x*y*z
prism_volume(1,2,3)
prism_volume(1,z=2,y=3)
prism_volume(z=2,y=3,1)
prism_volume('length', 'width', 'height')
prism_volume('length', 2, 3)
#flow
def checker(x, y):
    if x > y:
        print x, 'is bigger than', y
        return x
    else:
        print x, 'is not bigger than', y
        return y
bigger = checker(4, 6)
print(bigger)

def better_checker(x, y):
    if x > y:
        print x, 'is bigger than', y
        return x
    elif x == y:
        print x, 'is equal to than', y
        return y
    else:
        print x, 'is smaller than', y
        return y
better_checker(4, 4)
better_checker(4, 4.5)
better_checker(y=4, x=1)
# lists
True
False
1 > 2
bool(1)
bool(0)
bool("False")
bool("0")
bool("")
None
a = list()
a
len(a)
a.append(1)
a
a = range(10)
a
a = range(1,10)
a = [3,7, 2]
a.sort()
print a
a = range(10)
a.reverse()
a
dir(a)
help(a)
help(a.count)
[0]*10
[0]*10 + [1]*10
[0]*[1]
[0]+[1]
a.insert(0,11)
a
a.pop()
a
#listindexing
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x[0]
x[1]
x[0:5]
x[1:5]
print x
x[0] = 1.3
y = ["a", 5.2, 3]
a, b, c = y
a, b = 10.1, 4
#iteration
for i in x:
    print i
for i in range(10):
    print i
    print calc_circumference(i)
for abc in "hello, there":
	print abc
from_string = list("here is a string")
print abc
def calc_num_attachment_points(n):
    return 2*n - 3
for i in range(3, 101):
    num_attachments = calc_num_attachment_points(i)
    print i, num_attachments
