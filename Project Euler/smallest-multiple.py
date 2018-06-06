number = 1
end = 20+1
output = False
def loop(code, parent, start, stop, step):
    for x in range(start, stop, step):
        exec(code)
loop('''
global number, output
if number % x != 0:
    loop(\'\'\'
global number, output
if parent % x == 0 and output == False:
    print(parent, x)
    number *= parent / x
    output = True
\'\'\', x, x-1, 1-1, -1)
    if output == True:
        output = False
    else:
        number *= x
else:
    pass
''', None, 1, end, 1)
print("The smallest number that is divisible by all the numbers from 1 to 20 is %d." % number)