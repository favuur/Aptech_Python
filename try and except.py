try:
    r
except:
    print("you didnt defined r")
finally:
    print("we caught the error")



try:
    print(x)
except:
    print("error detected")





x=input("input any alphabet")
try:
    #int(x)
    print(int(x))
except:
    print("alphabet are not allow")
