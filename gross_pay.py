# Program to prompt the user for hours and rate per hour using the raw input to compute gross pay.

hours = input('Enter the number of hours: ')
rate = input('Enter the rate per hour: ')
pay = float(hours) * float(rate)
print('Total gross pay:',pay)
quit()
