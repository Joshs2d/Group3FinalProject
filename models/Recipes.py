from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Recipes(Base):
    
    __tablename__ = 'recipes'

    RECID = Column(Integer, primary_key=True)
    RECName = Column(String(20))


    def getID(self):

        return self.RECID
        

    def getName(self):

        return self.RECName


    def __repr__(self):
         
        return "<User(RECName='%s')>" % (
                             self.RECName)
