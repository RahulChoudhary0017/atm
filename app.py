from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy balance data (normally from database)
user_balances = {
    "1234567890": 5000,
    "0987654321": 10000
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_balance', methods=['GET', 'POST'])
def check_balance():
    balance = None
    account = None
    error = None
    if request.method == 'POST':
        account = request.form['account']
        balance = user_balances.get(account)
        if balance is None:
            error = 'Account not found!'
    return render_template('check_balance.html', balance=balance, account=account, error=error)

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    account = None
    amount = None
    new_balance = None
    error = None
    if request.method == 'POST':
        account = request.form['account']
        try:
            amount = int(request.form['amount'])
        except ValueError:
            error = 'Invalid amount!'
            return render_template('withdraw.html', account=account, amount=amount, new_balance=new_balance, error=error)
        if account in user_balances:
            if user_balances[account] >= amount:
                user_balances[account] -= amount
                new_balance = user_balances[account]
            else:
                error = 'Insufficient Balance!'
        else:
            error = 'Account not found!'
    return render_template('withdraw.html', account=account, amount=amount, new_balance=new_balance, error=error)

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    account = None
    amount = None
    new_balance = None
    error = None
    if request.method == 'POST':
        account = request.form['account']
        try:
            amount = int(request.form['amount'])
        except ValueError:
            error = 'Invalid amount!'
            return render_template('deposit.html', account=account, amount=amount, new_balance=new_balance, error=error)
        if account in user_balances:
            user_balances[account] += amount
        else:
            user_balances[account] = amount
        new_balance = user_balances[account]
    return render_template('deposit.html', account=account, amount=amount, new_balance=new_balance, error=error)

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if request.method == 'POST':
        from_account = request.form['from_account']
        to_account = request.form['to_account']
        amount = int(request.form['amount'])
        if from_account == to_account:
            return "<h2>Cannot transfer to the same account!</h2><a href='/transfer'>Try Again</a>"
        if from_account in user_balances and to_account in user_balances:
            if user_balances[from_account] >= amount:
                user_balances[from_account] -= amount
                user_balances[to_account] += amount
                return f"<h2>₹{amount} transferred from {from_account} to {to_account}.<br>New Balance: ₹{user_balances[from_account]}</h2><a href='/'>Back</a>"
            else:
                return "<h2>Insufficient Balance!</h2><a href='/transfer'>Try Again</a>"
        else:
            return "<h2>Account not found!</h2><a href='/transfer'>Try Again</a>"
    return render_template('transfer.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        # In real app, you'd store this
        return f"<h2>Thanks {name}, we received your message!</h2><a href='/'>Back</a>"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
