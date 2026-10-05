"""data_loading.py - Load the CFPB Consumer Financial Complaints dataset."""

import pandas as pd

# -> Update these paths if your folder structure changes
DATA_PATH = r"D:\AI & ML\Consumer_Financial_Complaints\Dataset\Consumer Financial Complaints.csv"
CLEAN_DATA_PATH = r"D:\AI & ML\Consumer_Financial_Complaints\Dataset\Consumer_Financial_Complaints_Cleaned.csv"


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the consumer financial complaints dataset."""
    data = pd.read_csv(path)
    print("Dataset loaded successfully.")
    print("Dataset Shape:", data.shape)
    return data


def create_raw_and_clean(data: pd.DataFrame):
    """Create raw (untouched) and clean (working) copies of the dataset."""
    raw_data = data.copy()
    clean_data = data.copy()
    print("Raw dataset shape:", raw_data.shape)
    print("Clean dataset shape:", clean_data.shape)
    return raw_data, clean_data


def inspect_dataset(df: pd.DataFrame) -> None:
    """Preview dataset, dimensions, data types, nulls and column names."""
    print("Consumer Financial Complaints Dataset Information")
    print("=" * 60)
    print(df.head())
    print()
    df.info()
    print("\nNumber of Rows:", df.shape[0])
    print("Number of Columns:", df.shape[1])
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing values per column:")
    print(df.isna().sum())
    print("\nColumns in the dataset:\n")
    for i, column in enumerate(df.columns, start=1):
        print(i, "->", column)
    print("\nStatistical summary:")
    print(df.describe(include="all").T)


if __name__ == "__main__":
    data = load_data()
    raw_data, clean_data = create_raw_and_clean(data)
    inspect_dataset(clean_data)