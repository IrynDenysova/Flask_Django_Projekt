from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from app.schemas.category import CategoryResponse


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)
    category_id: Optional[int] = None


class QuestionResponse(BaseModel):
    id: int
    text: str
    category: CategoryResponse | None = None
    category_id: Optional[int] = None

    # class Config:
    #     # Указываем Pydantic использовать эти параметры чтобы можно было переносить данные прямо с объекта
    #     orm_mode = True
    #     from_attributes = True

    model_config = ConfigDict(
        from_attributes=True
    )


class MessageResponse(BaseModel):
    message: str
