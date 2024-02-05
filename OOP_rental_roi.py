class ROI:
    def __init__(self, cost):
        self.cost = cost
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0
        self.investments = 0
        self.annual_cash_flow = 0
        self.roi = 0

# calculate income by adding inputs for all sub categories
    
    def calculateIncome(self, rental_income, laundry, storage, misc):
        self.income = rental_income + laundry + storage + misc

# calculate expenses by adding inputs for all sub categories
    def calculateExpenses(self, taxes, insurance, utilities, repairs, property_management, hoa_fees, vacancy_costs, mortgage_expenses):
        self.expenses = taxes + insurance + utilities + repairs + property_management + hoa_fees + vacancy_costs + mortgage_expenses

# cash flow is income-expenses costs are broken into monthly costs
    def calculateCashFlow(self):
        self.cash_flow = self.income - self.expenses

# calculate investments by adding inputs for all sub categories
    def calculateInvestments(self, down_payment, closing_costs, repair_budget, other_investments):
        self.investments = down_payment + closing_costs + repair_budget + other_investments

# annual cash flow are monthly cash flow costs* 12
    def calculateAnnualCashFlow(self):
        self.annual_cash_flow = self.cash_flow * 12

# ROI is annual cashflow/ investments, show percentage of ROI
    def calculateROI(self):
        if self.investments != 0:
            self.roi = (self.annual_cash_flow / self.investments) * 100
        else:
            print("Investments should be greater than 0 to calculate ROI.")


# Instantiating ROI
            
property_cost = float(input("Enter the cost of the rental property: $"))
property_roi = ROI(property_cost)

# Income inputs
print("Please enter income costs.")
property_roi.calculateIncome(    
    float(input("Enter rental income: $")),
    float(input("Enter laundry income: $")),
    float(input("Enter storage income: $")),
    float(input("Enter miscellaneous income: $"))
)

# Expense inputs
print("Please enter expense costs.")
property_roi.calculateExpenses(
    float(input("Enter taxes: $")),
    float(input("Enter insurance: $")),
    float(input("Enter utilities: $")),
    float(input("Enter repairs: $")),
    float(input("Enter property management fees: $")),
    float(input("Enter HOA fees: $")),
    float(input("Enter vacancy costs: $")),
    float(input("Enter mortgage expenses: $"))
)

# Investment inputs
print("Please enter investment costs.")
property_roi.calculateCashFlow()
property_roi.calculateInvestments(
    float(input("Enter down payment: $")),
    float(input("Enter closing costs: $")),
    float(input("Enter repair budget: $")),
    float(input("Enter other investments: $"))
)

# Calcumalations
property_roi.calculateAnnualCashFlow()
property_roi.calculateROI()


# print out summary
print(f"Property Cost: ${property_roi.cost}")
print(f"Income: ${property_roi.income}")
print(f"Expenses: ${property_roi.expenses}")
print(f"Cash Flow: ${property_roi.cash_flow}")
print(f"Investments: ${property_roi.investments}")
print(f"Annual Cash Flow: ${property_roi.annual_cash_flow}")
print(f"ROI: {property_roi.roi}%")







# IGNORE BELOW CODE

# class ROI:
#     def __init__(self, cost):
#         self.cost = cost
#         self.income = 0
#         self.expenses = 0
#         self.cash_flow = 0
#         self.investments = 0
#         self.annual_cash_flow = 0
#         self.roi = 0

#     def incomeInput(self):
#         self.income = float(input("Enter rental income: "))
#         self.income += float(input("Enter laundry income: "))
#         self.income += float(input("Enter storage income: "))
#         self.income += float(input("Enter miscellaneous income: "))

#     def expensesInput(self):
#         self.expenses = float(input("Enter taxes: "))
#         self.expenses += float(input("Enter insurance: "))
#         self.expenses += float(input("Enter utilities: "))
#         self.expenses += float(input("Enter repairs: "))
#         self.expenses += float(input("Enter property management fees: "))
#         self.expenses += float(input("Enter HOA fees: "))
#         self.expenses += float(input("Enter vacancy costs: "))
#         self.expenses += float(input("Enter mortgage expenses: "))

#     def cashFlow(self):
#         self.cash_flow = self.income - self.expenses

#     def investmentInput(self):
#         self.investments = float(input("Enter down payment: "))
#         self.investments += float(input("Enter closing costs: "))
#         self.investments += float(input("Enter repair budget: "))
#         self.investments += float(input("Enter other investments: "))

#     def annualCashFlow(self):
#         self.annual_cash_flow = self.cash_flow * 12

#     def calculateROI(self):
#         if self.investments != 0:
#             self.roi = (self.annual_cash_flow / self.investments) * 100
#         else:
#             print("Error: Investments cannot be zero.")

# # Instantiate ROI
            
# property_cost = float(input("Enter the cost of the property: "))
# property_roi = ROI(property_cost)

# property_roi.incomeInput()
# property_roi.expenseInput()
# property_roi.cashFlow()
# property_roi.investmentsInput()
# property_roi.annualCashFlow()
# property_roi.calculateROI()

# print("ROI:", property_roi.roi, "%")