from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(String(30))
    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30))
    patron: Mapped[Optional[str]]
    is_active: Mapped[bool]

class Users_roles(db.model):
    user_id: Mapped[int]
    role_id: Mapped[int]

class Roles(db.model):
    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str]

class Roles_permissions(db.model):
    role_id: Mapped[int]
    permission_id: Mapped[int]

class Permissions(db.model):
    id: Mapped[int] = mapped_column(primary_key=True)
    permission: Mapped[str] = mapped_column(String(50))
