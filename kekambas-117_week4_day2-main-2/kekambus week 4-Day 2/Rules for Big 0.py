Rules for Big 0
# Time complexity == O(n * m)
def nested_params(n,m):
	for num in n: # linear operation - O(n)
		for i in m: #linear operation - O(m)
			print(num+i) # constant operation - negligible

# Time Complexity == O(n + m) 
def stacked_loops(n,m):
	for num in n: #linear operation - O(n)
		print(num)
	for i in m: # linear Operation - O(m)
		print(i)