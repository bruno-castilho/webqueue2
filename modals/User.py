from datetime import datetime
from pony.orm import *
from lib import db

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    last_name = Optional(str)
    avatar_url = Optional(str)
    email = Required(str, unique=True)
    admin = Required(bool, default=False)
    images = Set('Image')
    created_at = Optional(datetime, default=lambda: datetime.now())
    last_access = Optional(datetime, default=lambda: datetime.now())
    projects_leader = Set('Project', reverse='leader')
    projects_member = Set('Project', reverse='members')
