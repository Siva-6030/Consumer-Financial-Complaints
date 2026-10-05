"""data_cleaning.py - Clean the CFPB Consumer Financial Complaints dataset."""

import pandas as pd

from data_loading import load_data, create_raw_and_clean, CLEAN_DATA_PATH

TEXT_COLUMNS = [
    "product", "sub_product", "issue", "sub_issue",
    "company_public_response", "company", "state", "tags",
    "submitted_via", "company_response_to_consumer", "timely_response",
]


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows only if they exist."""
    duplicate_count = df.duplicated().sum()
    print("Number of duplicate rows:", duplicate_count)
    if duplicate_count > 0:
        df = df.drop_duplicates()
        print("Duplicate rows removed.")
    else:
        print("No duplicate rows found.")
    return df


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase, strip and snake_case all column names."""
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace("?", "", regex=False)
    )
    print("Updated Column Names:\n")
    for i, column in enumerate(df.columns, start=1):
        print(f"{i} -> {column}")
    return df


def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """Convert date columns to datetime and zip_code to int."""
    df = df.copy()
    df["date_received"] = pd.to_datetime(df["date_received"], errors="coerce")
    df["date_sent_to_company"] = pd.to_datetime(df["date_sent_to_company"], errors="coerce")
    df["zip_code"] = pd.to_numeric(df["zip_code"], errors="coerce").fillna(0).astype(int)
    print(df[["date_received", "date_sent_to_company", "zip_code"]].dtypes)
    return df


def clean_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Cast text columns to string dtype and strip whitespace."""
    df = df.copy()
    for column in TEXT_COLUMNS:
        df[column] = df[column].astype("string").str.strip()
    print("Text columns cleaned successfully.")
    return df


def clean_state(df: pd.DataFrame) -> pd.DataFrame:
    """Uppercase and strip the state column."""
    df = df.copy()
    df["state"] = df["state"].str.upper().str.strip()
    return df


def validate_complaint_ids(df: pd.DataFrame) -> None:
    """Report complaint ID uniqueness."""
    print("Total Complaint Records:", len(df))
    print("Unique Complaint IDs:", df["complaint_id"].nunique())
    print("Duplicate Complaint IDs:", df["complaint_id"].duplicated().sum())


def treat_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values in categorical columns with meaningful labels."""
    df = df.copy()
    df["company_public_response"] = df["company_public_response"].fillna("Not Provided")
    df["tags"] = df["tags"].fillna("No Tag")
    df["state"] = df["state"].fillna("Unknown")
    df["sub_issue"] = df["sub_issue"].fillna("Not Specified")
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create response_days and year features."""
    df = df.copy()
    df["response_days"] = (df["date_sent_to_company"] - df["date_received"]).dt.days
    print(df[["date_received", "date_sent_to_company", "response_days"]].head())
    print("Negative response-time records:", (df["response_days"] < 0).sum())
    df["year"] = df["date_received"].dt.year
    return df


def final_quality_check(df: pd.DataFrame, title: str = "FINAL DATA QUALITY CHECK") -> None:
    """Print final data quality metrics."""
    print("=" * 70)
    print(title)
    print("=" * 70)
    print("\nRows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("\nDuplicate Rows:", df.duplicated().sum())
    print("\nTotal Missing Values:", df.isnull().sum().sum())
    print("\nUnique Complaint IDs:", df["complaint_id"].nunique())
    print("\nNegative Response Days:", (df["response_days"] < 0).sum())


def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Run the full cleaning pipeline in notebook order."""
    df = remove_duplicates(df)
    df = standardize_column_names(df)
    df = convert_data_types(df)
    df = clean_text_columns(df)
    df = clean_state(df)
    validate_complaint_ids(df)
    df = treat_missing_values(df)
    df = engineer_features(df)
    final_quality_check(df)
    return df


def save_clean_data(df: pd.DataFrame, path: str = CLEAN_DATA_PATH) -> None:
    """Save the cleaned dataset to CSV."""
    df.to_csv(path, index=False)
    print("Cleaned dataset saved successfully.")


if __name__ == "__main__":
    data = load_data()
    raw_data, clean_data = create_raw_and_clean(data)
    clean_data = clean_pipeline(clean_data)
    save_clean_data(clean_data)