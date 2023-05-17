## Common Time Complexities

### Constant Time - O(1)

Regardless of input size, your function will always have the same run time. If you can create an algorithm to solve a problem in O(1) time, you are usually at the optimal solution. Constant time is not always achievable in many situations (depending on the problem you solve). It also may not always be the quickest. It only means that the amount of operations your code must run will always remain constant, regardless of input size. Consider the following code:#assuming that items is a list of integers with a length >= 2
def constant_algo(items):
	result = items[0] + items[1] # constant operation(s) - O(1)
	return result