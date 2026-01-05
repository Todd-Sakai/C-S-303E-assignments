# CS 303E Quiz 1C
# do NOT rename this file, otherwise Gradescope will not accept your submission


# Problem 1: Clothing Purchases
def clothingPurchases():
    soldoutFirst=input()
    soldoutSecond=input()
    total=259.41

    if (soldoutFirst=="T-Shirt"):
        total-=19.98
    elif (soldoutFirst=="Jeans"):
        total-=33.95
    elif (soldoutFirst=="Cologne"):
        total-=74.95
    elif (soldoutFirst=="Belt"):
        total-=48.72
    elif (soldoutFirst=="Perfume"):
        total-=81.81

    if (soldoutSecond=="T-Shirt"):
        total-=19.98
    elif (soldoutSecond=="Jeans"):
        total-=33.95
    elif (soldoutSecond=="Cologne"):
        total-=74.95
    elif (soldoutSecond=="Belt"):
        total-=48.72
    elif (soldoutSecond=="Perfume"):
        total-=81.81
    print("$" + format(total,".2f"))
    pass


# Problem 2: First Term Larger than k
def firstTermLarger():
    k=float(input())
    n=1
    an=.65*n**2+1.32*n

    while (an<=k):
        n+=1
        an=.65*n**2+1.32*n
    print(format(an,".2f"))
    pass


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # clothingPurchases()
    # firstTermLarger()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT