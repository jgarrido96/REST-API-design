from database import db
from sqlalchemy.orm import Mapped, mapped_column
# from typing import List


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    # id: Mapped[int] = mapped_column(primary_key=True)
    # name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    # email: Mapped[str] = mapped_column(db.String(320))
    # orders: Mapped[List['Order']] = db.relationship(back_populates='customer')

    def __repr__(self):
        return f'<customers {self.id}|{self.name}>'