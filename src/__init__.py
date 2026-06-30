from src.billing import product_billing_calculator
from src.customer import calculate_customer_profile_and_financial_summary
from src.eligibility import loan_eligibility_decision, campaign_eligibility


def show_menu():
    while True:
        print("\n========================================")
        print("MAIN MENU")
        print("========================================")
        print("1: Customer Profile and Financial Summary")
        print("2: Product Billing Calculator")
        print("3: Loan Eligibility Decision")
        print("4: Campaign Eligibility")
        print("5: Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n========================================")
            print("Selected: Customer Profile and Financial Summary")
            print("========================================")
            calculate_customer_profile_and_financial_summary()

        elif choice == "2":
            print("\n========================================")
            print("Selected: Product Billing Calculator")
            print("========================================")
            product_billing_calculator()

        elif choice == "3":
            print("\n========================================")
            print("Selected: Loan Eligibility Decision")
            print("========================================")
            loan_eligibility_decision()

        elif choice == "4":
            print("\n========================================")
            print("Selected: Campaign Eligibility")
            print("========================================")
            campaign_eligibility()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
