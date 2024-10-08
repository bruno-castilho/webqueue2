from pony.orm import *
from lib import db
from modals import Project

class Storage(db.Entity):
    id = PrimaryKey(int, auto=True)
    ip = Required(str)
    nfs_path = Required(str)
    container_path = Required(str)
    project_default = Optional(Project, reverse='storage_default')
    project = Optional(Project, reverse='storages')


