"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


DEFAULT_IMAGE = "https://cdn-icons-png.flaticon.com/512/2821/2821784.png"

__tablename__ = "cupcakes"

id = db.Column(db.Integer, primary_key=True, autoincrement=True)
flavor = db.Column(db.Text, nullable=False)
size = db. Column(db.Text, nullable= False)
rating = db.Column(db.Float, nullable= False)
image = db. Column(db.Text, nullable= False, default=DEFAULT_IMAGE)

def to_dict(self):
    """Organizing cupcakes into the dictionary."""

    return {
        "id": self.id,
        "flavor": self.flavor,
        "rating": self.rating,
        "size": self.size,
        "image": self.image,
    }

def connect_db(app):
    """Connect the database."""

    db.app = app
    db.init_app(app)

