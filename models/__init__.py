from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker


Base = declarative_base()
Session = scoped_session(sessionmaker())
session = Session()

def initialize_sql(engine):

    Session.configure(bind = engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)