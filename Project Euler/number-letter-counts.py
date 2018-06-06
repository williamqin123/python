ones = None
tens = None
hundreds = None
thousands = None
written = None
sum = 0
def analyse():
    global ones, tens, hundreds, thousands
    if ones != "":
        ones = ""
        return tenTeens[int(written[3])]
    else:
        return "ten"
def revise():
    global ones, tens, hundreds, thousands
    if tens == analyse:
        tens = tens()
    if ones != "" and tens != "":
        tens += "-"
    if (tens != "" or ones != "") and hundreds != "":
        hundreds += " and "
tenTeens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
singleTens = ["", analyse, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
onesDigits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
hundredsDigits = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
thousandsDigits = ["", "one thousand", "two thousand", "three thousand", "four thousand", "five thousand", "six thousand", "seven thousand", "eight thousand", "nine thousand"]
for number in range(1, 1000+1):
    written = str(number)
    written = "0" * (4 - len(written)) + written
    thousands = thousandsDigits[int(written[0])]
    hundreds = hundredsDigits[int(written[1])]
    tens = singleTens[int(written[2])]
    ones = onesDigits[int(written[3])]
    revise()
    sentence = thousands + hundreds + tens + ones
    print("The number written in word form is %s." % sentence)
    semiSum = len(sentence)
    for i in sentence:
        if (i == " " and i != "-") or (i == "-" and i != " "):
            semiSum -= 1
    sum += semiSum
print("All the letters in all the numbers that are in word form add up to a sum of %d." % sum)