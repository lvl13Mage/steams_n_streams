from fastapi import APIRouter, Response, Depends
from sqlalchemy.orm import Session
import json

router = APIRouter()

router.prefix = "/debug"
router.tags = ["debug"]

@router.get("/hello")
def hello_world(response: Response):
    print("Hello CLI")
    return "Hello WEB"