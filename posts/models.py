from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from base.base_model import Base


class Posts(Base):
    __tablename__ = 'Posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    post: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    author: Mapped["Users"] = relationship(back_populates="posts")



