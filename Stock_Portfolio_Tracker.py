#Stock Portfolio Tracker

prices = {
    "AAPL": 100,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 415,
    "NVDA": 875,
}

print("=== Stock Portfolio Tracker ===")
print("Stocks:", ", ".join(prices.keys()))
print()

total = 0
purchases = []  

while True:
    symbol = input("Enter stock (or 'done'): ").upper()

    if symbol == "DONE":
        break

    if symbol not in prices:
        print("Stock not found. Try again.")
        continue

    while True:
        qty_input = input(f"Quantity of {symbol}: ")
        if qty_input.isdigit():
            qty = int(qty_input)
            break
        else:
            print("Invalid quantity. Please enter a whole number.")

    value = prices[symbol] * qty
    total += value
    purchases.append((symbol, qty, prices[symbol], value))
    print(f" {symbol} * {qty} = ${value}\n")

print(f"\nTotal Investment: ${total}")

save = input("\nSave results to a file? (yes/no): ").lower()

if save == "yes":
    file_format = input("Save as .txt or .csv? ").lower()

    if file_format == "csv":
        f = open("portfolio.csv", "w")
        f.write("Stock,Quantity,Price,Value\n")
        for symbol, qty, price, value in purchases:
            f.write(f"{symbol},{qty},{price},{value}\n")
        f.write(f"Total,,,{total}\n")
        f.close()
        print("Saved to portfolio.csv")

    elif file_format == "txt":
        f = open("portfolio.txt", "w")
        f.write("=== Stock Portfolio Tracker ===\n")
        for symbol, qty, price, value in purchases:
            f.write(f"{symbol} * {qty} = ${value}\n")
        f.write(f"\nTotal Investment: ${total}\n")
        f.close()
        print("Saved to portfolio.txt")

    else:
        print("Unrecognized format. Skipping save.")
else:
    print("Results not saved.")