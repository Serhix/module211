from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, event
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    birthday = Column(DateTime, nullable=False)
    description = Column(String)
    favorites = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


'''
наступний блок реалізовано для розуміння роботи event
'''

@event.listens_for(Contact, 'before_insert')
def updated_favorites(mapper, conn, target):
    family = ['Кохана', 'Батько', 'Мама']
    if target.first_name in family:
        target.favorites = True
