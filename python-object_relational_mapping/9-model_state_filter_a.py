#!/usr/bin/python3
"""lists all State objects that contain the letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Setting up connection to the database
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine that connects to the core (MySQL)
    engine = create_engine(
        f"mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.like('%a%'))
    for states in state:
        if state:
            print(f"{states.id}: {states.name}")
