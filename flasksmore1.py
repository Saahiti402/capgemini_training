from flask import Flask
from flask_smorest import Api, Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields
from datetime import datetime


app = Flask(__name__)

app.config["API_TITLE"] = "BANK API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

customers = {}
accounts = {}
transactions = []



class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)

class AccountSchema(Schema):
    acc_no = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    account_type = fields.Str(required=True)
    balance = fields.Float(dump_only=True)

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    acc_no = fields.Int(required=True)
    type = fields.Str(required=True)
    amount = fields.Float(required=True)
    date = fields.Str(dump_only=True)



blp = Blueprint("bank", 
                __name__,
                  description="Bank Management APIs")





@blp.route("/customers")
class CustomerList(MethodView):

    @blp.response(200, CustomerSchema(many=True))
    def get(self):
        return list(customers.values())

    @blp.arguments(CustomerSchema)
    @blp.response(201, CustomerSchema)
    def post(self, data):
        cid = len(customers) + 1
        data["id"] = cid
        customers[cid] = data
        return data





@blp.route("/accounts")
class AccountList(MethodView):

    @blp.arguments(AccountSchema)
    @blp.response(201, AccountSchema)
    def post(self, data):

        if data["customer_id"] not in customers:
            return {"message": "Customer not found"}, 404

        acc_no = len(accounts) + 1001

        account = {
            "acc_no": acc_no,
            "customer_id": data["customer_id"],
            "account_type": data["account_type"],
            "balance": 0
        }

        accounts[acc_no] = account
        return account



@blp.route("/accounts/<int:acc_no>")
class Account(MethodView):

    @blp.response(200, AccountSchema)
    def get(self, acc_no):
        if acc_no not in accounts:
            return {"message": "Account not found"}, 404

        return accounts[acc_no]



@blp.route("/transactions")
class TransactionList(MethodView):

    @blp.arguments(TransactionSchema)
    @blp.response(201, TransactionSchema)
    def post(self, data):

        acc_no = data["acc_no"]

        if acc_no not in accounts:
            return {"message": "Account not found"}, 404

        amount = data["amount"]
        ttype = data["type"]

     

        if ttype == "Deposit":
            accounts[acc_no]["balance"] += amount

        elif ttype == "Withdraw":

            if accounts[acc_no]["balance"] < amount:
                return {"message": "Insufficient balance"}, 400

            accounts[acc_no]["balance"] -= amount

        else:
            return {"message": "Invalid transaction type"}, 400

        transaction = {
            "id": len(transactions) + 1,
            "acc_no": acc_no,
            "type": ttype,
            "amount": amount,
            "date": str(datetime.now())
        }

        transactions.append(transaction)

        return transaction
    

    
@blp.route("/transactions/<int:acc_no>")
class TransactionHistory(MethodView):

    @blp.response(200, TransactionSchema(many=True))
    def get(self, acc_no):
        return [t for t in transactions if t["acc_no"] == acc_no]







api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)