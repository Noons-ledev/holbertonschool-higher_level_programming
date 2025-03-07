#!/usr/bin/python3
"""
Using SQLAlchemy to retrieve a liste of states from a db table
"""

if __name__ == '__main__':

    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    letter = 'a'
    states = session.query(State).\
        filter(State.name.like('%{}%'.format(letter))).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
