
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


def twoNumberSum2(array, targetSum):
    # Write your code here.
	# hash table method
	# o(n) time | o(n) space

# 	create hash table
	nums = {}
# 	for currentnum in array
	for currentNum in array:
# 		set potential match to: target - currentNum
		potentialMatch = targetSum - currentNum
# 		if that potential number is in our hash
		if potentialMatch in nums:
# 			return ans, aka potmatch & currentnum
			return [potentialMatch, currentNum]
# 		otherwse push the current num to the hash table incase it is a match for a later number in array
		else:
			nums[currentNum] = True
# 	no solution
	return []

    pass






def twoNumberSum3(array, targetSum):
    # Write your code here.
	# double for-loop solution
# 	too long and too much space
	
	for i in range(len(array) - 1):
		firstNum = array[i]
		for j in range(i + 1, len(array)):
			secondNum = array[j]
			if firstNum + secondNum == targetSum:
				return [firstNum, secondNum]
	return []

    pass
