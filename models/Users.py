from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Users(Base):
    
    __tablename__ = 'users'

    UID = Column(Integer, primary_key=True)
    Fname = Column(String(20))
    Lname = Column(String(20))
    Phone = Column(String(20))
    Email = Column(String(20))


    def getID():
        
        return self.UID
        

    def getName():

        return self.Fname + ' ' + self.Lname


    def getPhone():

        return self.Phone


    def getEmail():

        return self.Email


    def __repr__(self):
         
        return "<User(Fname='%s', Lname='%s', Phone='%s', Email='%s')>" % (
                             self.Fname, self.Lname, self.Phone, self.Email)
