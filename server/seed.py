# server/seed.py
from app import app
from models import db, Message

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Seed data
    messages = [
        Message(body="Hello, world!", username="Alice"),
        Message(body="Hi there!", username="Bob"),
        Message(body="How are you?", username="Charlie")
    ]

    db.session.add_all(messages)
    db.session.commit()
    print("Database seeded!")