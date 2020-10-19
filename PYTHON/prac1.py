
# find  2 num in the input array that sum up to the target input


def twoNumberSum(array, targetSum):
    # Write your code here.
    # 	optimized sort from least to greatest
    array.sort()
# 	sets left array pointer
    leftP = 0
# 	sets right array pointer
    rightP = (len(array) - 1)
# 		while the left pointer is less than the right pointer
    while leftP < rightP:
        # 		set the current sum of the pointers
        currentSum = array[leftP] + array[rightP]
# 		if the current sum equals the target
        if currentSum == targetSum:
            # 			return the pair answer
            return [array[leftP], array[rightP]]
# 		if the sum is greater than the target,
        elif currentSum > targetSum:
            # 			reduce the right pointer one position
            rightP -= 1
# 		if the sume is less than the target
        elif currentSum < targetSum:
            # 			increase the left pointer one position
            leftP += 1
# 	return nothing because array is sorted and there is no answer in given array
    return []


twoNumberSum([1, 2, 3], 5)
