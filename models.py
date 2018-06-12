from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

class Items(Base):
    """
    Items table
    """
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    quantity = Column(Integer)
    description = Column(String(256))
    date_added = Column(DateTime())

    def __repr__(self):
        return "<Items(name='%s', quantity='%s', description='%s',date_added='%s')>" % (
               self.name, self.quantity, self.description, self.date_added);
