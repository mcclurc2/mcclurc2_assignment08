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

#main.py



import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=GroceryStoreSimulator;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()

cursor.execute('SELECT dbo.tDiscountType.IsFree, dbo.tCoupon.Coupon, dbo.tDiscountType.DiscountType\
                FROM  dbo.tCoupon INNER JOIN\
                dbo.tCouponDetail ON dbo.tCoupon.CouponID = dbo.tCouponDetail.CouponID INNER JOIN\
                dbo.tCouponSource ON dbo.tCoupon.CouponSourceID = dbo.tCouponSource.CouponSourceID INNER JOIN\
                dbo.tDiscountType ON dbo.tCouponDetail.DiscountTypeID = dbo.tDiscountType.DiscountTypeID')
for row in cursor:
    print(row[0])
    print(row[1])
    print(row[2])
    

