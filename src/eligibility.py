from src.utils import __format_number__, __get_valid_text__, __get_valid_number__, __get_valid_segment__, __risk_category__, __customer_value_category__, __emi_to_income_ratio__, __savings_percent__, __monthly_savings__

TARGET_CAMPAIGN_CITIES = ["Mumbai", "Delhi", "Bengaluru", "Chennai", "Hyderabad", "Pune"]

def loan_eligibility_decision():
    age = __get_valid_number__("Enter the age of the customer: ", 15, 110)
    monthly_income = __get_valid_number__("Enter the monthly income of the customer: ", 1)
    monthly_expenses = __get_valid_number__("Enter the monthly expenses of the customer: ", 0)
    existing_emi_amount = __get_valid_number__("Enter the existing EMI amount: ", 0)
    requested_loan_amount = __get_valid_number__("Enter the amount of loan requested by the customer: ", 1)
    credit_score = __get_valid_number__("Enter the credit score of the customer: ", 300, 900)

    monthly_savings = monthly_income - monthly_expenses - existing_emi_amount
    savings_percentage = (monthly_savings / monthly_income) * 100
    emi_to_income_ratio = (existing_emi_amount / monthly_income)

    decision, reason = check_loan_eligibility(
        age,
        monthly_income,
        credit_score,
        savings_percentage,
        emi_to_income_ratio,
        requested_loan_amount
    )

    print("\n------------------------------------------")
    print("LOAN ELIGIBILITY SUMMARY")
    print("------------------------------------------")
    print("Age:", age)
    print("Monthly income:", __format_number__(monthly_income))
    print("Monthly expenses:", __format_number__(monthly_expenses))
    print("Existing EMI amount:", __format_number__(existing_emi_amount))
    print("Requested loan amount:", __format_number__(requested_loan_amount))
    print("Credit score:", credit_score)
    print("Monthly savings:", __format_number__(monthly_savings))
    print("Savings percentage:", __format_number__(savings_percentage))
    print("EMI-to-income ratio:", __format_number__(emi_to_income_ratio))

    print("\nDecision:", decision)
    print("Reason:", reason)
    print("------------------------------------------")

def check_loan_eligibility(age, monthly_income, credit_score, savings_percentage, emi_to_income_ratio, requested_loan_amount):
    if age < 21 or age > 60:
        return "Rejected", "Customer age is outside the allowed loan age range of 21 to 60."
    if credit_score < 600:
        return "Rejected", "Credit score is too low for loan approval."
    if savings_percentage < 5:
        return "Rejected", "Savings percentage is too low after expenses and existing EMI."
    if emi_to_income_ratio > 0.6:
        return "Rejected", "Existing EMI is too high compared to monthly income."
    if requested_loan_amount > monthly_income * 12:
        return "Rejected", "Requested loan amount is more than 12 times the monthly income."
    if credit_score >= 750 and savings_percentage >= 20 and emi_to_income_ratio <= 0.4 and requested_loan_amount <= monthly_income * 6:
        return "Approved", "Customer has a strong credit score, good savings, and manageable EMI level."
    return "Manual Review Required", "Customer meets basic rules, but does not fully meet the automatic approval rules."



def campaign_eligibility():
    city = __get_valid_text__("Enter the city of the customer: ").title()
    monthly_income = __get_valid_number__("Enter the monthly income of the customer: ", 1)
    monthly_expenses = __get_valid_number__("Enter the monthly expenses of the customer: ", 0)
    existing_emi_amount = __get_valid_number__("Enter the existing EMI amount: ", 0)
    customer_segment = __get_valid_segment__()

    monthly_savings = monthly_income - monthly_expenses - existing_emi_amount
    savings_percentage = (monthly_savings / monthly_income) * 100
    customer_value_category = __customer_value_category__(monthly_income, customer_segment)

    campaign, reason = check_campaign_eligibility(
        customer_segment,
        city,
        savings_percentage,
        customer_value_category
    )

    print("\n------------------------------------------")
    print("CAMPAIGN ELIGIBILITY SUMMARY")
    print("------------------------------------------")
    print("City:", city)
    print("Monthly income:", __format_number__(monthly_income))
    print("Monthly expenses:", __format_number__(monthly_expenses))
    print("Existing EMI amount:", __format_number__(existing_emi_amount))
    print("Customer segment:", customer_segment.title())
    print("Monthly savings:", __format_number__(monthly_savings))
    print("Savings percentage:", __format_number__(savings_percentage))
    print("Customer value category:", customer_value_category)

    print("\nCampaign group:", campaign)
    print("Reason:", reason)
    print("------------------------------------------")

def check_campaign_eligibility(customer_segment, city, savings_percentage, customer_value_category):
    if customer_segment == "enterprise" and customer_value_category == "High Value":
        return "Premium Upsell Campaign", "Enterprise high-value customers are suitable for premium offers."
    if customer_segment == "premium" and savings_percentage >= 20 and city in TARGET_CAMPAIGN_CITIES:
        return "Premium Upsell Campaign", "Premium customer has good savings and lives in a target campaign city."
    if savings_percentage >= 15 and customer_value_category in ["Medium Value", "High Value"]:
        return "Loan Offer Campaign", "Customer has enough savings capacity for a loan offer campaign."
    if customer_segment == "standard" and savings_percentage >= 5:
        return "Cashback Campaign", "Standard customer has some savings and may respond well to cashback offers."
    return "No Campaign", "Customer does not match the current campaign rules."
