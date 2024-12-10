import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://swasthikp03:swasthik@swasthikprabhu.fabhbaq.mongodb.net/")
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
