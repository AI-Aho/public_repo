from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
Base = declarative_base()
engine = create_engine("sqlite:///todo.db", echo = False, future = True)

# Items
class Item(Base):
    __tablename__ = "items"
    itemId = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    time = Column(DateTime(timezone=True), default=func.now())
    users = relationship("User", secondary="useritems", back_populates="items", single_parent=True)

class User(Base):
    __tablename__ = "users"
    userId = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(Integer, nullable=False)
    items = relationship("Item", secondary="useritems", back_populates="users", single_parent=True)

class UserItem(Base):
    __tablename__ = "useritems"
    userId = Column(Integer, ForeignKey("users.userId"), primary_key=True)
    itemId = Column(Integer, ForeignKey("items.itemId"), primary_key=True)



Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)







