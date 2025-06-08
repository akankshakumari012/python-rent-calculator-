#inputs we need from the user
#total rent
#total food ordered for snacking
#electricity unit spend
#charge per unit
##output
#total a ount you have to pay
rent=int(input("enter your hostel//flatrent="))

food=int(input("enter the amount of food ordered="))

electricity_spend=int(input("enter the total of electricity spend="))
charge_per_unit=int(input("enter the charge per unit="))
person=int(input("enter the number of persons living in room/ flat"))


totalbill=electricity_spend*charge_per_unit
output=(food +rent+totalbill)

print("each person will pay=",output)
