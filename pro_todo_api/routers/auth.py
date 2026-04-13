# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from fastapi.security import OAuth2PasswordRequestForm
# from database import get_db
# import models,schemas,security

# router = APIRouter(prefix="/auth", tags=["auth"])

# @router.post("/register", response_model=schemas.User)
# def register (user: schemas.UserCrate, db: Session = Depends(get_db)):
#     db_user = db.query (models.User).filter(models.User.username == user.username).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")

#     hashed_password = security.get_passowd_hash(user.password)
#     new_user= models.User(username = user.username, hashed_password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

# @router.post("/login")
# def login(from_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.username == from_data.username).filter()
#     if not user or not security.verify_password(from_data.password, user.hashed_password):
#         raise HTTPException(status_code=400, detail="Invalid username or password")
    
#     return {"massage": "Login successful"}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
import models, security, schemas 

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = security.get_password_hash(user.password)
    new_user = models.User(username = user.username, hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    return {"message": "Login successful"}