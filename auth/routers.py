from fastapi import HTTPException, status, Depends
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from base.base_crud import CRUD

from auth.utils import create_token, check_hash, create_hash
from auth.schemes import SignRequest

from base.dependencies import SessionDep
from users.models import Users


auth_router = APIRouter(tags=["auth"])

@auth_router.post("/login")
async def login(session: SessionDep, form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    authCRUD = CRUD(session=session, table=Users)
    filt = [username == Users.name]
    user = await authCRUD.read_by_filter(filt)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    else:
        user = user[0]
        if not check_hash(user.password, password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password"
            )
        token_info = {'sub': str(user.id)}
        access_token = create_token(data=token_info)
        return {"access_token": access_token, "token_type": "bearer"}



@auth_router.post("/sign_in")
async def sign_in(data: SignRequest, session: SessionDep):
    authCRUD = CRUD(session=session, table=Users)
    filt = [(data.login == Users.name)]
    if await authCRUD.read_by_filter(filt):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    else:
        data = {"name": data.login,
                "password": create_hash(data.password)
                }
        await authCRUD.create(data)

    return {'response': "user successfully created!!"}
