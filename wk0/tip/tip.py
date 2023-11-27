def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dlr = d.replace('$', '').strip()
    return float(dlr)


def percent_to_float(p):
    perc = p.replace('%', '').strip()
    return float(perc)/100.0


main()