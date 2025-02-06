bp=int(input("Enter your buying amount :"))
sp=int(input("Enter your selling amount:"))
if bp==sp:
    print("it equal")
elif bp>sp:
    print("in lose")
    print("loseamount",bp-sp)
else:
    print("in profit")
    print("profitamount",sp-bp)
