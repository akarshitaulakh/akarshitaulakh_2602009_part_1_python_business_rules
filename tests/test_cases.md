# Test Cases

## Test Case 1: Valid Customer Profile - Low Risk Customer

**Input values:**

```text
Menu choice: 1
Customer name: Rahul Dua
Age: 30
City: Mumbai
Monthly income: 80000
Monthly expenses: 30000
Existing EMI amount: 10000
Credit score: 780
Customer segment: Premium
```

**Expected output or decision:**

```text
Monthly savings: ₹40000.00
Savings percentage: 50.00%
EMI-to-income ratio: 12.50%
Risk category: Low Risk
Customer value category: Medium Value
```

**Reason for expected output:**

Monthly savings are calculated as 80000 - 30000 - 10000 = 40000. The savings percentage is 50%, EMI-to-income ratio is 12.5%, and the credit score is above 750, so the customer is Low Risk. The customer is Premium, so the value category is Medium Value.

---

## Test Case 2: Valid Customer Profile - High Value Customer

**Input values:**

```text
Menu choice: 1
Customer name: Rahul Dua
Age: 40
City: Delhi
Monthly income: 120000
Monthly expenses: 50000
Existing EMI amount: 20000
Credit score: 720
Customer segment: Standard
```

**Expected output or decision:**

```text
Monthly savings: ₹50000.00
Savings percentage: 41.67%
EMI-to-income ratio: 16.67%
Risk category: Medium Risk
Customer value category: High Value
```

**Reason for expected output:**

The customer has monthly income above 100000, so the customer is High Value. The credit score is not high enough for Low Risk, but the customer does not meet High Risk conditions, so the risk category is Medium Risk.

---

## Test Case 3: Product Billing With Delivery Charge Waived

**Input values:**

```text
Menu choice: 2
Product name: Laptop
Product category: Electronics
Quantity: 2
Unit price: 30000
Discount percentage: 10
GST percentage: 18
Delivery charge: 200
```

**Expected output or decision:**

```text
Gross amount: ₹60000.00
Discount amount: ₹6000.00
Amount after discount: ₹54000.00
GST amount: ₹9720.00
Delivery charge applied: ₹0.00
Final payable amount: ₹63720.00
```

**Reason for expected output:**

Gross amount is 2 * 30000 = 60000. Discount is 10% of 60000 = 6000. Amount after discount is 54000. GST is 18% of 54000 = 9720. Amount before delivery is 63720, which is greater than 5000, so delivery is waived.

---

## Test Case 4: Product Billing With Delivery Charge Applied

**Input values:**

```text
Menu choice: 2
Product name: Mouse
Product category: Accessories
Quantity: 2
Unit price: 500
Discount percentage: 10
GST percentage: 18
Delivery charge: 100
```

**Expected output or decision:**

```text
Gross amount: ₹1000.00
Discount amount: ₹100.00
Amount after discount: ₹900.00
GST amount: ₹162.00
Delivery charge applied: ₹100.00
Final payable amount: ₹1162.00
```

**Reason for expected output:**

Gross amount is 2 * 500 = 1000. Discount is 100. Amount after discount is 900. GST is 162. Amount before delivery is 1062, which is below the free delivery threshold of 5000, so delivery charge is applied.

---

## Test Case 5: Loan Eligibility Approved

**Input values:**

```text
Menu choice: 3
Age: 35
Monthly income: 90000
Monthly expenses: 35000
Existing EMI amount: 10000
Requested loan amount: 400000
Credit score: 780
```

**Expected output or decision:**

```text
Decision: Approved
```

**Reason for expected output:**

The customer is within the loan age range, has a credit score above 750, savings percentage is above 20%, EMI-to-income ratio is below 40%, and requested loan amount is less than 6 times the monthly income.

---

## Test Case 6: Loan Eligibility Rejected Due to Credit Score

**Input values:**

```text
Menu choice: 3
Age: 35
Monthly income: 70000
Monthly expenses: 30000
Existing EMI amount: 10000
Requested loan amount: 200000
Credit score: 550
```

**Expected output or decision:**

```text
Decision: Rejected
Reason: Credit score is too low for loan approval.
```

**Reason for expected output:**

The credit score is below 600, so the loan should be rejected.

---

## Test Case 7: Loan Eligibility Manual Review Required

**Input values:**

```text
Menu choice: 3
Age: 35
Monthly income: 70000
Monthly expenses: 35000
Existing EMI amount: 15000
Requested loan amount: 300000
Credit score: 700
```

**Expected output or decision:**

```text
Decision: Manual Review Required
```

**Reason for expected output:**

The customer does not meet rejection rules, but also does not fully meet automatic approval rules because the credit score is below 750. Therefore, manual review is required.

---

## Test Case 8: Campaign Eligibility - Premium Upsell Campaign

**Input values:**

```text
Menu choice: 4
City: Mumbai
Monthly income: 80000
Monthly expenses: 30000
Existing EMI amount: 10000
Customer segment: Premium
```

**Expected output or decision:**

```text
Campaign group: Premium Upsell Campaign
```

**Reason for expected output:**

The customer is Premium, savings percentage is 50%, and Mumbai is a target campaign city. Therefore, the customer is assigned to the Premium Upsell Campaign.

---

## Test Case 9: Campaign Eligibility - Cashback Campaign

**Input values:**

```text
Menu choice: 4
City: Jaipur
Monthly income: 30000
Monthly expenses: 22000
Existing EMI amount: 3000
Customer segment: Standard
```

**Expected output or decision:**

```text
Campaign group: Cashback Campaign
```

**Reason for expected output:**

Monthly savings are 5000, so savings percentage is 16.67%. The customer is Standard and has savings percentage above 5%, so the customer is assigned to the Cashback Campaign.

---

## Test Case 10: Invalid Input - Negative Age

**Input values:**

```text
Menu choice: 1
Age: -25
```

**Expected output or decision:**

```text
Invalid input. Value must be at least 15
```

**Reason for expected output:**

Age cannot be negative and the program only accepts age values from 15 to 110 for customer profile input.

---

## Test Case 11: Invalid Input - Credit Score Outside Range

**Input values:**

```text
Menu choice: 3
Credit score: 950
```

**Expected output or decision:**

```text
Invalid input. Value must not be more than 900
```

**Reason for expected output:**

Credit score must be between 300 and 900. A score of 950 is outside the allowed range.

---

## Test Case 12: Invalid Input - Product Quantity Less Than 1

**Input values:**

```text
Menu choice: 2
Quantity: 0
```

**Expected output or decision:**

```text
Invalid input. Value must be at least 1
```

**Reason for expected output:**

Quantity must be at least 1. A product quantity of 0 is invalid.

---

## Test Case 13: Invalid Input - Discount Percentage Above 100

**Input values:**

```text
Menu choice: 2
Discount percentage: 120
```

**Expected output or decision:**

```text
Invalid input. Value must not be more than 100
```

**Reason for expected output:**

Discount percentage cannot be more than 100 because a discount above 100% is not valid.

---

## Test Case 14: Invalid Input - Invalid Customer Segment

**Input values:**

```text
Menu choice: 4
Customer segment: Gold
```

**Expected output or decision:**

```text
Invalid segment. Please enter Standard, Premium, or Enterprise.
```

**Reason for expected output:**

Only Standard, Premium, and Enterprise are accepted as valid customer segments.
