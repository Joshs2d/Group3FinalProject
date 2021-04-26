from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from models import Base
"""
Base = declarative_base()
"""
class Ingredientlist2(Base):
    
    __tablename__ = 'ingredientlist2'

    ILID = Column(Integer, primary_key=True)
    Ingredient = Column(String(20))


    def getID(self):

        return self.ILID
        

    def getName(self):

        return self.Ingredient


    def __repr__(self):
         
        return "<Ingredientlist2(Ingredient='%s')>" % (
                             self.Ingredient)
