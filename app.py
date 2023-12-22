from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    priority = db.Column(db.Integer)
    active = db.Column(db.Boolean)

    def __repr__(self):
        return f"Vendor {self.id}/ {self.name}"


@app.route('/')
def index():
    db.create_all()

    # v1 = Vendor(id=1, name="microsoft", priority=0, active=True)
    # db.session.add(v1)
    # db.session.commit()

    # v1 = Vendor(id=2, name="samsung", priority=5, active=False)
    # db.session.add(v1)
    # db.session.commit()

    vendors = Vendor.query.all()
    print(vendors)  # [Vendor 1/ microsoft, Vendor 2/ samsung]
    print(Vendor.query.filter(Vendor.active == True).all())  # [Vendor 1/ microsoft]
    print(Vendor.query.filter(Vendor.name.like('%t%')).all())  # [Vendor 1/ microsoft]

    ret = ''
    for v in vendors:
        ret += str(v) + '<br>'

    # return "Test"
    return ret


if __name__ == '__main__':
    app.run(debug=True)
