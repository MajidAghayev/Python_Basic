#text = input("ala enter text :")
#def is_Palindrome(text):

	#if(text.lower().replace(" ","") == text[::-1].lower().replace(" ","")):
		#return True
	#else:
		#return False

#print(is_Palindrome(text))


def is_palindrome(text):
  text = text.replace(" ", "").lower()
  return text == text[::-1]

print(is_palindrome(text="Never     odd or      even"))