#  LLM Rejection Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Pydantic](https://img.shields.io/badge/Pydantic-Structured_Output-purple)
![Status](https://img.shields.io/badge/Status-In_Development-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

An AI-powered prototype that automatically analyzes reviewer rejection reasons using **LangChain** and **Google Gemini**.

The system groups similar Arabic rejection reasons into meaningful categories, calculates statistics, and produces structured business insights that can later be visualized in dashboards or integrated into enterprise systems.

---

#  Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Folder Responsibilities](#-folder-responsibilities)
- [Example Input](#-example-input)
- [Example Output](#-example-output)
- [Installation](#-installation)
- [Running the Project](#-running-the-project)
- [Tech Stack](#-tech-stack)
- [Roadmap](#-roadmap)
- [Future Vision](#-future-vision)
- [Author](#-author)

---

#  Overview

This project demonstrates how Large Language Models (LLMs) can automate the analysis of reviewer rejection reasons.

Instead of manually reading hundreds of rejection comments, the system automatically:

- Groups similar rejection reasons
- Creates meaningful categories
- Calculates category percentages
- Generates concise summaries
- Produces structured JSON output

The project simulates an AI component that can later be integrated into larger review systems.

---

#  Problem Statement

Organizations often collect free-text rejection reasons from reviewers.

Example:

- الصورة غير واضحة
- الهوية غير مقروءة
- المستند منتهي الصلاحية
- المرفقات ناقصة

Reading hundreds or thousands of these comments manually is slow and inefficient.

Managers need answers such as:

- What are the most common rejection reasons?
- Which problems occur most frequently?
- What trends appeared this month?
- Which rejection category should be improved first?

---

#  Solution

The project uses an LLM to transform raw rejection reasons into structured business insights.

Input:

```
Arabic rejection reasons
```

↓

Prompt Engineering

↓

LangChain

↓

Google Gemini

↓

Structured JSON

↓

Business Insights

---

#  Features

- Analyze Arabic rejection reasons
- Automatic semantic categorization
- Structured JSON output
- Category percentages
- Summary generation
- Modular architecture
- Easily replaceable LLM provider
- Prompt separation from code

---

#  System Architecture

```
                    Reviewer
                        │
                        ▼
            Rejection Reasons (Arabic)
                        │
                        ▼
                 JSON Dataset
                        │
                        ▼
               Prompt Template
                        │
                        ▼
                 LangChain
                        │
                        ▼
                 Gemini LLM
                        │
                        ▼
            Structured JSON Output
                        │
                        ▼
             Dashboard / Analytics
```

---

#  Project Structure

```
llm-rejection-analysis/

│
├── app.py
├── generate_dataset.py
├── requirements.txt
├── README.md
├── .env.example
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
├── output/
│   └── analysis.json
│
└── docs/
```

---

#  Folder Responsibilities

| Folder | Responsibility |
|---------|---------------|
| app.py | Project entry point |
| generate_dataset.py | Generates sample Arabic rejection reasons |
| data | Input datasets |
| prompts | Prompt templates |
| models | Pydantic schemas |
| services | Business logic and LLM interaction |
| output | Generated AI analysis |
| docs | Project documentation |

---

#  Example Input

```json
[
  "الصورة غير واضحة",
  "المرفقات ناقصة",
  "رقم الهوية لا يطابق البيانات",
  "المستند منتهي الصلاحية"
]
```

---

#  Example Output

```json
{
  "categories": [
    {
      "name": "Document Quality",
      "count": 24,
      "percentage": 32.0,
      "reasons": [
        "الصورة غير واضحة",
        "الهوية غير مقروءة"
      ]
    },
    {
      "name": "Missing Documents",
      "count": 18,
      "percentage": 24.0,
      "reasons": [
        "المرفقات ناقصة"
      ]
    }
  ],
  "summary": "Most rejection reasons are related to document quality and missing required documents."
}
```

---

#  Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/llm-rejection-analysis.git
```

Move into the project

```bash
cd llm-rejection-analysis
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

#  Environment Variables

Create a `.env` file

```env
GOOGLE_API_KEY=your_google_api_key
```

---

#  Running the Project

Generate the dataset

```bash
python generate_dataset.py
```

Run the application

```bash
python app.py
```

The generated analysis will be stored inside

```
output/analysis.json
```

---

#  Tech Stack

- Python
- LangChain
- Google Gemini
- Pydantic
- JSON
- Git
- Bitbucket
- GitHub

---

#  Roadmap

##  Completed

- Dataset generation
- Arabic rejection reason analysis
- LangChain integration
- Gemini integration
- Structured JSON output
- Modular architecture
- Prompt separation
- Category percentages

---

##  In Progress

- Full reviewer workflow simulation
- Application-level data model
- Better prompt engineering

---

##  Planned

- Dashboard
- FastAPI
- Dataiku integration
- Docker
- Unit tests
- Logging
- CI/CD
- Database integration
- Batch processing
- REST API
- Authentication

---

#  Future Vision

The long-term goal is to evolve this prototype into an enterprise-ready AI component capable of integrating into real review systems.

Future versions will support:

- Reviewer workflows
- Batch analysis
- Interactive dashboards
- Database integration
- API endpoints
- Dataiku pipelines
- Cloud deployment

---

#  Author

**Ahmad Al Sultan**

AI & Data Science Enthusiast

Built as part of my AI Engineering learning journey and internship preparation.


