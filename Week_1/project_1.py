# Python program for simple interest, compound interest and annuity plan
P = float(input("Enter the Principal Amount: "))
R = float(input("Enter the Annual interest Rate in %: "))
T = float(input("Enter the time period in years: "))
n = int(input("Enter the number of compounding periods per year: "))
PMT = float(input("Enter the Periodic payment for Annuity: "))

def simple_interest(P,R,T):
    A = (P * R * T)/100
    return A

def compound_interest(P,R,n,T):
    B = P * (1 + R / n) ** (n * T)
    return B

def annuity_plan(PMT,R,T,n):
    C = PMT * (((1 + R/n) ** (n*T) -1) / (R/n))
    return C

simple_A = simple_interest(P,R,T)
compound_B = compound_interest(P,R,n,T)
Annuity_C = annuity_plan(PMT,R,T,n)

print(f"Simple Interest Amount: {simple_A:.2f}")
print(f"Compound Interest Amount: {compound_B:.2f}")
print(f"Annuity Plan Amount: {Annuity_C:.2f}")