palindromes = []
biggest = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        product = x * y
        palindrome = str(product)
        if palindrome[::-1] == palindrome:
            palindromes.append(int(palindrome))
for i in palindromes:
    if i > biggest:
        biggest = i
print("The greatest numeric palindrome that can be constructed with 2 multiplied 3-digit numbers is %d." % biggest)