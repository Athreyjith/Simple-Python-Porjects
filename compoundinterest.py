from sqlalchemy.sql.operators import truediv

interest_rate = 0
principle=0
time= 0
extra_amount=0
#
# while principle <= 0:
#     principle= float(input(" enter the principle amount "))
#     if principle <= 0:
#         print(" the principal amount cannot be less than zero ")
#
# while interest_rate <= 0:
#     interest_rate= float(input(" enter the interest rate "))
#     if interest_rate <= 0:
#         print(" the interest rate cannot be less than zero ")
#
# while time <= 0:
#     time= float(input(" enter the time in  year"))
#     if time <= 0:
#         print(" the time cannot be less than a day ")


# ci=  principle * pow(( 1 + interest_rate/100 ),time )
# print(f" the compound interest is {ci}")
# extra_amount = ci -principle
# print(f" the extra_amount due to interest is {extra_amount}")


while True:
    principle= float(input(" enter the principle amount "))
    if principle <= 0:
        print(" the principle amount cannot be less than zero ")
    else :
        break

while True:
    interest_rate= float(input(" enter the interest rate "))
    if interest_rate <= 0:
        print(" the interest rate cannot be less than zero ")
    else :
        break

while True:
    time= float(input(" enter the time in  year"))
    if time <= 0:
        print(" the time cannot be less than a day ")
    else :
        break
ci=  principle * pow(( 1 + interest_rate/100 ),time )
print(f" the compound interest is {ci:.2f}")
extra_amount = ci -principle
print(f" the extra_amount due to interest is {extra_amount:.2f}")
