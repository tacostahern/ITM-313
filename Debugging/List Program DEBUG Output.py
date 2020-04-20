Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ======
Enter current value: 1
Enter current value: 1
Enter current value: 1
Enter current value: 1
Enter current value: 1
Resistance 	 Current 	 Power

16 		 1 		 81 

27 		 1 		 81 

39 		 1 		 81 

56 		 1 		 81 

81 		 1 		 81 

Total: 		 5 		 405
>>> 
======= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ======
Enter current value: 2
Enter current value: 3
Enter current value: 4
Enter current value: 5
Enter current value: 6
Resistance 	 Current 	 Power

16 		 6 		 2916 

27 		 6 		 2916 

39 		 6 		 2916 

56 		 6 		 2916 

81 		 6 		 2916 

Total: 		 30 		 14580
>>> 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 1
Enter current value: 2
Enter current value: 3
Enter current value: 4
Enter current value: 5
Resistance 	 Current 	 Power

16 		 1 		 16 

27 		 2 		 108 

39 		 3 		 351 

56 		 4 		 896 

81 		 5 		 2025 

Total: 		 25 		 10125
>>> 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 1
Enter current value: 2
Enter current value: 3
Enter current value: 4
Enter current value: 5
Resistance 	 Current 	 Power

16 		 1 		 16 

27 		 2 		 108 

39 		 3 		 351 

56 		 4 		 896 

81 		 5 		 2025 

Total: 		 15 		 3396
>>> 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 1
Traceback (most recent call last):
  File "C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py", line 9, in <module>
    powerSum.append(resistance[i] * current**2)
NameError: name 'current' is not defined
2
>>> 
>>> 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 1
Enter current value: 2
Enter current value: 3
Enter current value: 4
Enter current value: 5
Resistance 	 Current 	 Power

Traceback (most recent call last):
  File "C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py", line 16, in <module>
    print(resistance[x],"\t\t", currentList[x],"\t\t", powerList[x],"\n")
NameError: name 'currentList' is not defined
>>> 

========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
>>> 
Enter current value: 1
Enter current value: 2
Enter current value: 3
Enter current value: 4
Enter current value: 5
Resistance 	 Current 	 Power

16 		 1 		 16 

Traceback (most recent call last):
  File "C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py", line 17, in <module>
    currentSum += currentSum[x];
TypeError: 'int' object is not iterable
>>> 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 1
Enter current value: 2
Enter current value: 3
Enter current value: 4
Enter current value: 5
Resistance 	 Current 	 Power

16 		 1 		 16 

27 		 2 		 108 

39 		 3 		 351 

56 		 4 		 896 

81 		 5 		 2025 

Total: 		 15 		 3396
>>> 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 1
Enter current value: 2
Enter current value: 3
Enter current value: 4
Enter current value: 5
Resistance 	 Current 	 Power

16 		 1 		 16 

Traceback (most recent call last):
  File "C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py", line 18, in <module>
    currentSum += currentSum[x];
TypeError: 'int' object is not subscriptable
>>> 

========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
>>> 
Enter current value: 1
Enter current value: 2
Enter current value: 3
Enter current value: 4
Enter current value: 5
Resistance 	 Current 	 Power

16 		 1 		 16 

27 		 2 		 108 

39 		 3 		 351 

56 		 4 		 896 

81 		 5 		 2025 

Total: 		 15 		 3396
>>> 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 1
Traceback (most recent call last):
  File "C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py", line 9, in <module>
    current[i] = ((eval(input('Enter current value: '))))
IndexError: list assignment index out of range
>>> 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 1
Enter current value: 2
Enter current value: 3
Enter current value: 4
Enter current value: 5
Resistance 	 Current 	 Power

16 		 1 		 16 

27 		 2 		 108 

39 		 3 		 351 

56 		 4 		 896 

81 		 5 		 2025 

Total: 		 15 		 3396
>>> 
========= RESTART: C:\Users\tacos\Documents\ITM-313\Debugging\List Program DEBUG.py ========
Enter current value: 6
Enter current value: 7
Enter current value: 8
Enter current value: 9
Enter current value: 10
Resistance 	 Current 	 Power

16 		 6 		 576 

27 		 7 		 1323 

39 		 8 		 2496 

56 		 9 		 4536 

81 		 10 		 8100 

Total: 		 40 		 17031
>>> 