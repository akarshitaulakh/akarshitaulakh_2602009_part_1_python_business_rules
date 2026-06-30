# Python Business Rules Command-Line Application

## Student Details

**Student Name:** Akarshit Aulakh
**Student ID:** 2602009

## Problem Summary

This project is a menu-driven Python command-line application created for a business team. The application helps the business evaluate customers, calculate product billing amounts, check loan eligibility, and assign customers to marketing campaigns.

The program continues running until the user chooses the Exit option from the main menu.

The application is divided into multiple Python files inside the `src/` folder instead of writing the full program in one file.

## Features Implemented

The following features are implemented in this project:

1. Customer Profile and Financial Summary
2. Product Billing Calculator
3. Loan Eligibility Decision
4. Campaign Eligibility
5. Input Validation and Error Handling

## File Structure

```text
akarshitaulakh_2602009_part1_python_business_rules/
│
├── README.md
├── main.py
├── src/
│   ├── __init__.py
│   ├── customer.py
│   ├── billing.py
│   ├── eligibility.py
│   └── utils.py
├── outputs/
│   ├── sample_output.txt
│   └── screenshots/
└── tests/
    └── test_cases.md
```

## File Explanation

### main.py

This file starts the program by calling the menu function from `src/__init__.py`.

### src/**init**.py

This file contains the main menu. It allows the user to choose between customer summary, billing calculator, loan eligibility, campaign eligibility, and exit.

### src/customer.py

This file handles the Customer Profile and Financial Summary feature. It accepts customer details and calculates monthly savings, savings percentage, EMI-to-income ratio, risk category, and customer value category.

### src/billing.py

This file handles the Product Billing Calculator feature. It calculates gross amount, discount amount, amount after discount, GST amount, delivery charge, and final payable amount.

### src/eligibility.py

This file handles Loan Eligibility Decision and Campaign Eligibility. It checks customer details and returns a decision or campaign group with a reason.

### src/utils.py

This file is included as part of the required folder structure. Utility logic may be added here if shared helper functions are needed.

### outputs/sample_output.txt

This file contains sample program output.

### outputs/screenshots/

This folder contains screenshots of the running program.

### tests/test_cases.md

This file contains test cases used to check the program.

## How to Run the Program

1. Open the project folder in VS Code or another editor.
2. Open a terminal inside the project folder.
3. Run the following command:

```bash
python main.py
```

1. The main menu will appear.
2. Enter a number from 1 to 5 to use the application.

## Main Menu

```text
========================================
MAIN MENU
========================================
1: Customer Profile and Financial Summary
2: Product Billing Calculator
3: Loan Eligibility Decision
4: Campaign Eligibility
5: Exit
```

## Business Rules Used

### Customer Financial Summary Rules

Monthly savings are calculated as:

```text
Monthly savings = Monthly income - Monthly expenses - Existing EMI amount
```

Savings percentage is calculated as:

```text
Savings percentage = Monthly savings / Monthly income * 100
```

EMI-to-income ratio is calculated as:

```text
EMI-to-income ratio = Existing EMI amount / Monthly income * 100
```

## Risk Category Rules

### Low Risk

A customer is considered Low Risk if:

```text
Credit score is 750 or above
Savings percentage is 20% or above
EMI-to-income ratio is 30% or below
```

### High Risk

A customer is considered High Risk if:

```text
Credit score is below 650
OR savings percentage is below 10%
OR EMI-to-income ratio is above 50%
```

### Medium Risk

A customer is considered Medium Risk if they do not fall into Low Risk or High Risk.

## Customer Value Category Rules

### High Value

A customer is High Value if:

```text
Customer segment is Enterprise
OR monthly income is 100000 or above
```

### Medium Value

A customer is Medium Value if:

```text
Customer segment is Premium
OR monthly income is 50000 or above
```

### Low Value

A customer is Low Value if they do not fall into High Value or Medium Value.

## Product Billing Rules

Gross amount is calculated as:

```text
Gross amount = Quantity * Unit price
```

Discount amount is calculated as:

```text
Discount amount = Gross amount * Discount percentage / 100
```

Amount after discount is calculated as:

```text
Amount after discount = Gross amount - Discount amount
```

GST amount is calculated as:

```text
GST amount = Amount after discount * GST percentage / 100
```

Final payable amount is calculated as:

```text
Final payable amount = Amount after discount + GST amount + Delivery charge applied
```

## Free Delivery Rule

The free delivery threshold is defined as a constant in the code:

```text
FREE_DELIVERY_THRESHOLD = 5000
```

If the amount before delivery is greater than 5000, the delivery charge is waived.

If the amount before delivery is 5000 or below, the delivery charge is applied.

## Loan Eligibility Rules

The loan eligibility decision can be:

```text
Approved
Rejected
Manual Review Required
```

### Rejected

A loan is rejected if any of the following conditions are true:

```text
Customer age is below 21 or above 60
Credit score is below 600
Savings percentage is below 5%
EMI-to-income ratio is above 60%
Requested loan amount is more than 12 times the monthly income
```

