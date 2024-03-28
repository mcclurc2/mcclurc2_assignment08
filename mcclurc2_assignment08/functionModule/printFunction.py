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



def whatTypeCoupon(cursor):
    '''
    to find what type coupon is popping up. hopes to find BOGO
    return: BOGO from from the rows
    ''' 
    rows = cursor.fetchall()

    bogo_coupon_codes = [row[1] for row in rows if 'BOGO' in row[2]]

    return bogo_coupon_codes
    print(bogo_coupon_codes)
