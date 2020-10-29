# This is the class of the input root. Do not edit it.

# define BTS class
class BinaryTree:
# 	initialize the node and left/right nodes


def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# solution funciton


def branchSums(root):
# 	ans starts as an empty bracket
	sums = []
# 	call recursive function
	calculateBranchSums(root, 0, sums)

# 	return array of sums
	return sums

    pass

# define recursive function that takes in a node, a running sum of that branch, and the array of sums
# O(n) T/S


def calculateBranchSums(node, runningSum, sums):
	
# 	if the node is null.. end
	if node is None:
		return
	
# 	add current node value to the running sum
	newRunningSum = runningSum + node.value
	
# 	if you are at a leaf node
	if node.left is None and node.right is None:
# 		add the running sum to the sums array of answers
		sums.append(newRunningSum)
		return
# 	call recursive function on left / right nodes
	calculateBranchSums(node.left, newRunningSum,sums)
	calculateBranchSums(node.right, newRunningSum,sums)

		
