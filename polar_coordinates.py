import cmath


x = input()[:-1].split('+')
print(abs(complex(int(x[0]),int(x[1]))))
print(cmath.phase(complex(int(x[0]),int(x[1]))))
