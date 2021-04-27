from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from models import Base
"""
Base = declarative_base()
"""
class Ingredientlist(Base):
    
    __tablename__ = 'ingredientlist'

    ILID = Column(Integer, primary_key=True)
    Ingredient = Column(String(20))
    RecID = Column(Integer, ForeignKey('recipes.RecID'))
    
    users = relationship("Recipes", foreign_keys=[RecID])


    def getID(self):

        return self.ILID
        

    def getName(self):

        return self.Ingredient


    def __repr__(self):
         
        return "<Ingredientlist(Ingredient='%s')>" % (
                             self.Ingredient)
