# 🏦Consumer-Financial-Complaints

### Root-Cause Mining and Resolution Outcome Prediction from Consumer Complaint Narratives

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Data](https://img.shields.io/badge/Data-CFPB%20CCDB-0A66C2)
![Status](https://img.shields.io/badge/Status-EDA%20Phase-yellow)

> 🚧 **Current stage: Exploratory Data Analysis (EDA) and data cleaning.** NLP modeling, outcome prediction and the dashboard are planned for later phases.

---

## 📑 Table of Contents

1. [Overview](#-overview)
2. [Problem Statement](#-problem-statement)
3. [Project Objectives](#-project-objectives)
4. [Dataset](#-dataset)
5. [EDA Work Completed](#-eda-work-completed)
6. [Tech Stack](#-tech-stack)
7. [Project Structure](#-project-structure)
8. [Installation & Usage](#-installation--usage)
9. [Roadmap](#-roadmap)
10. [Key Findings](#-key-findings)


---

## 🔎 Overview

| Item | Detail |
|---|---|
| **Industry** | US consumer credit cards (retail banking and consumer lending) |
| **Product in scope** | Credit card (complaints with a narrative) |
| **Data source** | CFPB Consumer Complaint Database (updated daily) |
| **Companies in focus** | Capital One, JPMorgan Chase, Bank of America, Wells Fargo, Citi, Synchrony, Discover *(to be confirmed from the data)* |
| **Current phase** | Data cleaning and exploratory analysis |

---

## ❗ Problem Statement

Credit card issuers receive thousands of consumer complaints every month, mostly as free-text narratives filed under broad **Issue** labels such as *"Problem with a purchase shown on your statement"* or *"Fees or interest"*. These labels show **where** a complaint belongs, not **why** it happened. A single label can cover unauthorized charges, a merchant dispute, a rewards error, an unexpected interest charge or a closed account.

Issuers handle similar problems, yet the same root cause can end in monetary relief, non-monetary relief or only an explanation. There is no evidence-based way to check how consistent those outcomes are, and new problems appear in narratives before they appear in category counts.

---

## 🎯 Project Objectives

The full project will:

1. Clean and structure complaint narratives *(in progress, EDA phase)*
2. Discover root-cause themes with embedding-based topic modeling and track them over time
3. Predict expected relief probability from each narrative using a time-based split
4. Compute a company-level **Relief Gap Score** (observed minus expected relief per company and root cause)
5. Explain predictions with SHAP and present results in a dashboard

---

## 📦 Dataset

- **Source:** [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/)
- **Download:** <https://files.consumerfinance.gov/ccdb/complaints.csv.zip>

**Key columns explored**

| Column | Description |
|---|---|
| `complaint_id` | Unique complaint identifier |
| `date_received` / `date_sent_to_company` | Complaint timeline dates |
| `product`, `sub_product` | Financial product category |
| `issue`, `sub_issue` | Broad complaint labels |
| `company` | Company the complaint was filed against |
| `company_response_to_consumer` | How the company closed the complaint (future relief target) |
| `company_public_response` | Optional public response |
| `state`, `zip_code` | Consumer location |
| `submitted_via` | Submission channel |
| `timely_response` | Whether the company responded on time |
| `tags` | Consumer tags (e.g., older American, servicemember) |

> The raw CSV is not committed to this repository because of its size. Download it from the link above and update the path in the notebook.

---

## 🧹 EDA Work Completed

Notebook: [`Consumer_Financial_Complaints.ipynb`](Consumer_Financial_Complaints.ipynb)

| Step | Description |
|---|---|
| **1. Data loading** | Loaded the complaints CSV and checked its shape |
| **2. Raw vs clean copies** | Kept an untouched `raw_data` backup and worked on `clean_data` |
| **3. Structure inspection** | Reviewed columns, data types, dimensions and descriptive statistics |
| **4. Duplicate check** | Checked duplicate rows and duplicate complaint IDs |
| **5. Missing value analysis** | Computed missing counts and percentages per column, with a bar chart |
| **6. Column standardization** | Lowercased names and replaced spaces, hyphens and special characters |
| **7. Date and numeric conversion** | Converted `date_received`, `date_sent_to_company` to datetime and `zip_code` to numeric |
| **8. Text cleaning** | Stripped whitespace from categorical and text columns; standardized `state` to uppercase |
| **9. Feature creation** | Created `response_days` (date sent to company minus date received) and checked for negative values |
| **10. Missing value handling** | Filled `company_public_response`, `tags`, `state`, `zip_code` and `sub_issue` with explicit placeholders |
| **11. Summary statistics** | Counted unique companies, products, issues, sub-issues, states and channels |
| **12. Response time analysis** | Compared mean and median response time across the top products |
| **13. Final verification** | Compared raw vs clean data and confirmed duplicates and missing values |
| **14. Export** | Saved the cleaned dataset to CSV for the next phase |

---

## 🛠 Tech Stack

| Purpose | Tools |
|---|---|
| Language | Python 3.10+ |
| Data analysis | pandas, NumPy |
| Visualization | Matplotlib |
| Environment | Jupyter Notebook |

*Planned for later phases:* sentence-transformers, BERTopic, scikit-learn, LightGBM, SHAP, Streamlit.

---

## 📁 Project Structure

```
Consumer_Financial_Complaints/

│
├── README.md
│
├── Dataset/
│   ├── raw_dataset.csv
│   └── cleaned_dataset.csv
│
├── Notebook/
│   └── Data_Analysis_EDA.ipynb
│
├── Python/
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── data_visualization.py
│
├── Visualizations/
│   ├── distribution_analysis.png
│   ├── trend_analysis.png
│   ├── category_analysis.png
│   └── correlation_analysis.png
│
└── Documentation/
    └── Project_Report.pdf
```

---

## ⚙ Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/Siva-6030/FinGrievance-Intelligence.git
cd FinGrievance-Intelligence

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install pandas numpy matplotlib jupyter

# 4. Download the CFPB CSV, then update the file path in the notebook's load cell

# 5. Run the notebook
jupyter notebook Consumer_Financial_Complaints.ipynb
```

---

## 🗺 Roadmap

| Phase | Description | Status |
|---|---|---|
| 1 | Data loading, cleaning, quality checks, EDA | 🔄 In progress |
| 2 | Filter to credit card complaints with narratives; text preprocessing | ⏳ Planned |
| 3 | Embedding-based topic modeling and trend tracking | ⏳ Planned |
| 4 | Relief outcome prediction (time-based split) | ⏳ Planned |
| 5 | Relief Gap Score by company and root cause | ⏳ Planned |
| 6 | SHAP explainability and dashboard | ⏳ Planned |

---

## 📊 Key Findings

*To be added after the EDA is finalized (dataset size, top issues and companies, missing-value patterns, response-time trends).*

---

## 👤 Author

**Sivasuriyan V**
 Integrated M.Tech (Software Engineering), VIT Vellore

- 🔗 LinkedIn: [linkedin.com/in/sivasuriyan-v](https://www.linkedin.com/in/sivasuriyan-v/)
- 💻 GitHub: [github.com/Siva-6030](https://github.com/Siva-6030/)
- 📧 Email: sivasuriyan662004@gmail.com


⭐ If you find this project useful, consider starring the repository.
