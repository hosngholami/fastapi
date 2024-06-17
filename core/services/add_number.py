from fastapi import APIRouter

router = APIRouter()

@router.get("/sum/")
def sumation(a, b):
    sum = int(a) + int(b)
    return sum


@router.post('/multiply')
def multiply(a, b):
    return int(a) * int(b)

