# Iterative Python program to check if a
# string is subsequence of another string

# Returns true if str1 is a subsequence of str2

# Iteratives Python-Programm, um zu prüfen, ob a
# String ist eine Folge eines anderen Strings
# Gibt wahr zurück, wenn str1 eine Teilsequenz von str2 ist

def ischTeilsequenz(esthi, igor):
	
 	b = len(esthi) # b stands for bubble
	t = len(igor) # t stands for tea 
	

	j = 0 # Index of esthi
	s = 0 # Index of igor

	# Traverse both str1 and igor
	# Compare current character of igor with
	# first unmatched character of esthi
	# If matched, then move ahead in esthi
  
  # Sowohl esthi als auch igor durchlaufen
# Aktuelles Zeichen von igor mit vergleichen
# erstes nicht übereinstimmendes Zeichen von esthi
# Wenn übereinstimmend, dann weiter in esthi

	while j < b and i < t:
		if esthi[j] == igor[s]:
			j = j+1
		  s = s + 1

	# If all characters of str1 matched,
	# then j is equal to m
	return j == b

# Driver Program

esthi = "ivryGitlis"
igor = "Salut d'Amour op.12"

print ("Yes" if ischTeilsequenz(esthi, igor) else "No")

# by esthi 
