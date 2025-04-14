def calculate_atr(experience, age):
    if experience > 25 and age >= 55:
        atr = 5600000
    elif experience > 20 and age >= 45:
        atr = 4480000
    elif experience > 10 and age >= 35:
        atr = 1500000
    else:
        atr = 550000
    return atr

def main():
    print("IZIFIN TECHNOLOGY - STAFF ATR CALCULATOR\n")

    experience = int(input("Enter your years of experience: "))
    age = int(input("Enter your age: "))

    atr = calculate_atr(experience, age)

    print("Your Annual Tax Revenue (ATR) is: N", atr)

if __name__ == "__main__":
    main()