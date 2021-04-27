from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from models import Base

"""
Base = declarative_base()
"""

class Recipes(Base):
    
    __tablename__ = 'recipes'

    RecID = Column(Integer, primary_key=True)
    RecName = Column(String(20))
    RecDescription = Column(String(5000))
    PersonID = Column(Integer, ForeignKey('users.UID'))
    IngredientListID = Column(Integer, ForeignKey('ingredientlist.ILID'))

    users = relationship("Users", foreign_keys=[PersonID])
    Ingredientlist = relationship("Ingredientlist", foreign_keys=[IngredientListID])


    def getID(self):

        return self.RECID
        

    def getName(self):

        return self.RECName


    def __repr__(self):
         
        return "<Recipes(RecName='%s', RecDescription='%s')>" % (
                             self.RecName, self.RecDescription)
