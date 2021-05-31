'''ASSIGNMENT QUESTIONS:
1. Print "Learning DL" if age is greater than 15 but less than 18, print "DL" if age is above 18, and print "Not eligible" if age is less than or equal to 15.
2. Print pass if marks greater than 40% and print fail otherwise.
3. Print Grade A if marks > 90%, Grade B if marks > 80%, and Grade C if marks >70%
4. Print Grade A if marks > 90%, Grade B if marks > 80%, and Grade C if marks >70% and print D if marks>60%
5. Print Grade A if marks > 90%, Grade B if marks > 80% and marks<60%, Grade C if marks<60% and marks>40%
6. Print Grade A if marks > 90%, Grade B if marks > 80% and marks<60%, Grade C if marks<60% and marks>40% else print fail.
'''
#answer of Q1
#by if else
age = int(input("what is your age"))
if age > 15 and age < 18:
  print("Learning DL")
elif age>18:
  print("DL")
elif age <= 15:
  print("Not eligible")
#by ternery
age>15 and age<18 ? print("Learning DL")
age>18 ? print("DL")
age<= 15 ? print("Not eligible")
#answer of Q2
