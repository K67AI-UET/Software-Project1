from fastapi import Header, Depends

from src.controllers.factory import Factory
from src.controllers import KeyController, UserController
from src.utils import JWTHandler
from src.utils.exceptions import UnauthorizedException
from src.models import User


async def authorization(
    user_id: str = Header(
        alias="user-id",
    ),
    authorization: str = Header(
        alias="authorization",
    ),
    key_controller: KeyController = Depends(Factory().get_key_controller),
    user_controller: UserController = Depends(Factory().get_user_controller)
) -> User:
    publicKey = key_controller.get_by_userId(userId=user_id).publicKey
    print(publicKey)
    tokenDecoded = JWTHandler.decode(key=publicKey, token=authorization)
    print(tokenDecoded)
    if tokenDecoded.get('user_id') != user_id:
        raise UnauthorizedException(message="Invalid authorization")
    return user_controller.get_by_userId(userId=user_id)
