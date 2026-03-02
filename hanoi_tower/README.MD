Tower of Hanoi Solver



A Python implementation of the classic Tower of Hanoi puzzle using recursion.



Description



This program solves the Tower of Hanoi problem for any positive number of disks.

It returns a formatted string containing:



The initial configuration



Every intermediate move



The final configuration



Each state is displayed on a new line, with rods represented as lists of integers.



Function

hanoi\_solver(n: int) -> str



n: Number of disks



Returns: A string representing all moves required to solve the puzzle



Complexity



The solution follows the recursive strategy and performs:



2ⁿ − 1 moves



Time Complexity: O(2ⁿ)

