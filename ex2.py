
print("********world 11* hotel******")
print("menus here->")
print("dhosa-30")
print("biriyani-100")
print("idly-10")
one_dhosa=30
one_biriyani=100
one_idly=10
menus=["biriyani","dhosa","idly"]
your_order=input("enter your order:")

if your_order in menus:
    print(f"yes!..{your_order} is avilable")
    qunatity=int(input(f"how many {your_order} you want:"))
    if your_order=="biriyani":
        total=one_biriyani*qunatity
        if total>=1000:
            offer_total=total-200
            print(f"you ordered 1000+ so 200 less final offer bill is {offer_total}")
        else:
            print(f"you total bill is {total}")
    elif your_order=="dhosa":
        total=one_dhosa*qunatity
        if total>=1000:
            offer_total=total-200
            print(f"you ordered 1000+ so 200 less final offer bill is {offer_total}")
        else:
            print(f"you total bill is {total}")
    elif your_order=="idly":
        total=one_idly*qunatity
        if total>=1000:
            offer_total=total-200
            print(f"you ordered 1000+ so 200 less final offer bill is {offer_total}")
        else:
            print(f"you total bill is {total}")
        
else:
    print(f"sorry {your_order} is not avilable")
    

