x = -120
if x > 0:
    tmp = str(x)
    print ( 0 if int(tmp[::-1]) > 2147483646 else int(tmp[::-1]))
else:
    tmp = str(abs(x))
    print(0 if int('-'+tmp[::-1]) < -2147483648 else int('-'+tmp[::-1]))