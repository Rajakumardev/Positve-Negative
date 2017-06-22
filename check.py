# Positve-Negative
"""check whether a number is positive or negative or zero its very simple"""
def chknum(x):
   if x>0:
   print ("Positive Number")
elif x<0:
   print ("Negative Number")
else:
   print("Zero")
   
x=int(raw_input("Enter the Number :" ))
chknum(x)
