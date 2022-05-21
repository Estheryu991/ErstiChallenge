# Python Implementation of the approach
import itertools

def Sub_Sequences(STR):
	epsc = []
	for l in range(1, len(STR)+1):
		epsc.append(list(itertools.combinations(STR, l)))
	for c in epsc:
		for t in c:
			print (''.join(t), end =' ')

# Testing with driver code
if __name__ == '__main__':
	Sub_Sequences('igor')
	
	
# by esthi 
# result: rogi rog roi ro rgi rg ri r ogi og oi o gi g i
