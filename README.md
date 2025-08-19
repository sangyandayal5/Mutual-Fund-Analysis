# 📊 Mutual Fund NAV & Returns Tracker

## 🔎 Introduction

This is a Python-based tool that helps you analyze Mutual Fund NAV (Net Asset Value) trends for multiple schemes.

With this tool, you can:

- Fetch the current NAV of a scheme.
- Find the highest and lowest NAV in the last 52 weeks.
- Calculate returns for 1 week, 2 weeks, 3 weeks, and 1 month.
- Sort all results based on a chosen return period (e.g., sort by best 1-week returns).
- Save the final output neatly into a .json file for later use.

👉 This is useful if you want to quickly compare multiple Mutual Funds’ short-term performance without manually checking each scheme on different websites.

## ⚙️ Setup Instructions

Follow these steps carefully:

1. **Create Files and Folders**

   Make a folder on your computer, e.g., `mf-tracker/`.

   Inside this folder, create a file named:

   - `main.py` → Copy the Python code I provided into this file.

2. **Install Requirements**

   You need Python installed on your computer.

   Then, install the required library:
   `pip install requests`
This library allows the code to fetch data from the MF API.

3. **Run the Program**

Inside the folder where you saved `main.py`, open a terminal and 
Run the script with:
`python main.py`


## 🖥️ Usage Guide (Step by Step)

When the program runs, it will ask for inputs step by step:

### Enter MF Scheme Codes

Example: `119597` (every scheme has a unique code from [mfapi.in](https://mfapi.in)).

Keep entering one by one.

When you are done, type `STOP`.

### Choose Sorting Parameter

After `STOP`, the program will ask how to sort results.

Options are:

- `1w` → sort by 1-week returns
- `2w` → sort by 2-week returns
- `3w` → sort by 3-week returns
- `1m` → sort by 1-month returns

👉 Example: if you type `1m`, results will be sorted by 1-month performance.

### Choose File Name

Enter the name of the file where results should be saved, e.g.:

`results.json`

The file will be created in the same folder.

## 📂 Example of Final JSON Output

```json
[
{
   "scheme_name": "Sundaram Financial Services Opportunities Fund Direct Plan - Growth",
   "scheme_code": 119597,
   "current_nav": 115.67,
   "max_nav_52weeks": 120.7394,
   "min_nav_52weeks": 99.6488,
   "1_week_return_percent": 0.39,
   "2_week_return_percent": 1.12,
   "3_week_return_percent": -0.5,
   "1_month_return_percent": -4.13
},
{
   "scheme_name": "Mirae Asset Large & Midcap Fund - Direct Plan - Growth",
   "scheme_code": 118834,
   "current_nav": 160.45,
   "max_nav_52weeks": 175.368,
   "min_nav_52weeks": 141.099,
   "1_week_return_percent": 1.35,
   "2_week_return_percent": 2.1,
   "3_week_return_percent": 3.0,
   "1_month_return_percent": -1.92
}
]

