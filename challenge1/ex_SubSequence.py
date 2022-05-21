def SubSequence(STR, subSTR=""):
	"""
	function:
		To print all subsequences of string
		concept:
			Pick and Don’t Pick
		variables:
			STR = string
			subSTR = to store subsequence
	"""
	if len(STR) == 0:
		print(subSTR, end=" ")
		return

	# we add adding 1st character in string
	SubSequence(STR[:-1], subSTR + STR[-1])
	"""
	Not adding first character of the string
	because the concept of subsequence either
	character will present or not
	"""
	SubSequence(STR[:-1], subSTR)
	return


def main():
	"""
	main function to drive code
	"""
	STR = "igor"
	SubSequence(STR)


if __name__ == "__main__":
	main()

# by esthi
# output>>> i g o r ig io ir go gr or igo igr ior gor igor
