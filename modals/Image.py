from datetime import datetime
from pony.orm import *
from lib import db
from modals import User

class Image(db.Entity):
    id = PrimaryKey(int, auto=True)
    type = Required(int, size=8, unsigned=True)
    registry = Required(str)
    user = Required(User)
    created_at = Required(datetime, default=lambda: datetime.now())
    last_use = Required(datetime, default=lambda: datetime.now())
    projects = Set('Project')



