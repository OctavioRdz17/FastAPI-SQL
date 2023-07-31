Resumen

1) Creamos la carpeta models y dentro de ella los archivos __init__.py y movie.py.

```python
from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):
    ___tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
 ```   
2) En main.py añadimos las configuraciones para que se cree la base de datos.

```python
from config.database import Session, engine, Base
from models.movie import Movie

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)
```