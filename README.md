# Mini-RAG

A minimal Retrieval-Augmented Generation (RAG) application built as a hands-on learning project for understanding how to build and evolve an AI application from a simple prototype toward a more production-oriented architecture.

This project follows a lesson-by-lesson development approach, where each lesson is maintained in a separate Git branch to track the evolution of the application.

---

## 📌 Project Overview

The main goal of this project is to understand the practical engineering workflow behind building a RAG-based AI application.

Instead of building everything at once, the project is developed incrementally through multiple lessons. Each lesson introduces new concepts, technologies, or improvements to the application.

The project focuses on understanding:

* RAG application architecture
* Backend development with FastAPI
* Document and file processing
* LLM integration
* Vector databases
* Semantic search
* Prompt augmentation
* Database integration
* API design
* Asynchronous processing
* Production-oriented architecture
* Deployment concepts

The project is primarily intended for **learning and experimentation**, while gradually moving toward a more production-ready architecture.

---

# 🧠 What is RAG?

Retrieval-Augmented Generation (RAG) combines information retrieval with Large Language Models (LLMs).

Instead of asking an LLM to answer a question only from its pretrained knowledge, the system first retrieves relevant information from an external knowledge base and provides that information to the LLM as context.

A simplified RAG pipeline looks like this:

```text
User Question
      │
      ▼
   Retrieval
      │
      ▼
Relevant Documents
      │
      ▼
   LLM + Context
      │
      ▼
    Answer
```

This approach can help an AI application answer questions using private or domain-specific information.

---

# 🏗️ Project Architecture

The application evolves throughout the lessons.

The general architecture can be summarized as:

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   FastAPI     │
                    │     API       │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   RAG Logic   │
                    └───────┬───────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
          ┌─────────────┐       ┌─────────────┐
          │ Vector DB   │       │     LLM     │
          │   Search    │       │ Generation  │
          └─────────────┘       └─────────────┘
```

As the project progresses, additional components such as databases, background workers, monitoring, and deployment infrastructure are introduced.

---

# 🛠️ Tech Stack

The project currently uses technologies including:

* **Python 3.11**
* **FastAPI**
* **Uvicorn**
* **Pydantic**
* **Pydantic Settings**
* **LangChain**
* **OpenAI API**
* **Cohere**
* **Qdrant**
* **Motor**
* **MongoDB**
* **PyMuPDF**
* **python-dotenv**
* **aiofiles**
* **uv**
* **Git / GitHub**
* **WSL2 / Ubuntu**

The exact technologies used by the application evolve as new lessons are completed.

---

# 🖥️ Development Environment

The project is developed inside **WSL2 using Ubuntu**.

The project intentionally uses the Linux filesystem rather than keeping the primary development environment inside the Windows filesystem.

Current environment:

```text
Operating System:
Windows 11

Linux Environment:
WSL2
Ubuntu 24.04

Python:
3.11

Package / Environment Manager:
uv

Virtual Environment:
.venv
```

Using WSL provides a Linux development environment that is closer to the environment commonly used for backend and production workloads.

---

# 📂 Project Location

The primary project is stored inside the WSL Linux filesystem:

```text
/home/wael_mohamed/projects/mini-RAG
```

The project structure starts approximately as:

```text
mini-RAG/
│
├── .venv/
├── src/
├── requirements.txt
├── README.md
└── ...
```

> `.venv` is a local development environment and should not be committed to Git.

---

# 🚀 Installation

## 1. Clone the Repository

Clone the repository from GitHub:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd mini-RAG
```

---

## 2. Verify Python

The project currently uses Python 3.11.

Check the installed version:

```bash
python3 --version
```

Expected output:

```text
Python 3.11.x
```

---

# 📦 Installing `uv`

This project uses **uv** instead of Conda for Python environment and package management.

Install uv inside Ubuntu:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Load uv into the current shell:

```bash
source $HOME/.local/bin/env
```

Verify the installation:

```bash
uv --version
```

Example:

```text
uv 0.12.13
```

---

# 🐍 Creating the Virtual Environment

Create a project-local virtual environment using Python 3.11:

```bash
uv venv --python 3.11
```

This creates:

```text
.venv/
```

Activate the environment:

```bash
source .venv/bin/activate
```

Verify the Python interpreter:

```bash
python --version
```

And:

```bash
which python
```

The Python path should point to the project's virtual environment:

```text
/home/wael_mohamed/projects/mini-RAG/.venv/bin/python
```

You can also check the active virtual environment directly:

```bash
echo $VIRTUAL_ENV
```

---

# 📥 Installing Dependencies

The project dependencies are defined in:

```text
requirements.txt
```

Install them using uv:

```bash
uv pip install -r requirements.txt
```

The project currently uses pinned dependency versions to keep the development environment reproducible.

Current dependencies include:

```text
fastapi==0.110.2
uvicorn[standard]==0.29.0
python-multipart==0.0.9
python-dotenv==1.0.1
pydantic-settings==2.2.1
aiofiles==23.2.1
langchain==0.1.20
PyMuPDF==1.24.3
motor==3.4.0
pydantic-mongo==2.3.0
openai==1.35.13
cohere==5.5.8
qdrant-client==1.10.1
```

---

# 🔐 Environment Variables

API keys and other sensitive configuration values should not be hard-coded into the source code.

Environment variables can be stored in a `.env` file.

Example:

```env
OPENAI_API_KEY=your_api_key
COHERE_API_KEY=your_api_key
```

