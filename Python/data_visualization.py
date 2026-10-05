"""data_visualization.py - Charts for the CFPB Consumer Financial Complaints dataset."""

import matplotlib.pyplot as plt
import pandas as pd

from data_loading import load_data, create_raw_and_clean
from data_cleaning import (
    remove_duplicates, standardize_column_names, convert_data_types,
    clean_text_columns, clean_state, clean_pipeline,
)
from exploratory_analysis import missing_value_summary, value_counts_for


def plot_missing_values(missing_summary: pd.DataFrame) -> None:
    """Bar chart of missing value percentage per column."""
    missing_plot = missing_summary[missing_summary["Missing Values"] > 0]
    plt.figure(figsize=(12, 6))
    plt.bar(missing_plot.index, missing_plot["Missing Percentage"])
    plt.xlabel("Columns")
    plt.ylabel("Missing Values (%)")
    plt.title("Missing Value Analysis")
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.show()


def plot_vertical_bar(counts: pd.Series, xlabel: str, title: str,
                      top_n: int = 10, rotation: int = 45, figsize=(12, 6)) -> None:
    """Vertical bar chart of the top-N categories."""
    top = counts.head(top_n)
    plt.figure(figsize=figsize)
    plt.bar(top.index, top.values)
    plt.xlabel(xlabel)
    plt.ylabel("Number of Complaints")
    plt.title(title)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.show()


def plot_horizontal_bar(counts: pd.Series, ylabel: str, title: str,
                        top_n: int = 15, figsize=(12, 7)) -> None:
    """Horizontal bar chart of the top-N categories."""
    top = counts.head(top_n)
    plt.figure(figsize=figsize)
    plt.barh(top.index[::-1], top.values[::-1])
    plt.xlabel("Number of Complaints")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_all(clean_df: pd.DataFrame) -> None:
    """Generate all EDA charts from the cleaned dataset."""
    plot_vertical_bar(value_counts_for(clean_df, "product"), "Product",
                      "Top Financial Products by Complaint Volume", top_n=10, rotation=45)
    plot_horizontal_bar(value_counts_for(clean_df, "issue"), "Issue",
                        "Top Complaint Issues", top_n=15)
    plot_horizontal_bar(value_counts_for(clean_df, "sub_issue"), "Sub-Issue",
                        "Top Complaint Sub-Issues", top_n=15)
    plot_vertical_bar(value_counts_for(clean_df, "company"), "Company",
                      "Top Companies by Complaint Volume", top_n=10, rotation=75)
    plot_vertical_bar(value_counts_for(clean_df, "state"), "State",
                      "Top States by Complaint Volume", top_n=15, rotation=0,
                      figsize=(10, 6))


if __name__ == "__main__":
    data = load_data()
    _, working = create_raw_and_clean(data)

    # Missing-value chart uses the dataset BEFORE missing-value treatment (as in the notebook)
    pre = remove_duplicates(working)
    pre = standardize_column_names(pre)
    pre = convert_data_types(pre)
    pre = clean_text_columns(pre)
    pre = clean_state(pre)
    plot_missing_values(missing_value_summary(pre))

    # Remaining charts use the fully cleaned dataset
    clean_data = clean_pipeline(working)
    plot_all(clean_data)