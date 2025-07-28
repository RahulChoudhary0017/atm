# ATM Web Application

This is a simple ATM web application built with Flask. It allows users to check their balance, withdraw and deposit money, transfer funds between accounts, and contact support. The application uses dummy data for demonstration purposes and does not connect to a real database.

## Features
- **Check Balance:** View the current balance for a given account number.
- **Withdraw Money:** Withdraw funds from an account if sufficient balance is available.
- **Deposit Money:** Deposit funds into an account.
- **Transfer Funds:** Transfer money between two accounts.
- **Contact Support:** Send a message to the support team.

## Project Structure
```
atm/
  app.py                # Main Flask application
  templates/
    index.html          # Home page
    check_balance.html  # Balance inquiry page
    withdraw.html       # Withdraw funds page
    deposit.html        # Deposit funds page
    transfer.html       # Transfer funds page
    contact.html        # Contact support page
  atm.ipynb             # (Optional) Jupyter notebook for experiments
```

## Requirements
- Python 3.x
- Flask

## Installation
1. Clone this repository or download the source code.
2. Install Flask:
   ```bash
   pip install flask
   ```

## Usage
1. Run the Flask app:
   ```bash
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000/`.
3. Use the web interface to check balances, withdraw, deposit, transfer funds, or contact support.

## Notes
- The app uses a hardcoded dictionary for account balances. In a real application, this would be replaced with a database.
- No authentication is implemented. Anyone with access to the app can use any account number.
- For demonstration and educational purposes only.

## License
This project is open source and available under the [MIT License](LICENSE). 