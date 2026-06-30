## PART - 1: PYTHON BUSINESS RULES ENGINE

Student name - Akarshit Aulakh
Student ID - 2602009

## Problem summary ->
To build a command line python application that helps a business team evaluate customers, calculate billing amounts and make decision recommendations.

## Features implemented ->
Feature 1 - Customer profile and financial summary

Feature 2 - Product Billing calculator

Feature 3 - Loan Eligibility Decision

Feature 4 - Campaign Eligibility

## Business rules used ->

# Feature 1: Customer profile and financial summary:

1. Monthly Savings = Monthly Income - Monthly Expenses

2. Savings Percentage = ((Monthly Income - Monthly Expenses)*100/(Monthly Income))

3. EMI-to-income Ratio = Existing EMI amount / Monthly Income

4. Risk Category:

    - Customers having EMI-to-income Ratio <= 0.4 are Low Risk Customers.

    - Customers having EMI-to-income Ratio >= 0.5 are High Risk Customers.

    - Customers having 0.4 < EMI-to-income Ratio < 0.5 are Medium Risk Customers.

5. Customer Value Category:

    - Customers having credit score < 649 are Low Value Customers.

    - Customers having credit score >= 750 are High Value Customers.

    - Customers having 650 <= credit score < 750 are Medium Value Customers.

# Feature 2: Product Billing Calculator:

1. Gross Amount = Quantity * Unit_price

2. Discount Amount = (Quantity * Unit_price * Discount percentage / 100)

3. Amount After Discount = Gross Amount - Discount Amount

4. GST Amount = Amount After Discount * (GST percentage/100)

5. Delivery Charge Applied =

6. Final Payable Amount =>

    Total Amount = Amount After Discount + GST Amount

    - if Total Amount > 999, then Delivery Charge Applied to total amount

    - if <= 999, then no delivery charge applied to total amount

# Feature 3: Loan Eligibility Decision:

1. If age of customer is between 21 and 60, credit score is more than 750, EMI_to_Income_ratio is less than 0.4 and requested loan amount is less than or equal to 3 times the monthly income then the Loan is Approved automatically.

2. If age is less than 21 or greater than 60, credit score is less than 600 and ratio is less than 0.4 then the Loan is rejected automatically.

3. For rest all cases, the manual review is required to approve a person for loan or not.

# Feature 4: Campaign Eligibility:

1. If a customer lies in Enterprise Segment, then it is automatically fall under "Premium Upsell Campaign".

2. If a customer is Premium customer segment, falls in Medium or High category of customer value category and have savings of more than 25% then they fall under "Premium Upsell Campaign".

3. If a customer is Standard customer segment, falls in Low category of customer value category and have savings of less than 10% then they fall under "Loan offer Campaign".

4. If a customer falls in Premium or Standard customer segment, falls in Medium category of customer value category and have savings between 10 and 25% then they fall under "Cashback Campaign".

5. And in all other cases the remaining customers fall under "No Campaign".
