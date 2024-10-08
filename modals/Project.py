from datetime import datetime
from pony.orm import *
from lib import db
from modals import User, Image

class Project(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    slug = Required(str, unique=True)
    created_at = Required(datetime, default=lambda: datetime.now())
    last_use = Required(datetime, default=lambda: datetime.now())
    leader = Required(User, reverse='projects_leader')
    members = Set(User, reverse='projects_member')
    images = Set(Image)
    storage_default = Required('Storage', reverse='project_default')
    storages = Set('Storage', reverse='project')
