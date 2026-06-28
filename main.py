import json
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class Category(BaseModel):
    name: str = Field(description="Short English category name")
    count: int = Field(description="Number of reasons in this category")
    reasons: List[str] = Field(description="Original Arabic rejection reasons")


class RejectionAnalysis(BaseModel):
    categories: List[Category]
    summary: str = Field(description="Short English summary")


def main():
    reasons_path = Path("data/rejection_reasons.json")
    prompt_path = Path("prompts/categorization_prompt.txt")

    reasons = json.loads(reasons_path.read_text(encoding="utf-8"))
    prompt_template = prompt_path.read_text(encoding="utf-8")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    structured_llm = llm.with_structured_output(RejectionAnalysis)

    prompt = f"""
{prompt_template}

Rejection reasons:
{json.dumps(reasons, ensure_ascii=False, indent=2)}
"""

    result = structured_llm.invoke(prompt)

    Path("output").mkdir(exist_ok=True)
    output_path = Path("output/analysis.json")

    output_path.write_text(
        result.model_dump_json(indent=2),
        encoding="utf-8"
    )

    print("Analysis saved to output/analysis.json")


if __name__ == "__main__":
    main()