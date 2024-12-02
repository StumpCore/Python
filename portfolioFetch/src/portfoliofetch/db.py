from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import pathlib
import os

def database():
    # Check if database exists
    rootPath = os.path.dirname(os.path.abspath(__file__))
    dbFile = pathlib.Path(rootPath+'/db.db')

    if not dbFile:
        print('Database does not exist. Creating new one.')
        dbFile = open('db.db', 'a')
        dbFile.close()

    # Establish connection to database
    engine = create_engine(f"sqlite:///{rootPath}/db.db")
    session = Session(engine)
    print('Established connection to database.')
    return session