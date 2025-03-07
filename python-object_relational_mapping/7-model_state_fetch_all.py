#!/usr/bin/python3
"""
Using SQLAlchemy to retrieve a liste of states from a db table
"""

if __name__ == '__main__':

    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa')

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.execute(text("SELECT * from states"))
    for id, name in result:
        print("{}: {}".format(id, name))
