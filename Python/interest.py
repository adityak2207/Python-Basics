#Calculate simple and compound interest for a given principal, rate and time

p = float(input("Enter the prinicpal : "))
t = float(input("Enter the time : "))
r = float(input("Enter the rate : "))

#Simple interest
si = p*t*r / 100
fa_si = float(p + si)
print("The simple interest is", si)
print("The final amount is : ", fa_si)

#Compound interest assuming yearly compound of interest
ci = float(p*(pow(1+r/100,t)) - p)
#ci = float(p* ( pow((1 + r/1), 1*t) - 1 ))
fa_comp = p + ci
print("\nThe compound interest is", round(ci,2))
print("The final amount after compounding is", round(fa_comp,2))
