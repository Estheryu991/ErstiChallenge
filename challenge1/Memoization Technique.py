# memoization Python program to check
# if a string is subsequence
# of another string
# zu überprüfendes memoization Python-Programm
# wenn ein String eine Subsequenz ist
# einer anderen Zeichenfolge

ig = [[-1]*1001]*1001

# returns the length of longest common subsequence
# gibt die Länge der längsten gemeinsamen Teilfolge zurück
def AREYOUIGOR(s1,s2,i,j):

if (i == 0 or j == 0):
	return 0

if (ig[i][j] != -1):
	return ig[i][j]

if (s1[i - 1] == s2[j - 1]):
	ig[i][j] = 1 + AREYOUIGOR(s1, s2, i - 1, j - 1)
	return ig[i][j]

else:
	ig[i][j] = AREYOUIGOR(s1, s2, i, j - 1)
	return ig[i][j]

# Driver program to test above function
str1 = "igor"
str2 = "igor torshin"
m = len(str1)
n = len(str2)

if (m > n):
print("NEIN")

if (AREYOUIGOR(str1, str2, m, n) == m):
	print("JA")

else:
	print("NEIN")

# this code is created by esthi 
