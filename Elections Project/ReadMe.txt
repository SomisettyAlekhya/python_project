# Election Results Analysis

This Python project reads multiple election result text files (2004, 2009, 2014), analyzes the data, and saves the summary to an Excel file. The data includes candidate names, gender, party affiliations, votes, and constituencies.

---

## Input Files

Expected file format for each text file (`Elections2004.txt`, etc.):

Each line should follow this pattern:

<row_number> <Constituency> <Candidate1> <Gender1> <Party1> <Votes1> <Candidate2> <Gender2> <Party2> <Votes2>

markdown
Copy
Edit

---

## Features

1. Parsing Election Files
- Extracts candidate details (name, gender, party, votes) from election result text files.
- Supports elections for years: **2004**, **2009**, and **2014**.

2. Election Analysis
- Calculates total **seats won by each party**.
- Identifies **highest margin winner**.
- Extracts total number of **female candidates** and **female winners**.

3. Excel Output
All results are saved into an Excel workbook named: `Election_Results_Analysis.xlsx`

The workbook contains:
- `Elections2004`, `Elections2009`, `Elections2014`: Raw parsed data per year
- `Seats Won`: Count of seats won by each political party
- `Highest Margin Winner`: Candidate who won with the highest vote margin
- `Female Candidates`: Total female contestants and winners

---

## Requirements

Install required packages via pip:

```bash
pip install pandas openpyxl