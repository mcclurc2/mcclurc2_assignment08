# Name:Chase McClure, Duncan Ward Kaileb Strasser
# email:mcclurc2@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: march 28
# Course/Section: ADV APP DEV (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: this assignment is to see if we can construct a sql statment and get it to run in ecliple with having three other functions. our will to count how many coupons are free and then the third thing will print the function in a different class
# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this. this module taught us how to get eclipse to read a database sql code and to bring sql code from ssms
# Citations:canvas slides
# Anything else that's relevant: as of doing this no





#function.py
#function,py
def countCouponsFree(cursor):
    '''
    Counts the number of rows where the value under IsFree is false
    cursor: Cursor object containing the result set
    returns: number of rows with false under IsFree 
    '''
    rows = cursor.fetchall()
    false_count = len(rows)
    print("Number of rows with False under IsFree", false_count)
    # return the count of rows with false under IsFree
    return false_count
