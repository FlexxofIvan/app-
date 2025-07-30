from fastapi import APIRouter, HTTPException, status

from base.dependencies import SessionDep
from users.dependencies import UserDep
from users.schemas import UsersPatchSchemes, UsersPutSchemes
from users.transactions import UsersCRUD

user_router = APIRouter(
        tags=['users']
)


@user_router.patch('/{user_id}')
async def change_info(user_id: int, user: UserDep, user_changes: UsersPatchSchemes, session: SessionDep):
        if not (user.id == user_id):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                    detail="You do not have permission to change this.")
        else:
                updates = user_changes.model_dump(exclude_unset=True)
                for name, val in updates.items():
                        setattr(user, name, val)

                await session.commit()
                await session.refresh()

                raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)



@user_router.put('/{user_id}')
async def replace_user(user_id: int, user_data: UsersPutSchemes, current_user: UserDep, session: SessionDep):
    if current_user.id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You do not have permission to replace this user.")

    crud = UsersCRUD(session=session)
    user = await crud.get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")

    for field, value in user_data.model_dump().items():
        setattr(user, field, value)

    await session.commit()

    return {"message": "User replaced successfully"}