def nodeDepths(root, depth=0):
	# recursive method
# 	o(n) t \ o(h) s
	# 	handle base case
	if root is None:
		return 0

# 	return the current depth + recursive func on each branch
	return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)



    pass


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None







def nodeDepths2(root):
	# stack method
	
# 	o(n) t \ o(h) s
	
	
# 	init running sum
	sumOfDepths = 0
	
# 	initialize stack at root node
	stack = [{'node': root, 'depth': 0}]
	
# 	loop over stack while there are things to do
	while len(stack) > 0:
		
# 		pop the top of the stack
		nodeInfo = stack.pop()
		
# 		node = node and current depth 
		node, depth = nodeInfo['node'], nodeInfo['depth']
# 		if there is no node, continue
		if node is None:
			continue
# 		add node depth to total depth
		sumOfDepths += depth
# 		add the next two node branches and increase their depth
		stack.append({'node': node.left, 'depth': depth + 1})
		stack.append({'node': node.right, 'depth': depth + 1})
	return sumOfDepths
	
	
	
	
    pass


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
