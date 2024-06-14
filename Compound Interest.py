def compound_interest(principal, rate, periods, time):
    amount = principal * ((1 + rate / periods) ** (periods * time))
    return amount

def main():
    P = 10000  # principal amount
    r = 0.08   # interest rate
    n = 12     # number of times interest applied per time period

    t = int(input("Enter the number of years: "))  # time in years

    finalamount = compound_interest(P, r, n, t)
    print("The final amount after", t, "years will be:", finalamount)

if __name__ == "__main__":
    main()
