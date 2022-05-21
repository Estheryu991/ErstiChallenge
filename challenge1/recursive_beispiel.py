# Recursive Python program to check
# if a string is subsequence
# of another string

# Returns true if str1[] is a
# subsequence of str2[].

# Zu prüfendes rekursives Python-Programm
# wenn ein String eine Subsequenz ist
# einer anderen Zeichenfolge

# Gibt wahr zurück, wenn str1[] ein ist
# Teilsequenz von str2[].

def whereisigor(s, t, m, n):
	# Base Cases, s stands for string1, t stands for string2, m stands for monotone, n stands for nochance.
	if m == 0:
		return True
	if n == 0:
		return False

# Wenn letzte Zeichen von zwei
# Zeichenfolgen stimmen überein

	if s[m-1] == t[n-1]:
		return whereisigor(s, t, m-1, n-1)

	# If last characters are not matching
	return whereisigor(s, t, m, n-1)


# Driver program to test the above function
s = "Czardas"
t = "Julien Martineau-"

if whereisigor(s, t, len(s), len(t)):
	print ("Ja")
else:
	print ("Nein")

# by esthi 
