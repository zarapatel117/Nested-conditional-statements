q= int(input("how much units did you consumed "))
if q<50:
    amount=q*2.60
    surcharge=25
elif q<=100 :
    amount=130+(q-50)*3.25
    surcharge=35
elif q<=100 :
    amount=130+162.50+(q-100)*5.26
    surcharge=45
else :
    amount=130+162.50+526+(q-200)*8.45   
    surcharge=75
total =amount+surcharge
print ("your total bill is",total)    