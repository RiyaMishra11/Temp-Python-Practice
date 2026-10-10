"""Validate records before using them in a data analysis."""
def validate_sales_record(record):
    errors = []

    product = record.get("product")
    if not isinstance(product, str) or not product.strip():
        errors.append("Product must be a non-empty string.")

    try:
        sales = float(record.get("sales"))
        if sales < 0:
            errors.append("Sales cannot be negative.")
    except (TypeError, ValueError):
        errors.append("Sales must be a valid number.")

    quantity = record.get("quantity")
    if not isinstance(quantity, int) or quantity < 0:
        errors.append("Quantity must be a non-negative integer.")

    return errors

if __name__ == "__main__":
    records = [
        {"product": "Laptop", "sales": 45000, "quantity": 2},
        {"product": "", "sales": -100, "quantity": 1},
        {"product": "Mouse", "sales": "not available", "quantity": -3},
    ]
    for record in records:
        issues = validate_sales_record(record)
        if issues:
            print("Invalid record:", record)
            for issue in issues:
                print("-", issue)
        else:
            print("Valid record:", record)

    # Practice: validate sales ranges and add a date field.
