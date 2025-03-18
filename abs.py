def calculate_total(price, tax, discount):
    total = price + (price * tax) - discount
    return total
