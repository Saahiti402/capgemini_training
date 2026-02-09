from flask import Flask
from flask_smorest import Api, Blueprint, abort
from flask.views import MethodView
from marshmallow import Schema, fields, validate
from datetime import datetime

app = Flask(__name__)
app.config['API_TITLE'] = 'Bank Account API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)
blp = Blueprint("bank", __name__, description="Bank Account Management APIs")

# In-memory storage
customers, accounts, transactions = [], [], []
customer_id_counter = 1
transaction_id_counter = 1

# ---------------- Schemas ----------------
class CustomerSchema(Schema):
    customer_id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2))
    email = fields.Email(required=True)
    phone = fields.Str(required=True, validate=validate.Length(min=10))

class AccountSchema(Schema):
    account_number = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    account_type = fields.Str(required=True, validate=validate.OneOf(['Saving', 'Current']))
    balance = fields.Float(dump_only=True)

class AmountSchema(Schema):
    amount = fields.Float(required=True, validate=validate.Range(min=1))

class TransactionSchema(Schema):
    transaction_id = fields.Int(dump_only=True)
    account_number = fields.Int(dump_only=True)
    type = fields.Str(dump_only=True)
    amount = fields.Float(dump_only=True)
    date = fields.Str(dump_only=True)

# ---------------- Helpers ----------------
def find_customer(cid):
    return next((c for c in customers if c['customer_id'] == cid), None)

def find_account(acc_no):
    return next((a for a in accounts if a['account_number'] == acc_no), None)

def add_txn(acc_no, ttype, amount):
    global transaction_id_counter
    transactions.append({
        "transaction_id": transaction_id_counter,
        "account_number": acc_no,
        "type": ttype,
        "amount": float(amount),
        "date": datetime.utcnow().isoformat()
    })
    transaction_id_counter += 1

# ---------------- Customer Routes ----------------
@blp.route("/customers")
class Customers(MethodView):

    # Create new customer
    @blp.arguments(CustomerSchema)
    @blp.response(201, CustomerSchema)
    def post(self, data):
        global customer_id_counter
        data["customer_id"] = customer_id_counter
        customer_id_counter += 1
        customers.append(data)
        return data

    # Get all customers
    @blp.response(200, CustomerSchema(many=True))
    def get(self):
        return customers


@blp.route("/customers/<int:cid>")
class CustomerById(MethodView):

    # Get one customer
    @blp.response(200, CustomerSchema)
    def get(self, cid):
        cust = find_customer(cid)
        if not cust:
            abort(404, message="Customer not found")
        return cust

    # Delete customer
    def delete(self, cid):
        cust = find_customer(cid)
        if not cust:
            abort(404, message="Customer not found")

        # Remove accounts of customer
        cust_accounts = [a for a in accounts if a["customer_id"] == cid]
        for a in cust_accounts:
            accounts.remove(a)

        customers.remove(cust)
        return {"message": "Customer deleted successfully"}, 200


# ---------------- Account Routes ----------------
@blp.route("/accounts")
class Accounts(MethodView):

    # Create new account
    @blp.arguments(AccountSchema)
    @blp.response(201, AccountSchema)
    def post(self, data):
        if not find_customer(data["customer_id"]):
            abort(404, message="Customer not found")

        acc_no = 1000 + len(accounts) + 1
        acc = {"account_number": acc_no, "balance": 0.0, **data}
        accounts.append(acc)
        return acc

    # Get all accounts
    @blp.response(200, AccountSchema(many=True))
    def get(self):
        return accounts


@blp.route("/accounts/<int:acc_no>")
class AccountById(MethodView):

    # Get one account
    @blp.response(200, AccountSchema)
    def get(self, acc_no):
        acc = find_account(acc_no)
        if not acc:
            abort(404, message="Account not found")
        return acc

    # Delete account
    def delete(self, acc_no):
        acc = find_account(acc_no)
        if not acc:
            abort(404, message="Account not found")

        accounts.remove(acc)
        return {"message": "Account deleted successfully"}, 200


# ---------------- Deposit ----------------
@blp.route("/accounts/<int:acc_no>/deposit")
class Deposit(MethodView):
    @blp.arguments(AmountSchema)
    @blp.response(200, AccountSchema)
    def post(self, body, acc_no):
        acc = find_account(acc_no)
        if not acc:
            abort(404, message="Account not found")

        acc["balance"] += float(body["amount"])
        add_txn(acc_no, "Deposit", body["amount"])
        return acc

# ---------------- Withdraw ----------------
@blp.route("/accounts/<int:acc_no>/withdraw")
class Withdraw(MethodView):
    @blp.arguments(AmountSchema)
    @blp.response(200, AccountSchema)
    def post(self, body, acc_no):
        acc = find_account(acc_no)
        if not acc:
            abort(404, message="Account not found")

        amt = float(body["amount"])
        if acc["balance"] < amt:
            abort(400, message="Insufficient balance")

        acc["balance"] -= amt
        add_txn(acc_no, "Withdraw", amt)
        return acc

# ---------------- Transaction History ----------------
@blp.route("/accounts/<int:acc_no>/transactions")
class TxnHistory(MethodView):

    # GET all transactions for account
    @blp.response(200, TransactionSchema(many=True))
    def get(self, acc_no):
        if not find_account(acc_no):
            abort(404, message="Account not found")
        return [t for t in transactions if t["account_number"] == acc_no]

    # DELETE all transactions for account
    def delete(self, acc_no):
        if not find_account(acc_no):
            abort(404, message="Account not found")

        global transactions
        transactions = [t for t in transactions if t["account_number"] != acc_no]

        return {"message": "Transaction history cleared"}, 200


# Register blueprint
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
