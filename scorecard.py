# Program to prompt for a score between 0.0 and 1.0
# If the score is out of range print error. If the score is between 0.0 and 0.1, print the grade using following:
# >=0.9 A, >=0.8 B, >=0.7 C, >=0.6 D, <0.6 F

ss = input('Enter Score between 0.0 and 1.0: ')
fs = float(ss)
if fs > 1.0 :
    print('Error')
elif fs < 0.0 :
    print('Error')
elif fs >= 0.9 :
    print('Grade: A')
elif fs >= 0.8 :
    print('Grade: B')
elif fs >= 0.7 :
    print('Grade: C')
elif fs >= 0.6 :
    print('Grade: D')
elif fs < 0.6 :
    print('Grade: F')
quit()
