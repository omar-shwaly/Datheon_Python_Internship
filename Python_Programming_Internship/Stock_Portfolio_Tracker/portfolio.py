import csv

portfolio = {}


def menu():
    print("#" * 50)
    print("Menu".center(50, "-"))
    print("#" * 50)
    print("1- Add_Stock to Portfolio ")
    print("2- Portfolio Calculation")
    print("3-Exit")
    print("#" * 50)


def Add_Stock_to_Portfolio():
    print("Your selected Add Stock to Portfolio ")

    Stock_Name = input("Enter Stock Name \n").strip().upper()
    Number_of_shares = int(input("Enter Number_of_shares \n"))
    Stock_price = float(input("Enter Stock price \n"))

    Stock_Specifications = {
        "Stock_Name": Stock_Name,
        "Number_of_shares": Number_of_shares,
        " Stock_price": Stock_price,
    }
    portfolio[Stock_Name] = Stock_Specifications

    with open(
        "Stock_Portfolio_Tracker/portfolio_Summary.csv",
        "a",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.writer(file)
        writer.writerow([Stock_Name, Number_of_shares, Stock_price])

    print(f"Saved {Stock_Name} successfully!\n")


def Portfolio_Calculation():
    print("Your selected Portfolio Calculation ")
    total_portfolio_value = 0
    try:

        with open(
            "Stock_Portfolio_Tracker/portfolio_Summary.csv", "r", encoding="utf-8"
        ) as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                stock_name = row[0]
                shares = int(row[1])
                price = float(row[2])
                stock_total = shares * price
                total_portfolio_value += stock_total

                print(
                    f"Stock: {stock_name} | Shares: {shares} | Price: {price} | Total: {stock_total}"
                )

        print(f"Total Portfolio Value = {total_portfolio_value}\n")

    except FileNotFoundError:
        print("Portfolio file not found! Add some stocks first.\n")


def Exit():
    print("Goodbye!")


def main():
    option = 0
    while option != 3:
        menu()
        option = int(input("Enter your option \n"))
        if option == 1:
            Add_Stock_to_Portfolio()

        elif option == 2:
            Portfolio_Calculation()
        elif option == 3:
            Exit()
        else:
            print("invalid option plase enter option agin")


main()
