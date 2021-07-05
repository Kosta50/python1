# print("*")
# print("*")
# print('This "is" a\' demo')
# for s in range(3):#This controls height
#     for n in range(2):#This controls width
#         print("*", end=" ")
#     print()

#Ask the user for width and height, and print a rectangle using that width and height

# x=input("Enter width")
# print(x)
#
# y=input("Enter height")
# print(y)

#Triangle

# y=10
# x=1
#
#
# for s in range(int(y)):
#     # x=x+1
#     for n in range(int(x)):
#         print("*", end=" ")
#     print()
#     x=x+1
# for n in range(int(x)):
#     print("*", end=" ")
# print()
#
# for i in range(int(y)-2):
#     print("*", end=" ")
#     for n in range(int(x) - 2):
#         print(" ", end=' ')
#     print("*", end=" ")
#     print()
# #
# for n in range(int(x)):
#     print("*", end=" ")
# print()

#Code a triangle as extra/think about how you would do it

# *
# * *
# * * *
# * * * *

# y=10
#
# for s in range(int(y)):
#     print(s)

# y=10
# for s in range(int(y)):
#     for n in range(int(s+1)):
#         print("*", end=" ")
#     print()

# y=10
# for s in range(int(y)):
#     for n in range(int(y-s)):
#         print("*", end=" ")
#     print()

#Reversed right triange, and upside down reversed right triange *releated to our hollow rectangles*
"""
* * * * * * * * * *
  * * * * * * * * *
    * * * * * * * *
      * * * * * * *
        * * * * * *
          * * * * *
            * * * *
              * * *
                * *
                  *
"""

" "


y=10
for s in range(int(y)):
    for n in range(int(s)):
        print(".", end=" ")
    for m in range(int(y-s)):
        print("*", end=" ")
    print()

print("Hi")