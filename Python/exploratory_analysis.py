"""exploratory_analysis.py - EDA for the CFPB Consumer Financial Complaints dataset."""

import pandas as pd

from data_loading import load_data, create_raw_and_clean
from data_cleaning import clean_pipeline, standardize_column_names, remove_duplicates


def missing_value_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Missing value count and percentage per column."""
    return pd.DataFrame({
        "Missing Values": df.isnull().sum(),
        "Missing Percentage": (df.isnull().sum() / len(df) * 100).round(2),
    })


def descriptive_statistics(df: pd.DataFrame):
    """Numeric and string descriptive statistics."""
    return df.describe().T, df.describe(include="string").T


def value_counts_for(df: pd.DataFrame, column: str) -> pd.Series:
    """Value counts for a column (product, issue, sub_issue, company, state)."""
    return df[column].value_counts()


def data_quality_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Summary table of key data quality metrics."""
    return pd.DataFrame({
        "Metric": [
            "Total Records", "Total Columns", "Duplicate Rows",
            "Missing Values", "Unique Complaint IDs", "Negative Response Days",
        ],
        "Value": [
            len(df), len(df.columns), df.duplicated().sum(),
            df.isnull().sum().sum(), df["complaint_id"].nunique(),
            (df["response_days"] < 0).sum(),
        ],
    })


def run_eda(df: pd.DataFrame) -> dict:
    """Run all EDA steps and return results."""
    results = {
        "missing_summary": missing_value_summary(df),
        "product_counts": value_counts_for(df, "product"),
        "issue_counts": value_counts_for(df, "issue"),
        "sub_issue_counts": value_counts_for(df, "sub_issue"),
        "company_counts": value_counts_for(df, "company"),
        "state_counts": value_counts_for(df, "state"),
        "quality_summary": data_quality_summary(df),
    }
    numeric_stats, string_stats = descriptive_statistics(df)
    results["numeric_stats"] = numeric_stats
    results["string_stats"] = string_stats

    print("Descriptive statistics (numeric):\n", numeric_stats)
    print("\nDescriptive statistics (string):\n", string_stats)
    print("\nTop 10 products:\n", results["product_counts"].head(10))
    print("\nTop 15 issues:\n", results["issue_counts"].head(15))
    print("\nTop 20 sub-issues:\n", results["sub_issue_counts"].head(20))
    print("\nTop 15 companies:\n", results["company_counts"].head(15))
    print("\nTop 15 states:\n", results["state_counts"].head(15))
    print("\nData quality summary:\n", results["quality_summary"])
    return results


if __name__ == "__main__":
    data = load_data()
    _, clean_data = create_raw_and_clean(data)
    clean_data = clean_pipeline(clean_data)
    run_eda(clean_data)