The `.env` file should not be committed to GitHub.

Add it to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
```

---

# ▶️ Running the Application

After activating the virtual environment:

```bash
source .venv/bin/activate
```

The application can be started using Uvicorn.

For example:

```bash
uvicorn main:app --reload
```

The `--reload` option automatically reloads the application when source files are modified during development.

The API should then be available at:

```text
http://127.0.0.1:8000
```

FastAPI also provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

and:

```text
http://127.0.0.1:8000/redoc
```

---

# 🌿 Git Branch Strategy

The project uses Git branches to separate individual lessons.

Instead of using the original tutorial branch naming convention, this project uses:

```text
lsn-01
lsn-02
lsn-03
...
lsn-17
```

The `main` branch represents the main stable version of the project.

Each lesson branch represents the state of the project while working through that specific lesson.

Example:

```text
main
 │
 ├── lsn-01
 ├── lsn-02
 ├── lsn-03
 ├── lsn-04
 ├── ...
 └── lsn-17
```

This makes it easier to:

* Compare changes between lessons
* Experiment safely
* Return to previous implementations
* Understand how the architecture evolved
* Keep experimental work isolated
* Track the learning process using Git

---

# 🔀 Merging Useful Changes into `main`

Not every experiment needs to become part of the main project.

When a lesson contains a useful implementation that should become part of the stable version, the changes can be merged into `main`.

For example:

```bash
git switch main
```

Then:

```bash
git merge lsn-02
```

Finally:

```bash
git push origin main
```

The lesson branch remains available even after the merge.

This allows the project to maintain both:

* The historical lesson implementation
* The evolving stable version

---

# 🧪 Learning & Experimentation

The lesson branches are also used as experimentation environments.

For example, a lesson may contain:

```text
lsn-05
```

where different implementations are tested.

Some experiments may remain only in the lesson branch, while useful implementations can later be integrated into `main`.

This keeps experimentation separate from the stable project.

---

# 🗺️ Development Roadmap

The project is developed incrementally.

The learning progression includes concepts such as:

### Phase 1 — Project Setup

* Project structure
* Git and GitHub
* Python environment
* FastAPI
* Configuration
* Environment variables

### Phase 2 — Backend

* FastAPI routes
* Nested routes
* Request handling
* File uploads
* File processing

### Phase 3 — Data Processing

* Document processing
* PDF extraction
* Data pipelines
* Database integration

### Phase 4 — RAG

* LLM integration
* Embeddings
* Vector databases
* Semantic search
* Retrieval
* Context augmentation
* Answer generation

### Phase 5 — Databases

* MongoDB
* PostgreSQL
* SQLAlchemy
* Alembic
* pgvector

### Phase 6 — Production-Oriented Architecture

* Docker
* Nginx
* Qdrant
* PostgreSQL
* Background workers
* Celery
* Monitoring
* Prometheus
* Grafana

The exact implementation is tracked through the individual lesson branches.

---

# 🐳 Production-Oriented Components

As the project evolves, the architecture introduces several production-oriented technologies.

The intended architecture includes components such as:

```text
                    ┌─────────────┐
                    │   Client    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    Nginx    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   FastAPI   │
                    └──────┬──────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        PostgreSQL      Qdrant         LLM
        + pgvector      Vector DB      API
             │
             ▼
        Background
         Workers
         (Celery)
             │
             ▼
        Monitoring
   Prometheus + Grafana
```

This allows the project to move beyond a simple notebook-style RAG implementation toward a more realistic AI application architecture.

---

# 🎯 Project Goals

The main goals of this project are:

1. Understand how RAG applications are structured.
2. Learn how to build an AI backend using FastAPI.
3. Understand how documents move through a data pipeline.
4. Learn how vector databases support semantic retrieval.
5. Integrate LLMs into an application rather than using them only through notebooks.
6. Understand asynchronous and background processing.
7. Learn how databases are used in AI applications.
8. Understand containerization and deployment.
9. Learn production-oriented architecture and monitoring.
10. Practice Git and GitHub throughout the development process.

---

# 📚 Learning Philosophy

This repository is not intended to be just a collection of copied tutorial code.

The goal is to understand:

```text
Why?
 │
 ├── Why this technology?
 ├── Why this architecture?
 ├── Why this database?
 ├── Why this retrieval approach?
 └── Why this deployment strategy?
```

The project is therefore developed incrementally, with each lesson representing a step in understanding how the individual components fit together.

---

# ⚠️ Development Status

🚧 **This project is currently under development.**

The implementation is being built incrementally while progressing through the lessons.

Some components may therefore be incomplete, experimental, or subject to change.

The `main` branch is intended to contain the more stable version, while individual `lsn-*` branches preserve lesson-specific implementations and experiments.

---

# 📄 License

This project is intended as a personal learning and portfolio project.

The licensing of any original tutorial code or third-party components remains subject to their respective licenses.

For code independently created for this repository, see the project's `LICENSE` file.

---

# 👤 Author

**Wael Mohamed**

AI Engineer in Training

Focused on:

* Generative AI
* Large Language Models
* Retrieval-Augmented Generation
* Agentic AI
* AI Engineering
* Production AI Systems

---

# ⭐ Acknowledgment

This project is developed as part of a hands-on learning journey based on the Mini-RAG educational project and its associated tutorials.

The purpose of this repository is to learn, experiment, understand the architecture, and progressively build practical AI engineering skills.
