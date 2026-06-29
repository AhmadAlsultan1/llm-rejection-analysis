# LLM Rejection Analysis

An AI-powered prototype that analyzes reviewer rejection reasons using LangChain and Google's Gemini model.

The system groups similar Arabic rejection reasons into meaningful categories, counts how many reasons belong to each category, calculates percentages, and generates a structured summary.

---

## Features

- Analyze Arabic rejection reasons
- Automatically group similar reasons into categories
- Generate category counts and percentages
- Produce a concise summary
- Return structured JSON output
- Built with a modular project architecture

---

## Architecture

```text
Reviewer Rejection Reasons
          |
          v
JSON Dataset
          |
          v
Prompt Template
          |
          v
LangChain
          |
          v
Gemini LLM
          |
          v
Structured Output
          |
          v
analysis.json
```

---

## Project Structure

```text
llm-rejection-analysis/
│
├── app.py
├── generate_dataset.py
├── requirements.txt
├── README.md
│
├── data/
│   └── rejection_reasons.json
│
├── prompts/
│   └── categorization_prompt.txt
│
├── models/
│   └── schema.py
│
├── services/
│   ├── llm.py
│   └── analyzer.py
│
└── output/
    └── analysis.json
```

---

## Folder Responsibilities

| Path | Responsibility |
|---|---|
| `app.py` | Main entry point for running the analysis |
| `generate_dataset.py` | Generates sample Arabic rejection reasons |
| `data/` | Stores input datasets |
| `prompts/` | Stores LLM prompt templates |
| `models/` | Contains Pydantic schemas for structured output |
| `services/` | Contains LLM setup and analysis logic |
| `output/` | Stores generated analysis results |

---

## Example Input

```json
[
  "الصورة غير واضحة.",
  "المرفقات ناقصة.",
  "رقم الهوية لا يطابق البيانات المدخلة.",
  "المستند منتهي الصلاحية."
]
```

---

## Example Output

```json
{
  "categories": [
    {
      "name": "Poor Document Quality",
      "count": 1,
      "percentage": 25.0,
      "reasons": [
        "الصورة غير واضحة."
      ]
    },
    {
      "name": "Missing Documents",
      "count": 1,
      "percentage": 25.0,
      "reasons": [
        "المرفقات ناقصة."
      ]
    }
  ],
  "summary": "The rejection reasons mainly relate to document quality, missing attachments, data mismatch, and expired documents."
}
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd llm-rejection-analysis
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> Do not commit your `.env` file.

---

## Run the Project

Generate sample data:

```bash
python generate_dataset.py
```

Run the analysis:

```bash
python app.py
```

The result will be saved to:

```text
output/analysis.json
```

---

## Tech Stack

- Python
- LangChain
- Google Gemini
- Pydantic
- JSON
- Git
- Bitbucket
- GitHub

---

## Roadmap

### Completed

- [x] Generate Arabic rejection reason dataset
- [x] Analyze reasons using Gemini
- [x] Categorize similar rejection reasons
- [x] Generate structured JSON output
- [x] Refactor project into modular architecture

### Next Improvements

- [ ] Simulate full reviewer decision workflow
- [ ] Support application-level JSON data
- [ ] Add dashboard visualizations
- [ ] Add FastAPI endpoint
- [ ] Add Dataiku integration
- [ ] Add unit tests
- [ ] Add logging
- [ ] Add Docker support
- [ ] Add CI/CD pipeline

---

## Project Goal

This project is a learning prototype designed to simulate how AI can help summarize and categorize reviewer rejection reasons in a real review system.