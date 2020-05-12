# Program to prompt the user for hours and rate per hour using the raw input to compute the gross pay.
# Award time and a half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of time and a half in the function call computepay() and use the function to do the computation. Funtion should return a value.

def computepay(fh,fr):
    reg = fh * fr
    otp = (fh-40) * (fr*1.5)
    pay = reg + otp
    return pay
try:
    sh = input('Enter hours: ')
    sr = input('Enter rate per hour: ')
    fh = float(sh)
    fr = float(sr)
    if fh>40:
        pay = computepay(fh,fr)
    else:
        pay = fh * fr
    print ('Pay:',pay)
except:
    print('Please enter numeric input')
quit()
