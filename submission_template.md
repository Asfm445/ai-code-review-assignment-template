# AI Code Review Assignment (Python)

## Candidate
- Name: **Awel Abubekar**
- Approximate time spent: **~40 minutes**

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs
- The original implementation divides the sum of non-cancelled orders by the **total number of orders**, including cancelled ones, producing an incorrect average.

### Edge cases & risks
- Empty input list results in division by zero.
- All orders cancelled results in division by zero.
- Missing `status` or `amount` fields may cause runtime errors.

### Code quality / design issues
- The denominator does not reflect the filtered dataset.
- Lacks defensive handling for empty or invalid inputs.

---

## 2) Proposed Fixes / Improvements

### Summary of changes
- Track the count of **non-cancelled orders only**.
- Prevent division by zero when no valid orders exist.
- Access dictionary fields defensively.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations
- Empty orders list.
- All orders cancelled.
- Mixed cancelled and non-cancelled orders.
- Orders with missing or zero amounts.

---

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Claims division is done using non-cancelled orders, which is incorrect.
- States cancelled orders are correctly excluded, which is misleading.

### Rewritten explanation
- The function calculates the average order value by summing amounts from non-cancelled orders and dividing by the number of such orders. It safely handles empty inputs and cases where no valid orders exist by avoiding division by zero.

---

## 4) Final Judgment
- Decision: **Request Changes**
- Justification: Core logic error affecting correctness.
- Confidence & unknowns: High confidence after fix; assumes basic order schema.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs
- Any string containing `@` is treated as a valid email, leading to false positives.

### Edge cases & risks
- Non-string inputs (e.g., `None`, integers) cause runtime errors.
- Invalid formats such as `@example` or `test@` are incorrectly counted as valid.

### Code quality / design issues
- Validation logic is overly simplistic for the stated purpose.

---

## 2) Proposed Fixes / Improvements

### Summary of changes
- Ensure inputs are strings.
- Require exactly one `@`.
- Enforce non-empty local and domain parts.
- Apply minimal domain structure validation.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations
- Valid and invalid email formats.
- Inputs containing non-string values.
- Empty input list.
- Emails with malformed domains.

---

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Overstates correctness and safety of the validation logic.
- Does not reflect actual behavior of the code.

### Rewritten explanation
- The function counts email addresses that meet basic structural validity requirements while safely ignoring invalid or non-string inputs, without attempting full RFC-level validation.

---

## 4) Final Judgment
- Decision: **Request Changes**
- Justification: Incorrect validation logic and misleading explanation.
- Confidence & unknowns: High confidence for basic structural validation.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs
- The original implementation divides by the total number of inputs instead of the number of valid measurements.

### Edge cases & risks
- Raises exceptions when values cannot be converted to floats.
- Empty input or all-invalid input leads to division by zero.

### Code quality / design issues
- Assumes all non-None values are numeric and safely convertible.

---

## 2) Proposed Fixes / Improvements

### Summary of changes
- Count only valid, convertible measurements.
- Safely ignore invalid or non-numeric values.
- Prevent division by zero when no valid data exists.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
- Mixed numeric and non-numeric inputs.
- All values are `None`.
- Empty input list.
- String representations of numbers.

---

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average.

### Issues in original explanation
- Claims accurate averaging while using an incorrect denominator.
- States safe handling of mixed input types, which was not true.

### Rewritten explanation
- The function computes the average of valid numeric measurements by ignoring missing or invalid values and safely handling mixed input types.

---

## 4) Final Judgment
- Decision: **Request Changes**
- Justification: Logic and safety issues affecting correctness.
- Confidence & unknowns: High confidence after correction.
