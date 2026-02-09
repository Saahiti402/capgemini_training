from flask import Flask
from flask_smorest import Api, Blueprint, abort
from flask.views import MethodView
from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import EXCLUDE

app = Flask(__name__)

app.config['API_TITLE'] = 'Bank Account API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:riya%402005123@localhost:3306/bankdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
api = Api(app)
blp = Blueprint("bank", __name__, description="Bank APIs")

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))

class Account(db.Model):
    account_number = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    account_type = db.Column(db.String(20))
    balance = db.Column(db.Float, default=0.0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.Integer)
    type = db.Column(db.String(20))
    amount = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)

@blp.route("/customers")
class CustomerList(MethodView):

    # GET all customers
    @blp.response(200, CustomerSchema(many=True))
    def get(self):
        return Customer.query.all()

    # CREATE customer
    @blp.arguments(CustomerSchema)
    @blp.response(201, CustomerSchema)
    def post(self, data):
        customer = Customer(**data)
        db.session.add(customer)
        db.session.commit()
        return customer


@blp.route("/customers/<int:customer_id>")
class CustomerDetail(MethodView):

    @blp.response(200, CustomerSchema)
    def get(self, customer_id):
        customer = Customer.query.get(customer_id)
        if not customer:
            abort(404, message="Customer not found")
        return customer

    @blp.arguments(CustomerSchema)
    @blp.response(200, CustomerSchema)
    def put(self, data, customer_id):
        customer = Customer.query.get(customer_id)
        if not customer:
            abort(404, message="Customer not found")

        customer.name = data["name"]
        customer.email = data["email"]
        customer.phone = data["phone"]

        db.session.commit()
        return customer

    @blp.response(200)
    def delete(self, customer_id):
        customer = Customer.query.get(customer_id)
        if not customer:
            abort(404, message="Customer not found")

        db.session.delete(customer)
        db.session.commit()
        return {"message": "Customer deleted successfully"}


api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True, port=3300)