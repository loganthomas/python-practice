def addtwo(a,b):
    added = a+b
    return added

x = raw_input('Provide x:')
y = raw_input('Provide y:')

try:
    x=float(x)
    y=float(y)
except:
    print 'Invalid Number'
    exit()
print addtwo(x,y)