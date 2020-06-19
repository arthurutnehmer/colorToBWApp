#! /usr/bin/python
# Exercise No.  01
# File Name:    hw8project1.py
# Programmer:   Arthur Utnehmer
# Date: April 6, 2020
#
# Problem Statement: (what you want the code to do)
# The Fibonacci sequence starts 1, 1, 2, 3, 5, 8, . . .. Each number in the se­ quence (after the first two)
# is the sum of the previous two. Write a pro­ gram that computes and outputs the nth Fibonacci number,
# where n is a value entered by the user.
#
# Overall Plan (step-by-step,howyou want the code to make it happen):
# 1. Get the number that represents which Fibonacci number to stop at.
# 2. Loop by adding the previouse two to get the next number.

def main():
    x = int(input("This is a Fibonacci sequence term finder for 1, 1, 2, 3, 5, 8, . . .. Enter the N-th term to find its value."))

    nthTerm = x;
    firstTerm = 1;
    secondTerm = 0;
    Nterm = 1;

    while(x>1):
        Nterm = firstTerm + secondTerm;
        secondTerm = firstTerm;
        firstTerm = Nterm;
        x = x-1;

    print("The term with index ", nthTerm, "Term is:", Nterm)



main()
