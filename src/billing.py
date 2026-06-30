from src.utils import __format_number__, __get_valid_text__, __get_valid_number__

FREE_DELIVERY_THRESHOLD = 5000

def product_billing_calculator():
    product_name = __get_valid_text__("Enter the product name: ")
    product_category = __get_valid_text__("Enter the product category: ")

    quantity = __get_valid_number__("Enter the quantity of the products: ", 1)
    unit_price = __get_valid_number__("Enter the unit price of the product: ", 0)
    discount_percentage = __get_valid_number__("Enter the discount percentage: ", 0, 100)
    gst_percentage = __get_valid_number__("Enter the GST percentage: ", 0)
    delivery_charge = __get_valid_number__("Enter the delivery charge: ", 0)

    gross_amount = quantity * unit_price
    discount_amount = gross_amount * discount_percentage / 100
    amount_after_discount = gross_amount - discount_amount
    gst_amount = amount_after_discount * gst_percentage / 100
    amount_before_delivery = amount_after_discount + gst_amount

    if amount_before_delivery > FREE_DELIVERY_THRESHOLD:
        delivery_charge_applied = 0
        delivery_message = "Delivery charge waived"
    else:
        delivery_charge_applied = delivery_charge
        delivery_message = "Delivery charge applied"

    final_payable_amount = amount_before_delivery + delivery_charge_applied

    print("\n------------------------------------------")
    print("PRODUCT DETAILS")
    print("------------------------------------------")
    print("Product name:", product_name.title())
    print("Product category:", product_category.title())
    print("Quantity:", int(quantity))
    print("Unit price:", __format_number__(unit_price))
    print("Discount percentage:", __format_number__(discount_percentage))
    print("GST percentage:", __format_number__(gst_percentage))
    print("Entered delivery charge:", __format_number__(delivery_charge))

    print("\n------------------------------------------")
    print("BILLING SUMMARY")
    print("------------------------------------------")
    print("Gross amount:", __format_number__(gross_amount))
    print("Discount amount:", __format_number__(discount_amount))
    print("Amount after discount:", __format_number__(amount_after_discount))
    print("GST amount:", __format_number__(gst_amount))
    print("Delivery rule:", delivery_message)
    print("Delivery charge applied:", __format_number__(delivery_charge_applied))
    print("Final payable amount:", __format_number__(final_payable_amount))
    print("------------------------------------------")
