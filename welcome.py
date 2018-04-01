

print(' Hello there, Enter your name')
name = input()
if not re.match("[a-z]", name): 
    print(" I Don't need some freakn numbers ")
    
else: 
print('Hello ' + str(name) + ' This is my first program')
