import cmath

def solve_quadratic():
    print("\nSolving Quadratic Equation: Ax^2 + Bx + C = 0")
    A = float(input("Enter A: "))
    B = float(input("Enter B: "))
    C = float(input("Enter C: "))

    discriminant = cmath.sqrt(B**2 - 4*A*C)
    root1 = (-B + discriminant) / (2*A)
    root2 = (-B - discriminant) / (2*A)

    print(f"Roots are: {root1} and {root2}")

def solve_cubic():
    print("\nSolving Cubic Equation: Ax^3 + Bx^2 + Cx + D = 0")
    A = float(input("Enter A: "))
    B = float(input("Enter B: "))
    C = float(input("Enter C: "))
    D = float(input("Enter D: "))

    if A == 0:
        print("This is not a cubic equation.")
        return

    # Normalize coefficients
    a = B / A
    b = C / A
    c = D / A

    # Calculate depressed cubic t^3+pt+q = 0
    p = b - (a**2)/3
    q = (2*(a**3))/27 - (a*b)/3 + c

    discriminant = (q**2)/4 + (p**3)/27

    if discriminant > 0:
        u = ((-q/2) + (discriminant)**0.5)**(1/3)
        v = ((-q/2) - (discriminant)**0.5)**(1/3)
        root1 = u + v - a/3
        print(f"One real root: {root1}")
    elif discriminant == 0:
        u = (-q/2)**(1/3)
        root1 = 2*u - a/3
        root2 = -u - a/3
        print(f"Roots are: {root1}, {root2}")
    else:
        r = (-p**3/27)**0.5
        theta = cmath.acos(-q/(2*r))
        r = (-p/3)**0.5
        root1 = 2*r*cmath.cos(theta/3) - a/3
        root2 = 2*r*cmath.cos((theta+2*cmath.pi)/3) - a/3
        root3 = 2*r*cmath.cos((theta+4*cmath.pi)/3) - a/3
        print(f"Roots are: {root1}, {root2}, {root3}")

def solve_quartic():
    print("\nSolving Quartic Equation: Ax^4 + Bx^3 + Cx^2 + Dx + E = 0")
    A = float(input("Enter A: "))
    B = float(input("Enter B: "))
    C = float(input("Enter C: "))
    D = float(input("Enter D: "))
    E = float(input("Enter E: "))

    print("Solving Quartic equations generally requires complex methods and substitutions.")
    print("This simple program cannot solve all quartic equations.")
    print("Consider reducing it to quadratic factors if possible.")

def main():
    while True:
        print("\n=== Root Finder Program ===")
        print("1. Solve Quadratic Equation")
        print("2. Solve Cubic Equation")
        print("3. Solve Quartic Equation")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            solve_quadratic()
        elif choice == '2':
            solve_cubic()
        elif choice == '3':
            solve_quartic()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
