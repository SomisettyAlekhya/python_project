#  Bike Purchase Data Analysis using openpyxl

This Python script analyzes an Excel dataset (`bikers.xlsx`) to extract insights about bike purchases, income distribution, regional representation, and gender-based purchase behavior.

##  Input File

- **File:** `bikers.xlsx`
- **Sheet Name:** `bike_buyers`

The Excel sheet should include at least the following columns:
- `Purchased Bike` (values: "Yes" or "No")
- `Income` (currency-formatted values, e.g., `$45,000`)
- `Region` (e.g., "Europe", "Pacific", etc.)
- `Gender` ("M" or "F")

---

##  Functionality

The script performs the following tasks:

1.  Average Income Calculation
- **Average income of buyers** who purchased a bike.
- **Average income of non-buyers** who didn’t purchase a bike.

2.  Regional Representation
- **How many unique regions** are represented.
- **Number of buyers per region**.

3.  Region-wise Purchase Percentage
- For each region, calculates the **percentage of citizens** who purchased a bike.

4.  Gender-based Purchase Analysis
- Calculates **percentage of males and females** who purchased a bike.

---

##  Dependencies

- `openpyxl`

Install with:

```bash
pip install openpyxl

------------------------------------------------------------------------------------------------------------------------

# Bike Purchase Analysis using Pandas

This Python project uses the `pandas` library to analyze bikers' purchase behavior and demographic trends from an Excel sheet (`bikers.xlsx`). The dataset includes details like income, region, gender, and whether the person purchased a bike.

---

## Input File

- **File Name**: `bikers.xlsx`
- Expected Columns:
  - `Purchased Bike` (values: "Yes" or "No")
  - `Income` (e.g., `$45,000`)
  - `Region` (e.g., Europe, Pacific, etc.)
  - `Gender` (M or F)

---

##  Features

1. Average Income Analysis
- Calculates the **average income** of:
  - People who **purchased** a bike.
  - People who **did not purchase** a bike.

2. Regional Insights
- Displays **total number of individuals** per region.
- Calculates the **percentage of people who purchased** bikes from each region.

3. Gender-based Purchase Analysis
- Shows the **percentage of males and females** who purchased bikes.

---

## Dependencies

Ensure you have the required package installed:

```bash
pip install pandas openpyxl

