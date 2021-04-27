from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.inspection import inspect

from models import Base
"""
Base = declarative_base()
"""
class Users(Base):
    
    __tablename__ = 'users'

    UID = Column(Integer, primary_key=True)
    Fname = Column(String(20))
    Lname = Column(String(20))
    Phone = Column(String(20))
    Email = Column(String(20))
    UPassword = Column(String(20))


    def getPKName():
        
        return inspect(Users).primary_key[0].name


    def getID():
        
        return self.UID
        

    def getName():

        return self.Fname + ' ' + self.Lname


    def getPhone():

        return self.Phone


    def getEmail():

        return self.Email


    def getPassword():

        return self.UPassword


    def __repr__(self):
         
        return "<Users(Fname='%s', Lname='%s', Phone='%s', Email='%s', UPassword='%s')>" % (
                             self.Fname, self.Lname, self.Phone, self.Email, self.UPassword)
