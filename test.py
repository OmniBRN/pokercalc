t = -1
try:
    while (t:=input()):
        t = t.lstrip(" ")
        if(t[0] != "#"):
            print(t)
except:
    True


test = [1,2,3]
print(test)