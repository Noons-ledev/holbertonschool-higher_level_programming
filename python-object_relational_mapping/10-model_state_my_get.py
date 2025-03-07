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
    state_name = sys.argv[4].strip()
    result = session.query(State).where(State.name
                                        == state_name).order_by(State.id).all()
    if result:
        for state in result:
            print("{}".format(state.id), end="")
    else:
        print("Not found", end="")
