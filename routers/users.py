from fastapi import APIRouter


router = APIRouter(
    
    prefix='/users',
    tags=['Users']
    
)


@router.get('/')
async def saludar():
    return {'Hola desde user'}