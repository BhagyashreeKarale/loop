#Difference between while loop and for loop in python?.
# The for statement iterates through a collection or iterable object or generator function.

# The while statement simply loops until a condition is False.

# It isn't preference. It's a question of what your data structures are.

# Often, we represent the values we want to process as a range (an actual list), or xrange (which generates the values) (Edit: In Python 3, range is now a generator and behaves like the old xrange function. xrange has been removed from Python 3). This gives us a data structure tailor-made for the for statement.

# Generally, however, we have a ready-made collection: a set, tuple, list, map or even a string is already an iterable collection, so we simply use a for loop.

# In a few cases, we might want some functional-programming processing done for us, in which case we can apply that transformation as part of iteration. The sorted and enumerate functions apply a transformation on an iterable that fits naturally with the for statement.

# If you don't have a tidy data structure to iterate through, or you don't have a generator function that drives your processing, you must use while.







#For loop	
# Command	       The structure of for loop is –for(initial condition; number of iterations){//body of the loop }	
# Iterations	   Iterates for a preset number of times.	
# Condition	       In the absence of a condition, the loop iterates for an infinite number of times till it reaches break command.	
# Initialization   Initialization in for loop is done only once when the program starts.	
# Use	           Used to obtain the result only when the number of iterations is known.	

#While loop
# Command	        Structure of while loop is-While(condition){statements;//body}
# Iterations	    Iterates till a condition is met.
# Condition	        In the absence of a condition, while loop shows an error.
# Initialization	Initialization is done every time the loop is iterated.
# Use	            Used to satisfy the condition when the number of iterations is unknown.
