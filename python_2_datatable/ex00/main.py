"""Tester script for Exercise 00 (Load my DB) of Module 02 (DataTable)."""

from load_csv import load


def main() -> None:
    """Main execution function to test load function with valid and invalid inputs."""
    print("--- Test 1: Valid Dataset ---")
    df = load("life_expectancy_years.csv")
    if df is not None:
        print(df.head())

    print("\n--- Test 2: Invalid File Path ---")
    load("nonexistent_file.csv")

    print("\n--- Test 3: Invalid Path Type ---")
    load(12345)  # type: ignore


if __name__ == "__main__":
    main()
