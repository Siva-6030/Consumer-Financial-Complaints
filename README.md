# 🏦 FinGrievance Intelligence

### Root-Cause Mining and Resolution Outcome Prediction from Consumer Complaint Narratives

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-EDA%20Phase-yellow)

---

## 📑 Table of Contents

1. [Industry](#-industry)
2. [Problem Statement](#-problem-statement)
3. [Proposed Solution](#-proposed-solution)
4. [Dataset](#-dataset)
5. [Tools & Technologies](#-tools--technologies)
6. [Project Workflow](#-project-workflow)
7. [Data Analysis & Visualization](#-data-analysis--visualization)
8. [Key Insights](#-key-insights)
9. [Recommendations](#-recommendations)
10. [Visualization Screenshots](#visualization-screenshots)
11. [Project Folder Structure](#-project-folder-structure)
12. [Author](#-author)

---

## 🏭 Industry

**US consumer credit cards (retail banking and consumer lending).**
Product in scope: Credit card (CFPB Consumer Complaint Database, complaints with a narrative).
Companies in focus: Capital One, JPMorgan Chase, Bank of America, Wells Fargo, Citi, Synchrony and Discover *(to be confirmed from the data)*.

---

## ❗ Problem Statement

Credit card issuers receive thousands of consumer complaints every month, mostly as free-text narratives filed under broad Issue labels such as *"Problem with a purchase shown on your statement"* or *"Fees or interest"*. These labels show **where** a complaint belongs, not **why** it happened. A single label can cover unauthorized charges, a merchant dispute, a rewards error, an unexpected interest charge or a closed account.

Issuers such as Capital One, JPMorgan Chase, Bank of America and Synchrony handle similar problems, yet the same root cause can end in monetary relief, non-monetary relief or only an explanation. There is no evidence-based way to check how consistent those outcomes are, and new problems such as a fraud pattern or an app change appear in narratives before they appear in category counts.

---

## 💡 Proposed Solution

An end-to-end NLP system on the credit card complaints in the CFPB database that:

1. Cleans and structures the narratives
2. Discovers root-cause themes with embedding-based topic modeling and tracks them over time
3. Predicts the expected relief probability of each complaint from its narrative using a time-based split
4. Computes a company-level **Relief Gap Score** (observed minus expected relief per company and root cause)
5. Explains predictions with SHAP and presents results in a dashboard

> 📌 **Current stage:** Steps 1 (data cleaning) and exploratory data analysis are completed in this repository. Steps 2–5 are planned future work.

---

## 📦 Dataset

| Item | Detail |
|---|---|
| **Dataset Name** | CFPB Consumer Complaint Database (Consumer Financial Complaints) |
| **Source** | [Consumer Financial Protection Bureau](https://www.consumerfinance.gov/data-research/consumer-complaints/) |
| **Download Link** | <https://files.consumerfinance.gov/ccdb/complaints.csv.zip> |
| **Update Frequency** | Daily |
| **Files** | Raw dataset and cleaned dataset (see folder structure) |

---

## 🛠 Tools & Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## 🔄 Project Workflow

**Industry Selection → Problem Identification → Dataset Collection → Data Cleaning → Data Transformation → Data Analysis → Data Visualization → Insights → Recommendations**

| Stage | Work done in this project |
|---|---|
| **Industry Selection** | US consumer credit cards (retail banking and consumer lending) |
| **Problem Identification** | Broad issue labels do not explain root causes or outcome consistency |
| **Dataset Collection** | CFPB Consumer Complaint Database CSV |
| **Data Cleaning** | Duplicate and missing value checks, column name standardization, text and state cleaning, complaint ID validation, handling of missing values |
| **Data Transformation** | Date and numeric conversion, creation of `response_days` (date sent to company minus date received), negative value check |
| **Data Analysis** | Complaint counts by company, issue, sub-issue, product and state; response time comparison across products |
| **Data Visualization** | Charts listed in the next section |
| **Insights** | See [Key Insights](#-key-insights) |
| **Recommendations** | See [Recommendations](#-recommendations) |

---

## 📊 Data Analysis & Visualization

The following analysis and visualizations were performed in the notebook:

> Click a visualization name to view the image.

<details>
<summary><b>📉 Missing Value Analysis</b></summary>
<br>

<img src="Visualizations/Missing%20Value%20Analysis.png" alt="Missing Value Analysis" width="800">

</details>

<details>
<summary><b>🏢 Top Companies by Complaint Volume</b></summary>
<br>

<img src="Visualizations/Top%20Companies%20by%20Complaint%20Volume.png" alt="Top Companies by Complaint Volume" width="800">

</details>

<details>
<summary><b>⚠️ Top Complaint Issues</b></summary>
<br>

<img src="Visualizations/Top%20Complaint%20Issues.png" alt="Top Complaint Issues" width="800">

</details>

<details>
<summary><b>🔎 Top Complaint Sub-Issues</b></summary>
<br>

<img src="Visualizations/Top%20Complaint%20Sub-Issues.png" alt="Top Complaint Sub-Issues" width="800">

</details>

<details>
<summary><b>💳 Top Financial Products by Complaint Volume</b></summary>
<br>

<img src="Visualizations/Top%20Financial%20Products%20by%20Complaint%20Volume.png" alt="Top Financial Products by Complaint Volume" width="800">

</details>

<details>
<summary><b>🗺️ Top States by Complaint Volume</b></summary>
<br>

<img src="Visualizations/Top%20States%20by%20Complaint%20Volume.png" alt="Top States by Complaint Volume" width="800">

</details>

---

## 🔍 Key Insights

*Add the insights from your notebook output here, using only real numbers. Suggested format:*

- Dataset size after cleaning: `___` rows and `___` columns
- Columns with the most missing values: `___`
- Company with the highest complaint volume: `___` (`___` complaints)
- Most frequent issue: `___`
- Most frequent sub-issue: `___`
- Product with the highest complaint volume: `___`
- State with the highest complaint volume: `___`
- Product with the longest average response time: `___` (`___` days)

---

## ✅ Recommendations

*Write 3–5 short recommendations based only on the insights above. Suggested format:*

1. Based on `[insight]`, issuers should `[action]`.
2. Based on `[insight]`, regulators or analysts should `[action]`.
3. Based on `[insight]`, the next analysis step should be `[action]`.

---

## Visualization Screenshots

> Click a visualization name to view the image.

<details>
<summary><b>📉 Missing Value Analysis</b></summary>
<br>

<img src="https://github.com/Siva-6030/Consumer-Financial-Complaints/blob/main/Visualizations/Missing%20Value%20Analysis.png?raw=true" alt="Missing Value Analysis" width="800">

</details>

<details>
<summary><b>🏢 Top Companies by Complaint Volume</b></summary>
<br>

<img src="https://github.com/Siva-6030/Consumer-Financial-Complaints/blob/main/Visualizations/Top%20Companies%20by%20Complaint%20Volume.png?raw=true" alt="Top Companies by Complaint Volume" width="800">

</details>

<details>
<summary><b>⚠️ Top Complaint Issues</b></summary>
<br>

<img src="https://github.com/Siva-6030/Consumer-Financial-Complaints/blob/main/Visualizations/Top%20Complaint%20Issues.png?raw=true" alt="Top Complaint Issues" width="800">

</details>

<details>
<summary><b>🔎 Top Complaint Sub-Issues</b></summary>
<br>

<img src="https://github.com/Siva-6030/Consumer-Financial-Complaints/blob/main/Visualizations/Top%20Complaint%20Sub-Issues.png?raw=true" alt="Top Complaint Sub-Issues" width="800">

</details>

<details>
<summary><b>💳 Top Financial Products by Complaint Volume</b></summary>
<br>

<img src="https://github.com/Siva-6030/Consumer-Financial-Complaints/blob/main/Visualizations/Top%20Financial%20Products%20by%20Complaint%20Volume.png?raw=true" alt="Top Financial Products by Complaint Volume" width="800">

</details>

<details>
<summary><b>🗺️ Top States by Complaint Volume</b></summary>
<br>

<img src="https://github.com/Siva-6030/Consumer-Financial-Complaints/blob/main/Visualizations/Top%20States%20by%20Complaint%20Volume.png?raw=true" alt="Top States by Complaint Volume" width="800">

</details>
---

## 📁 Project Folder Structure

```text
FinGrievance-Intelligence/
│
├── README.md
│
├── Dataset/
│   ├── complaints.csv                              # Raw CFPB dataset (replace with actual file name)
│   └── cleaned_complaints.csv                      # Cleaned dataset (replace with actual file name)
│
├── Notebook/
│   └── Consumer_Financial_Complaints.ipynb
│
└── Visualizations/
    ├── missing_value_analysis.png
    ├── top_companies.png
    ├── top_issues.png
    ├── top_sub_issues.png
    ├── top_products.png
    └── top_states.png
```

> If the raw CSV is too large for GitHub (over 100 MB), do not upload it. Keep only the download link in the Dataset section.

---

## 🚀 Future Scope

- Filter to credit card complaints with narratives and preprocess text
- Embedding-based topic modeling and trend tracking
- Resolution outcome (relief) prediction with a time-based split
- Company-level Relief Gap Score
- SHAP explainability and dashboard

---

## 👤 Author

| | |
|---|---|
| **Name** | Sivasuriyan Velmurugan |
| **Student ID** | AF05312120 |
| **Organization** | Anudip Foundation |
| **Course** | AIML |
| **Batch Code** | ANPD7444 |

---

⭐ If you find this project useful, consider starring the repository.
