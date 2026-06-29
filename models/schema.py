from typing import List
from pydantic import BaseModel, Field


class Category(BaseModel):
    name: str = Field(description="Short English category name")
    count: int = Field(description="Number of reasons in this category")
    percentage: float = Field(description="Percentage of total reasons")
    examples: List[str] = Field(description="A few example Arabic reasons for this category")


class RejectionAnalysis(BaseModel):
    categories: List[Category]
    summary: str = Field(description="Short English summary")