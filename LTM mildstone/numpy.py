
## Coding Assignment: Energy Usage Analyzer## Problem Description
You are tasked with building an EnergyAnalyzer class that processes, validates, metrics-analyzes, and formats household or industrial electricity consumption data. The energy data is passed around and manipulated primarily using standard Python lists and NumPy arrays representing hourly or daily usage values in kilowatt-hours (kWh).
------------------------------

## Class Requirements
## Method 1: create_usage_array

* Signature: def create_usage_array(self, usage_list)
* Description: Converts a standard Python list of numerical energy values into a structured NumPy array.
* Parameters:
* usage_list (list): A list containing numerical energy metrics.
* Returns: A numpy.ndarray with data type explicitly set to np.float64.

------------------------------
## Method 2: validate_usage_array

* Signature: def validate_usage_array(self, usage_array)
* Description: Checks the integrity of the energy array before performing analytical operations.
* Parameters:
* usage_array (numpy.ndarray): The usage data to check.
* Returns: bool. Returns False if the array is empty (size == 0) or if any element contains a negative usage value (< 0). Returns True if it passes both checks.

------------------------------
## Method 3: compute_usage_metrics

* Signature: def compute_usage_metrics(self, usage_array)
* Description: Computes essential summary statistics from the usage data.
* Parameters:
* usage_array (numpy.ndarray): The usage data array.
* Logic: Compute and return a tuple of three values:
* lowest: The minimum usage value, converted to a native Python int.
   * average: The mathematical mean of all usage, rounded to exactly 2 decimal places, as a Python float.
   * spread: The range of the data calculated as (maximum minus minimum), converted to a native Python int.
* Returns: tuple -> (lowest, average, spread)

------------------------------
## Method 4: classify_usage

* Signature: def classify_usage(self, usage_array, low_limit, high_limit)
* Description: Categorizes each individual data point in the array into predefined consumption bands.
* Parameters:
* usage_array (numpy.ndarray): The usage data array.
   * low_limit (number): The lower band boundary.
   * high_limit (number): The upper band boundary.
* Logic: Vectorize the categorization using the boundaries:
* If a value is greater than or equal to high_limit, classify it as "High".
   * If a value is between low_limit (inclusive) and high_limit (exclusive), classify it as "Moderate".
   * If a value is strictly less than low_limit, classify it as "Low".
* Returns: A numpy.ndarray of strings containing "High", "Moderate", or "Low" corresponding to the elements of usage_array.

------------------------------
## Method 5: longest_high_usage_streak

* Signature: def longest_high_usage_streak(self, usage_array, target)
* Description: Finds the maximum consecutive sequence of periods where energy usage matched or exceeded a certain threshold.
* Parameters:
* usage_array (numpy.ndarray): The chronological usage data array.
   * target (number): The target threshold value.
* Returns: int. The length of the longest continuous streak of values where element $\geq$ target.

------------------------------
## Method 6: format_usage_report

* Signature: def format_usage_report(self, usage_array)
* Description: Generates user-friendly textual representations of the numerical data points for reporting purposes.
* Parameters:
* usage_array (numpy.ndarray): The numerical usage metrics array.
* Returns: A numpy.ndarray of strings where each numerical value is truncated or cast to an integer and appended with the text suffix " kWh" (e.g., 25.7 becomes "25 kWh").

------------------------------

import numpy as np 
class EnergyAnalyzer:

    def create_usage_array(self,usage_list):
        return np.array(usage_list,dtype=np.float64)
    
    def validate_usage_array(self,usage_array):
        if usage_array.size==0:
            return False
        elif np.any(usage_array<0):
            return False
        return True
    def compute_usage_metrics(self,usage_array):

        lowest=int(np.min(usage_array))
        average=round(float(np.mean(usage_array)),2)
        maximum=np.max(usage_array)
        spread=int(maximum-lowest)

        return (lowest,average,spread)

    def classify_usage(self, usage_array, low_limit,high_limit):
        return np.where(
            usage_array>=high_limit,"High",
            np.where(usage_array>=low_limit,"Moderate","Low"))
    def longest_high_usage_streak(self,usage_array,target):
        longest=0
        current=0
        for i in range(0,len(usage_array)):
            if usage_array[i]>=target:
                current+=1
            else:
                longest=max(longest,current)
                current=0
        return max(longest,current)
    def format_usage_report(self, usage_array):
        return np.array([f"{int(value)} kWh" for value in usage_array])
        
