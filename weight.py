# weight converter program

weight = int(input(" enter the weight "))
unit=  input(  " is temperature in celsius or feranite (F/C)")

if unit == 'C':
         weight = weight * 2.2
         unit = 'gs'
elif unit == 'F':
        weight=weight /2.2
        unit = 'lbs'
else:
        print(f'{ unit } is wrong input')

print ( f"the weight is {weight} {unit}")
