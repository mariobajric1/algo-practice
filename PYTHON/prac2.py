def isValidSubsequence(array, sequence):
    # Write your code here.
# 	o(n) time | o(1) space
#   While-loop solution

# 	set arr pointer
	arrI = 0
# 	set seq pointer
	seqI = 0
# 	while pointers are true to arr/seq lenghths
	while arrI < len(array) and seqI < len(sequence):
# 		if array val = seq val
		if array[arrI] == sequence[seqI]:
# 			increase seq pointer
			seqI += 1
# 		increase arr pointer every iteration
		arrI += 1
# 	return t/f if seq pointer made it to the end of the sequence
	return seqI == len(sequence)


def isValidSubsequence2(array, sequence):
        # Write your code here.
# 	for-loop solution
# 	set sequence pointer
	pointer = 0

# 	for num in array
	for value in array:
# 		if the pointer = len of the sequence,
		if pointer == len(sequence):
# 			 we're done so it breaks
			break
# 		if sequence value = array value
		if sequence[pointer] == value:
# 			increase pointer position 1
			pointer += 1
# 	returns if pointer makes it to the end of the sequence
	return pointer == len(sequence)

    pass



