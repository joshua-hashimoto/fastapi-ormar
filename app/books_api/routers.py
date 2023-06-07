
from uuid import UUID

from fastapi import APIRouter, Body, FastAPI, HTTPException, Path, status

from .models import Book
from .schemas import BookIn, BookUpdateIn

router = APIRouter()

def setup_routers(app: FastAPI):
    app.include_router(router)


@router.get("/", response_model=list[Book])
async def fetch_books():
    try:
        books = await Book.objects.filter(is_active=True).all()
        return books
    except BaseException:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "一覧の取得に失敗しました"
        raise HTTPException(status_code=status_code, detail=message) from None


@router.get("/{book_id}")
async def fetch_book(book_id: UUID = Path(...)) -> Book:
    try:
        book = await Book.objects.get(id=book_id, is_active=True)
        return book
    except BaseException:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "詳細の取得に失敗しました"
        raise HTTPException(status_code=status_code, detail=message) from None


@router.post("/add", response_model=Book)
async def add_book(book_in: BookIn = Body(...)):
    try:
        book = Book(**book_in.dict())
        await book.save()
        return book
    except BaseException:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "本の作成に失敗しました"
        raise HTTPException(status_code=status_code, detail=message) from None


@router.put("/{book_id}/update")
async def update_book(book_id: UUID = Path(...), book_update_in: BookUpdateIn = Body(...)) -> Book:
    try:
        book = await Book.objects.get(id=book_id, is_active=True)
        updated_book = await book.update(**book_update_in.dict())
        return updated_book
    except BaseException:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "本の編集に失敗しました"
        raise HTTPException(status_code=status_code, detail=message) from None


@router.delete("/{book_id}/delete")
async def delete_book(book_id: UUID):
    try:
        book = await Book.objects.get(id=book_id, is_active=True)
        await book.update(is_active=False)
        return {"message": "success"}
    except BaseException:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "本の削除に失敗しました"
        raise HTTPException(status_code=status_code, detail=message) from None
