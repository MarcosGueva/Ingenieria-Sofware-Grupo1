from config.database import db
from passlib.context import CryptContext
from utils.jwt_utils import create_access_token
from bson.objectid import ObjectId

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

async def register_user(user_data):
    existing = await db.users.find_one({"email": user_data.email})
    if existing:
        return None
    user = user_data.dict()
    user["password"] = hash_password(user["password"])
    user["role"] = "SOCIO"
    result = await db.users.insert_one(user)
    return {**user, "id": str(result.inserted_id)}

async def authenticate_user(email: str, password: str):
    user = await db.users.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        return None
    token = create_access_token({"sub": user["email"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}
