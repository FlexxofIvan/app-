from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import inspect


class Base(DeclarativeBase):
    def __repr__(self):
        mapper = inspect(self.__class__)
        attrs = []
        for col in mapper.columns:
            attr_name = col.key
            attr = getattr(self, attr_name)
            attrs.append(f"{attr_name} is {attr}")
        return '\n'.join(attrs)