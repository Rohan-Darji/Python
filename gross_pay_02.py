# Program to prompt the user for hours and rate per hour using the raw input to compute gross pay.
# Pay the hourly rate for hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.

sh = input('Enter the number of hours: ')
sr = input('Enter te rate per hour: ')
fh = float(sh)
fr = float(sr)
if fh<=40 :
    pay = fh * fr
    print('Pay:',pay)
elif fh>40 :
    og = fh * fr
    otp = (fh-40.0) * (fr*1.5)
    pay = og + otp
    print('Pay:',pay)
quit()
