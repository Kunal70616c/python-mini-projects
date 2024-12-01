 #fn for calculation
def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    #using annotation
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate/100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_tax: float = monthly_tax * 12
    yearly_net_income = yearly_salary - yearly_tax
    #printing o/p values
    print('====================================')
    print(f'Monthly Income: {currency} {monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f} %')
    print(f'Monthly Tax: {currency} {monthly_tax:,.2f}')
    print(f'Mothly Net Income: {currency} {monthly_net_income:,.2f}')
    print(f'Yearly Salary: {currency} {yearly_salary:,.2f}')
    print(f'Yearly Tax Paid: {currency} {yearly_tax:,.2f}')
    print(f'Yearly Net Income: {currency} {yearly_net_income:,.2f}')
    print('====================================')

#main fn as the entry-point
def main() -> None:
    #taking i/p 
    monthly_income: float = float(input('Enter Your Monthly Salary:  '))
    tax_rate: float= float(input('Enter TAx Rate (%) :   '))
    #calling function
    calculate_finances(monthly_income,tax_rate,currency='₹')

if __name__ == '__main__':
    main()
