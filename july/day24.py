def get_loan_schedule(loan_amount, annual_rate, monthly_payment):
    balances = [loan_amount]
    current_balance = loan_amount
    
    monthly_rate = (annual_rate / 100) / 12
    
    while current_balance > 0:
        interest = current_balance * monthly_rate
        current_balance += interest
        
        current_balance -= monthly_payment
        
        if current_balance < 0:
            current_balance = 0
            
        balances.append(round(current_balance))
        
    return balances

