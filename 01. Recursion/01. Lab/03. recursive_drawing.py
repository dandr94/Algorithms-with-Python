"""
Write a program that draws the figure below depending on n.
Example if n == 5:

*****
****
***
**
*
#
##
###
####
#####

"""


def draw(n: int) -> None:
    if n == 0:
        return

    print('*' * n)

    draw(n - 1)

    print('#' * n)


draw(5)

# Test solution at:
# https://judge.softuni.org/Contests/Practice/Index/3459#2
