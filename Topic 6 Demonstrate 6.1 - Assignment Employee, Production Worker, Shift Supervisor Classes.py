class Employee:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    # Accessor methods
    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    # Mutator methods
    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self._number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self._shift_number = shift_number
        self._hourly_pay_rate = hourly_pay_rate

    # Accessor methods
    def get_shift_number(self):
        return self._shift_number

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    # Mutator methods
    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self._hourly_pay_rate = hourly_pay_rate


class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, annual_bonus):
        super().__init__(name, number)
        self._annual_salary = annual_salary
        self._annual_bonus = annual_bonus

    # Accessor methods
    def get_annual_salary(self):
        return self._annual_salary

    def get_annual_bonus(self):
        return self._annual_bonus

    # Mutator methods
    def set_annual_salary(self, annual_salary):
        self._annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self._annual_bonus = annual_bonus


# Demonstrate the classes
def main():
    # Create a ProductionWorker object
    name = input("Enter the production worker's name: ")
    number = input("Enter the production worker's number: ")
    shift_number = int(input("Enter the shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter the hourly pay rate: "))

    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)

    print("\nProduction Worker Details:")
    print(f"Name: {worker.get_name()}")
    print(f"Number: {worker.get_number()}")
    print(f"Shift Number: {worker.get_shift_number()}")
    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")

    # Create a ShiftSupervisor object
    name = input("\nEnter the shift supervisor's name: ")
    number = input("Enter the shift supervisor's number: ")
    annual_salary = float(input("Enter the annual salary: "))
    annual_bonus = float(input("Enter the annual bonus: "))

    supervisor = ShiftSupervisor(name, number, annual_salary, annual_bonus)

    print("\nShift Supervisor Details:")
    print(f"Name: {supervisor.get_name()}")
    print(f"Number: {supervisor.get_number()}")
    print(f"Annual Salary: ${supervisor.get_annual_salary():.2f}")
    print(f"Annual Bonus: ${supervisor.get_annual_bonus():.2f}")


if __name__ == "__main__":
    main()
