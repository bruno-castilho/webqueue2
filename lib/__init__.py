from fastapi import FastAPI
from pony.orm import *

db = Database()
app = FastAPI()