### Quadratic Time - O(n^2)
def quadratic_algo(items):
	for i in items: # Linear Time operation O(n)
		for j in items: # Linear time operation O(n)
			print(f'Outer Loop:{i} - Inner Loop: {j}'
In quadratic time, the amount of operations our code must perform will grow in direct proportion to the size of our input squared. In general, we hope to avoid quadratic time if at all possible. You will typically encounter quadratic time when you have nested loops. **If you have any operation that occurs inside of another operation, those time complexities must be multiplied to find your end result.**