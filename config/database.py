import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#nombre base de datos
sqlite_file_name = 'database.sqlite'

# directorio base de datos
base_dir = os.path.dirname(os.path.realpath(__file__))

# la URL de sqlite necesita el formato siguiente 
database_url = f'sqlite:///{os.path.join(base_dir,sqlite_file_name)}'

#crear la engine
engine = create_engine(database_url,echo=True)

#se crea la session
Session = sessionmaker(bind=engine)

# se usara despues 
Base = declarative_base()