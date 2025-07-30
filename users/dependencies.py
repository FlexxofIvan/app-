from typing import Annotated
from fastapi import Depends, HTTPException, status
from auth.dependencies import AuthDep
from auth.utils import decode_token
from base.base_crud import CRUD
from base.dependencies import SessionDep
from users.models import Users



async def get_current_user(token: AuthDep, session: SessionDep):
    try:
        payload = decode_token(token)
        idx = payload["sub"]
        user_crud = CRUD(table=Users, session=session)
        user = await user_crud.read_by_filter([Users.id == int(idx)])
        if user:
            return user[0]
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorized user")
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or expired")


UserDep = Annotated[Users, Depends(get_current_user)]
