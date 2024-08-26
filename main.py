from typing import List

from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from auth.auth import auth_backend
from database.database import User, get_async_session
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate, UserUpdate

from models import models
from notes.schemas import NoteCreate, NoteRead

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()

current_active_user = fastapi_users.current_user(active=True)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["auth"],
)


@app.get("/notes")
async def read_notes(user: User = Depends(current_active_user),
                     session: AsyncSession = Depends(get_async_session)) -> List[NoteRead]:
    query = select(models.Note).filter_by(user_id=user.id)
    result = await session.execute(query)
    user_notes = result.mappings().all()
    return user_notes


@app.post("/notes")
async def create_note(note: NoteCreate, user: User = Depends(current_active_user),
                      session: AsyncSession = Depends(get_async_session)) -> NoteRead:
    new_note = models.Note(title=note.title, content=note.content, user_id=user.id)
    session.add(new_note)
    await session.commit()
    await session.refresh(new_note)
    return new_note
