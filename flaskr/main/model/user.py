from ...db import Base
from sqlalchemy import Column, String


class USERS_TB(Base):
    __tablename__ = 'USERS_TB'

    id = Column(String(30), primary_key=True)
    pwd = Column(String(100))

    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd
        