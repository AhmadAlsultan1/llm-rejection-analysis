import json
from models.schema import RejectionAnalysis


def analyze_rejection_reasons(llm, reasons, prompt_template):
    structured_llm = llm.with_structured_output(RejectionAnalysis)

    prompt = f"""
{prompt_template}

Total rejection reasons: {len(reasons)}

Rejection reasons:
{json.dumps(reasons, ensure_ascii=False, indent=2)}
"""

    return structured_llm.invoke(prompt)

