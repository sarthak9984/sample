class EmployeeTrainingTracker:
    def __init__(self):
        self.training_records = []

    # 1. Add training record
    def add_training_record(self, employee, hours):
        hours = float(hours)
        if hours < 0:
            raise ValueError("Value must be non-negative")
        self.training_records.append((employee, hours))

    # 2. Get unique participating employees
    def participating_employees(self):
        ans = set()
        for i in self.training_records:
            ans.add(i[0])
        return ans

    # 3. Total training hours of all employees
    def total_training_hours(self):
        total = 0.0
        for i in self.training_records:
             total += i[1]
        return round(total, 2)

    # 4. Average training hours of one employee
    def average_training_hours(self, employee):
        l = []
        for i in self.training_records:
            if i[0] == employee:
                l.append(i[1])
        if len(l) == 0:
            return 0.0
        return round(sum(l) / len(l), 2)

    # 5. Total hours of one employee
    def employee_total_hours(self, employee):
        total = 0.0
        for i in self.training_records:
            if i[0] == employee:
                total += i[1]
        return round(total, 2)

    # 6. Highest training hours record
    def highest_training_hours(self):
        if len(self.training_records) == 0:
            return None
        highest = self.training_records[0]

        for i in self.training_records:
            if i[1] > highest[1]:
                highest = i
        return highest

    # 7. Count records of one employee
    def count_records_for_employee(self, employee):
        count = 0
        for i in self.training_records:
            if i[0] == employee:
                count += 1

        return count
