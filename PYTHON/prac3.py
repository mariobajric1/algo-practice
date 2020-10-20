def findClosestValueInBst(tree, target):
    # Write your code here.
    # 	O(log(n)) time | O(1) space

    # 	return helper function with tree, target, and infinity parameter as default
    return findClosestValueInBstHelper(tree, target, float('inf'))

# define helper funciton with tree, target, and closest value


def findClosestValueInBstHelper(tree, target, closest):
    # 	current node = tree.value
    currentNode = tree
# 	while current node is true
    while currentNode is not None:
        # 		if the current node of the tree is less than the original closest
        if abs(target-closest) > abs(target - currentNode.value):
            # 			set the new value of the closest to the current node value
            closest = currentNode.value
# 		if the target value is less than the current node value
        if target < currentNode.value:
            # 			set the current node to the next left node
            currentNode = currentNode.left
# 		if the target value is greater than the current node
        elif target > currentNode.value:
            # 			set the current node to the next right value
            currentNode = currentNode.right
# 		otherwise the value is found
        else:
            break
# 	return ans / closest val
    return closest
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
