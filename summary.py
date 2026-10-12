"""Print a short summary of Northwind's daily sales file."""
import csv

FILE = "sales.csv"


def load_rows(path):
    """Read the CSV into a list of dictionaries, with amount as a number."""
    rows = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            row["amount"] = float(row["amount"])
            rows.append(row)
    return rows


def totals_by(rows, column):
    """Add up the amount for each value in one column, e.g. each store."""
    totals = {}
    for row in rows:
        key = row[column]
        totals[key] = totals.get(key, 0) + row["amount"]
    return totals


def main():
    rows = load_rows(FILE)
    total = sum(row["amount"] for row in rows)
    stores = totals_by(rows, "store")
    top = max(stores, key=stores.get)

    print(f"Rows: {len(rows)}")
    print(f"Stores: {len(stores)}")
    print(f"Total sales: ${total:,.2f}")
    for store, amount in sorted(stores.items()):
        print(f"  {store}: ${amount:,.2f}")
    print(f"Top store: {top}")


if __name__ == "__main__":
    main()
