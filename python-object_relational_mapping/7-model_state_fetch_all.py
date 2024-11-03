#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Setting up connection to the database
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Creates an Engine, which is how SQLAlchemy communicates with the database
    engine = create_engine(
        f"mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}"
    )

    # Creates a configured class Session
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Creates a Session instance
    session = Session()

    # Querying for all State objects
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # Closes the session
    session.close()
