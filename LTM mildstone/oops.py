## Problem Statement: Employee Training Hours Tracker
### Scenario
A corporate learning department conducts multiple training programs to enhance employee skills. Employees attend various training sessions throughout the year, and the organization logs the exact number of hours spent in training. To manage this growing database cleanly, you are required to implement a robust, automated tracking system.

### Objective
Design a Python class named `EmployeeTrainingTracker` that models this management system using native Python data structures (`lists`, `tuples`, and `sets`). 

---

## 🏗️ Class Specification & Requirements

### 1. Class Attributes
* **Class Name:** `EmployeeTrainingTracker`
* **Instance Attribute:** `training_records` 
  * Type: `list` of `tuples`.
  * Structure: Each element must be a tuple formatted as `(employee_name, training_hours)`.
  * Records must maintain chronological order (the exact order they are added).

### 2. Methods to Implement=======================================================================

#### Method A: `__init__(self)`
* **Description:** Constructor to initialize the tracking system.
* **Logic:** Initialize the `training_records` instance attribute as an empty list.

#### Method B: `add_training_record(self, employee, hours)`
* **Description:** Appends a new training session to the system database.
* **Logic:** 
  1. Convert the `hours` argument to a `float` (the input may be an `int`, `float`, or numeric `str`).
  2. If the converted value is strictly negative (less than 0), raise a `ValueError`. Do **not** append anything to the record list if an error occurs.
  3. Otherwise, append the tuple `(employee, hours)` to `training_records`.

#### Method C: `participating_employees(self)`
* **Description:** Identifies all unique corporate learners.
* **Logic:** Extract all unique employee names currently stored inside `training_records`.
* **Returns:** A Python `set` of strings. Returns an empty set `set()` if no records exist.

#### Method D: `average_training_hours(self, employee)`
* **Description:** Calculates individual training metrics.
* **Logic:** Compute the arithmetic mean of all training hours logged specifically for the requested `employee`.
Round the final answer mathematically to **exactly 2 decimal places**. If the employee has zero logs in the system, return `0.0`.

#### Method E: `total_training_hours(self)`
* **Description:** Computes organizational training volume.
* **Logic:** Sum together all training hours recorded across the entire company. Round the final result to **exactly 2 decimal places**. If the system contains no logs at all, return `0.0`.

---

## ⚙️ Constraints
* Do **not** print output or include `print()` statements inside any of your class methods.
* Do **not** import external or third-party libraries. Use only built-in functions.
* Any testing code or operational driver scripts must be safely enclosed inside `if __name__ == "__main__":`.

---

## 💡 Verified Python Solution

```python
class EmployeeTrainingTracker:

    def __init__(self):
        self.training_records = []

    def add_training_record(self, employee, hours):
        hours_float = float(hours)
        if hours_float < 0:
            raise ValueError("Training hours cannot be negative.")
        self.training_records.append((employee, hours_float))

    def participating_employees(self):
        return {record[0] for record in self.training_records}

    def average_training_hours(self, employee):
        hours_list = [
            record[1]
            for record in self.training_records
            if record[0] == employee
        ]
        if not hours_list:
            return 0.0
        return round(sum(hours_list) / len(hours_list), 2)

    def total_training_hours(self):
        if not self.training_records:
            return 0.0
        total = sum(record[1] for record in self.training_records)
        return round(total, 2)


if __name__ == "__main__":
    # Test your class code here
    tracker = EmployeeTrainingTracker()
    tracker.add_training_record("John", 8.5)
    tracker.add_training_record("Sarah", "6.0")
    tracker.add_training_record("John", 4.5)

    print("Unique Employees:", tracker.participating_employees())
    print("John's Average Hours:", tracker.average_training_hours("John"))
    print("Total Corporate Hours:", tracker.total_training_hours())
```