### Approved

A loan is approved if all of the following conditions are true:

```text
Credit score is 750 or above
Savings percentage is 20% or above
EMI-to-income ratio is 40% or below
Requested loan amount is 6 times the monthly income or less
```

### Manual Review Required

A loan is sent for manual review if the customer passes the rejection rules but does not fully meet the automatic approval rules.

## Campaign Eligibility Rules

The campaign eligibility feature assigns customers to one of the following campaign groups:

```text
Premium Upsell Campaign
Loan Offer Campaign
Cashback Campaign
No Campaign
```

### Premium Upsell Campaign

A customer is assigned to the Premium Upsell Campaign if:

```text
The customer is an Enterprise customer and is High Value
OR the customer is Premium, has savings percentage of at least 20%, and lives in a target campaign city
```

Target campaign cities are:

```text
Mumbai, Delhi, Bengaluru, Chennai, Hyderabad, Pune
```

### Loan Offer Campaign

A customer is assigned to the Loan Offer Campaign if:

```text
Savings percentage is at least 15%
AND customer value category is Medium Value or High Value
```

### Cashback Campaign

A customer is assigned to the Cashback Campaign if:

```text
Customer segment is Standard
AND savings percentage is at least 5%
```

### No Campaign

A customer is assigned to No Campaign if they do not match any of the above campaign rules.

## Input Validation

The program handles invalid inputs by showing an error message and asking the user to enter the value again.

Examples of invalid inputs handled by the program include:

```text
Negative age
Monthly income less than 1
Negative monthly expenses
Negative EMI amount
Credit score below 300 or above 900
Quantity less than 1
Negative unit price
Discount percentage below 0 or above 100
Negative GST percentage
Invalid customer segment
Text entered where a number is expected
```

## Sample Input and Output

### Sample: Customer Profile and Financial Summary

```text
Enter your choice: 1
Enter the customer name: Akarshita
Enter the age of the customer: 30
Enter the city of the customer: Mumbai
Enter the monthly income of the customer: 80000
Enter the monthly expenses of the customer: 30000
Enter the existing EMI amount: 10000
Enter the credit score of the customer: 780
Enter the segment of the customer (Standard / Premium / Enterprise): Premium

CUSTOMER PROFILE
Customer name: Akarshita
Age: 30
City: Mumbai
Monthly income: ₹80000.00
Monthly expenses: ₹30000.00
Existing EMI amount: ₹10000.00
Credit score: 780
Customer segment: Premium

FINANCIAL SUMMARY
Monthly savings: ₹40000.00
Savings percentage: 50.00%
EMI-to-income ratio: 12.50%
Risk category: Low Risk
Customer value category: Medium Value
```

### Sample: Product Billing Calculator

```text
Enter your choice: 2
Enter the product name: Laptop
Enter the product category: Electronics
Enter the quantity of the products: 2
Enter the unit price of the product: 30000
Enter the discount percentage: 10
Enter the GST percentage: 18
Enter the delivery charge: 200

PRODUCT DETAILS
Product name: Laptop
Product category: Electronics
Quantity: 2
Unit price: ₹30000.00
Discount percentage: 10.00%
GST percentage: 18.00%
Entered delivery charge: ₹200.00

BILLING SUMMARY
Gross amount: ₹60000.00
Discount amount: ₹6000.00
Amount after discount: ₹54000.00
GST amount: ₹9720.00
Delivery rule: Delivery charge waived
Delivery charge applied: ₹0.00
Final payable amount: ₹63720.00
```

### Sample: Loan Eligibility Decision

```text
Enter your choice: 3
Enter the age of the customer: 35
Enter the monthly income of the customer: 90000
Enter the monthly expenses of the customer: 35000
Enter the existing EMI amount: 10000
Enter the amount of loan requested by the customer: 400000
Enter the credit score of the customer: 780

Decision: Approved
Reason: Customer has a strong credit score, good savings, and manageable EMI level.
```

### Sample: Campaign Eligibility

```text
Enter your choice: 4
Enter the city of the customer: Mumbai
Enter the monthly income of the customer: 80000
Enter the monthly expenses of the customer: 30000
Enter the existing EMI amount: 10000
Enter the segment of the customer (Standard / Premium / Enterprise): Premium

Campaign group: Premium Upsell Campaign
Reason: Premium customer has good savings and lives in a target campaign city.
```

## Screenshots

Screenshots of the program running are placed inside:

```text
outputs/screenshots/
```

## Assumptions Made

The following assumptions were made while creating this project:

1. Monthly income must be greater than 0.
2. Age between 15 and 110 is accepted as valid input, but loan approval uses the age range 21 to 60.
3. Credit score must be between 300 and 900.
4. Customer segment must be Standard, Premium, or Enterprise.
5. Delivery is waived only when the amount before delivery is greater than 5000.
6. EMI is included when calculating monthly savings.
7. The program uses simple business rules for learning purposes.
8. All currency values are displayed in Indian Rupees.
