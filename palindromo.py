from math import floor

three_digit_numbers_list = [value for value in range(100, 1000)]
greater_palindrome = 0
first_multi = 0
second_multi = 0
start = 0
middle = floor(len(three_digit_numbers_list)/2)
end = len(three_digit_numbers_list)

def multiple_is_palindrome(x, y):
	multiple = x * y
	multipleStr = str(multiple)

	if multipleStr == multipleStr[::-1]:
		return True, multiple
	else:
		return False, multiple

def find_greater_palindrome(numbers_list, start, end):

	hasPalindrome = False
	global greater_palindrome
	global first_multi
	global second_multi

	for x in numbers_list:
		for y in numbers_list:
			isPalindrome, multiple = multiple_is_palindrome(x, y)
		 
			if isPalindrome and multiple > greater_palindrome:
				hasPalindrome = True
				greater_palindrome = multiple 
				first_multi = x 
				second_multi = y 

	return hasPalindrome, greater_palindrome, first_multi, second_multi
 
l = [three_digit_numbers_list[value] for value in range(start, middle)]
r = [three_digit_numbers_list[value] for value in range(middle , end)]

end = len(l) -1

hasPalindrome, greater_palindrome, first_multi, second_multi = find_greater_palindrome(r, start, end)

if not hasPalindrome :
	hasPalindrome, greater_palindrome, first_multi, second_multi = find_greater_palindrome(l, start, end)

print("primeiro multiplo = ", first_multi)
print("segundo multiplo = ", second_multi)
print("Maior palindromo = ", greater_palindrome)


























