# Problem Statement: Vehicle Rental Usage Analyzer

## Objective
Implement six Python functions using Pandas to analyze vehicle and rental transaction data from CSV files. 

## Dataset Description
* **`Vehicles.csv`**: Contains `VehicleID`, `VehicleName`, `Brand`, and `Category`.
* **`RentalLog.csv`**: Contains `RentalID`, `CustomerID`, `VehicleID`, `PickupDate`, and `DropoffDate`.
---
## Functions to Implement-->>>>>

### Function 1: `load_data(vehicles_path, rentals_path)`
* **Logic**: Read both CSV files using `pd.read_csv`.
* **Returns**: A tuple of two DataFrames: `(vehicles_df, rentals_df)`

### Function 2: `clean_and_convert(rentals_df)`
* **Logic**: Remove leading and trailing whitespace from text columns using `.str.strip()`.
    Convert `PickupDate` and `DropoffDate` to datetime using `pd.to_datetime()`.
* **Returns**: Cleaned `rentals_df`

### Function 3: `merge_data(vehicles_df, rentals_df)`
* **Logic**: Perform an inner merge on the `VehicleID` column using `pd.merge()`.
* **Returns**: Merged DataFrame

### Function 4: `add_rental_duration(merged_df)`
* **Logic**: Calculate `DropoffDate - PickupDate`.
   Extract days using `.dt.days` and store the result in a new column named `RentalDuration`.
* **Returns**: Updated DataFrame with `RentalDuration`

### Function 5: `compute_summary(updated_df)`
* **Logic**: Compute metrics and return a dictionary with keys:
  * `"total_rentals"`: Total transactions using `len()`
  * `"unique_customers"`: Number of unique customers using `nunique()`
  * `"most_rented_vehicle"`: Most rented vehicle using `value_counts()` on `VehicleName`
  * `"top_customer"`: Top customer using `value_counts()` on `CustomerID`
  * `"avg_duration"`: Average rental duration rounded to 1 decimal place

### Function 6: `filter_long_rentals(merged_df, threshold=10)`
* **Logic**: Create a boolean mask `merged_df["RentalDuration"] >= threshold`. 
    Filter the DataFrame and return matching `RentalID` values as a Python list.
* **Returns**: List of strings (e.g., `["R003", "R007", ...]`)

---

## Constraints
* Must use Pandas operations.
* No function should contain print statements.
* Write input/output testing code inside `if __name__ == "__main__":`.


---------------------------------------------------------------------------------------------------------------
import pandas as pd


def load_data(vehicles_path, rentals_path):
    vehicles_df = pd.read_csv(vehicles_path)
    rentals_df = pd.read_csv(rentals_path)
    return vehicles_df, rentals_df

def clean_and_convert(rentals_df):
    for col in rentals_df.select_dtypes(include=["object"]).columns:
        rentals_df[col] = rentals_df[col].str.strip()
    rentals_df["PickupDate"] = pd.to_datetime(rentals_df["PickupDate"])
    rentals_df["DropoffDate"] = pd.to_datetime(rentals_df["DropoffDate"])
    return rentals_df

def merge_data(vehicles_df, rentals_df):
    return pd.merge(vehicles_df, rentals_df, on="VehicleID", how="inner")

def add_rental_duration(merged_df):
    merged_df["RentalDuration"] = (
        merged_df["DropoffDate"] - merged_df["PickupDate"]
    ).dt.days
    return merged_df

def compute_summary(updated_df):
    return {
        "total_rentals": len(updated_df),
        "unique_customers": updated_df["CustomerID"].nunique(),
        "most_rented_vehicle": updated_df["VehicleName"].value_counts().idxmax(),
        "top_customer": updated_df["CustomerID"].value_counts().idxmax(),
        "avg_duration": round(float(updated_df["RentalDuration"].mean()), 1),
    }


def filter_long_rentals(merged_df, threshold=10):
    return merged_df[merged_df["RentalDuration"] >= threshold][
        "RentalID"
    ].tolist()


if __name__ == "__main__":
    pass

