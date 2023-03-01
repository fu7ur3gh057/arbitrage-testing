from typing import Union

from fastapi import APIRouter, Depends, HTTPException

from server.db.dao.user_dao import UserDAO
from server.web.api.users.schema import UserDTO, UserInputDTO

router = APIRouter()


@router.post("/", response_model=UserDTO)
async def create_user(data: UserInputDTO, user_dao: UserDAO = Depends()) -> UserDTO:
    new_user = await user_dao.create_user(name=data.name, external_id=data.external_id)
    return UserDTO(
        id=new_user.id,
        name=new_user.name,
        external_id=new_user.external_id,
        deal_count=0,
    )


@router.get("/{user_id}", response_model=UserDTO)
async def get_user(user_id: int, user_dao: UserDAO = Depends()):
    user = await user_dao.get_user_by_id(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    else:
        deals = await user_dao.get_user_deals(user_id=user.id)
        return UserDTO(
            id=user.id,
            name=user.name,
            external_id=user.external_id,
            deal_count=len(deals),
        )


# TODO get user deals
