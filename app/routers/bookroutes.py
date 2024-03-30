from fastapi import APIRouter

router = APIRouter()

@router.post('/books')
async def addBook():


@router.patch('/books/{book_id}')
async def updateBook():



@router.get('/books/{book_id}')
async def getBookDetails():

