from config.database import Base
from sqlalchemy import Column, Integer,String, Float

class Movie(Base):
    __tablename__ ='movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    overview = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String(255))



