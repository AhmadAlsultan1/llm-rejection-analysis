from typing import List
from pydantic import BaseModel, Field


class Category(BaseModel):
    name: str = Field(description="Short English category name")
    count: int = Field(description="Number of reasons in this category")
    percentage: float = Field(description="Percentage of total reasons")
    reasons: List[str] = Field(description="Original Arabic rejection reasons")


class RejectionAnalysis(BaseModel):
    categories: List[Category]
    summary: str = Field(description="Short English summary")