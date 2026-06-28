import json
from pathlib import Path

from services.llm import get_llm
from services.analyzer import analyze_rejection_reasons


def main():
    reasons_path = Path("data/rejection_reasons.json")
    prompt_path = Path("prompts/categorization_prompt.txt")
    output_path = Path("output/analysis.json")

    reasons = json.loads(reasons_path.read_text(encoding="utf-8"))
    prompt_template = prompt_path.read_text(encoding="utf-8")

    llm = get_llm()
    result = analyze_rejection_reasons(llm, reasons, prompt_template)

    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(
        result.model_dump_json(indent=2),
        encoding="utf-8"
    )

    print("Analysis saved to output/analysis.json")


if __name__ == "__main__":
    main()