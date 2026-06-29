from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///test.db')
db = SQLAlchemy(app)
metrics = PrometheusMetrics(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))

@app.route("/")
def home():
    with app.app_context():
        db.create_all()
        visit = Visit(message="visited")
        db.session.add(visit)
        db.session.commit()
        count = Visit.query.count()
    return f"DevOps pipeline is alive. Total visits: {count}"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
