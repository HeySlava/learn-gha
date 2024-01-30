import os


var = os.environ['SLAVA']

for c in var:
    print(c)

print(var, 'os env')
print(len(var), 'len of this env')
