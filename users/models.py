from typing import List, Annotated, Optional
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from base.base_model import Base
from posts.models import Posts


created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]

class Users(Base):
    __tablename__ = 'Users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[Optional[int]]
    sex: Mapped[Optional[str]]
    posts: Mapped[List["Posts"]] = relationship(back_populates='author')
    password: Mapped[str]




