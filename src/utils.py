## INPUT VALIDATION FUNCTIONS

VALID_SEGMENTS = ["standard", "premium", "enterprise"]

def __get_valid_text__(message):
    while True:
        value = input(message).strip()
        if len(value) >= 2:
            return value
        print("Invalid input. Please enter at least 2 characters.")

def __get_valid_number__(message, minimum_value, maximum_value=None):
    while True:
        try:
            value = float(input(message))
            if value < minimum_value:
                print("Invalid input. Value must be at least", minimum_value)
            elif maximum_value is not None and value > maximum_value:
                print("Invalid input. Value must not be more than", maximum_value)
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def __get_valid_segment__():
    while True:
        segment = input("Enter the segment of the customer (Standard / Premium / Enterprise): ").strip().lower()
        if segment in VALID_SEGMENTS:
            return segment
        print("Invalid segment. Please enter Standard, Premium, or Enterprise.")

## OUTPUT FORMATTING FUNCTIONS

def __format_number__(value):
    return "{:.2f}".format(value)

## CALCULATION FUNCTIONS

def __gross_amount__(quantity, unit_price):
    gross_amount = quantity * unit_price
    return gross_amount

def __discount_amount__(quantity, unit_price, discount_percentage):
    discount_amount = __gross_amount__(quantity, unit_price) * (discount_percentage/100)
    return discount_amount

def __amount_after_discount__(quantity, unit_price, discount_percentage):
    amount_after_discount = __gross_amount__(quantity, unit_price) - __discount_amount__(quantity, unit_price, discount_percentage)
    return amount_after_discount

def __gst_amount__(quantity, unit_price, discount_percentage, gst_percentage):
    gst_amount = __amount_after_discount__(quantity, unit_price, discount_percentage) * (gst_percentage/100)
    return gst_amount

def __delivery_charge_applied__(quantity, unit_price, delivery_charge):
    delivery_charge_applied = __gross_amount__(quantity, unit_price) * delivery_charge
    return  delivery_charge_applied

def __final_payable_amount__(quantity, unit_price, discount_percentage, gst_percentage, delivery_charge):
    total_amount = __amount_after_discount__(quantity, unit_price, discount_percentage) + __gst_amount__(quantity, unit_price, discount_percentage, gst_percentage)
    if total_amount > 999:
        return total_amount + delivery_charge
    else:
        return total_amount

def __monthly_savings__(monthly_income, monthly_expenses, existing_emi_amount):
    total_expenses = monthly_expenses + existing_emi_amount
    return round((monthly_income - total_expenses),2)

def __savings_percent__(monthly_income, monthly_expenses, existing_emi_amount):
    savings = __monthly_savings__(monthly_income, monthly_expenses, existing_emi_amount)
    return round((savings / monthly_income * 100),2)

def __emi_to_income_ratio__(existing_EMI_amount, monthly_income):
    return round(existing_EMI_amount / monthly_income,2)

def __risk_category__(credit_score, savings_percentage, emi_to_income_ratio):
    if credit_score >= 750 and savings_percentage >= 20 and emi_to_income_ratio <= 0.3:
        return(f"LOW Risk")
    elif credit_score < 650 or savings_percentage < 10 or emi_to_income_ratio > 0.5:
        return(f"HIGH Risk")
    else:
        return "Medium Risk"

def __customer_value_category__(monthly_income, customer_segment):
    if customer_segment == "enterprise" or monthly_income >= 100000:
        return "High Value"
    elif customer_segment == "premium" or monthly_income >= 50000:
        return "Medium Value"
    else:
        return "Low Value"
