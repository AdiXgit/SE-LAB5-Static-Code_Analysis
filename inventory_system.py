import json
import logging
import ast  # FIX 1: added for safe eval alternative
from datetime import datetime

# Global variable for inventory data
stock_data = {}


# FIX 2: Changed mutable default argument logs=[] → logs=None
def add_item(item="default", qty=0, logs=None):
    """
    Add an item to inventory with specified quantity.
    """
    if logs is None:  # FIX 2 applied here
        logs = []

    if not item:
        return

    # MINOR FIX: Added type validation (not part of main 4 fixes)
    if not isinstance(qty, (int, float)):
        logging.warning("Invalid quantity type for %s", item)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove quantity of an item safely.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]

    # FIX 3: replaced bare except with specific exceptions
    except ValueError:
        print(f"Invalid quantity for {item}.")
    except KeyError:
        print(f"Item '{item}' not found in inventory.")


def get_qty(item):
    """
    Get the current quantity of an item.
    """
    # MINOR FIX: Safe access with .get() to avoid KeyError (not part of main 4 fixes)
    return stock_data.get(item, 0)


# FIX 4: Used context manager for file handling in load_data
def load_data(file_name="inventory.json"):
    """
    Load inventory data from a JSON file.
    """
    global stock_data
    try:
        with open(file_name, "r", encoding="utf-8") as file:  # FIX 4 applied here
            stock_data = json.load(file)
    except FileNotFoundError:
        stock_data = {}


# FIX 4 also applies to save_data (safe file handling)
def save_data(file_name="inventory.json"):
    """
    Save inventory data to a JSON file.
    """
    with open(file_name, "w", encoding="utf-8") as file:  # FIX 4 applied here too
        json.dump(stock_data, file, indent=4)


def print_data():
    """
    Print all items and their quantities.
    """
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """
    Return list of items below threshold quantity.
    """
    result = [item for item, qty in stock_data.items() if qty < threshold]
    return result


def main():
    """
    Main function for inventory operations.
    """

    # MINOR FIX: Improved function naming and readability (not part of main 4 fixes)
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("pear", 5)

    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()

    print_data()

    # FIX 1: Removed dangerous eval(), replaced with safe ast.literal_eval
    # eval("print('eval used')")  #Removed insecure code
    safe_code = "{'message': 'eval removed successfully'}"
    result = ast.literal_eval(safe_code)  #Safe evaluation
    print(result["message"])


# MINOR FIX: Added main guard (not part of main 4 fixes)
if __name__ == "__main__":
    main()


