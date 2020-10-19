def isValidSubsequence(array, sequence):
    # Write your code here.
# 	o(n) time | o(1) space
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

    pass
