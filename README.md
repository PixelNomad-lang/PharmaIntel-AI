# PharmaIntel-AI
AI-Powered Sales Intelligence for Laboratory &amp; Pharma
<div align="center">

# 🧪 PharmaIntel-AI

### AI-Powered Sales Intelligence Platform for Laboratory & Pharma

**Turn scattered sales data into AI-driven decisions — leads, customers, competitors, and pipeline, all in one intelligent workspace.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-TBD-lightgrey?style=for-the-badge)](#license)

[![Stars](https://img.shields.io/github/stars/your-username/pharmaintel-ai?style=social)](#)
[![Forks](https://img.shields.io/github/forks/your-username/pharmaintel-ai?style=social)](#)
[![Issues](https://img.shields.io/github/issues/your-username/pharmaintel-ai?color=orange)](#)
[![Last Commit](https://img.shields.io/github/last-commit/your-username/pharmaintel-ai?color=green)](#)

[Overview](#-overview) • [Features](#-features) • [Architecture](#-architecture) • [Tech Stack](#-tech-stack) • [Getting Started](#-getting-started) • [Roadmap](#-roadmap) • [Contributing](#-contributing)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Why PharmaIntel-AI](#-why-pharmaintel-ai)
- [Features](#-features)
- [AI Capabilities](#-ai-capabilities)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Database Schema](#-database-schema)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [API Reference](#-api-reference)
- [Testing](#-testing)
- [Security](#-security)
- [Roadmap](#-roadmap)
- [Future Enhancements](#-future-enhancements)
- [Skills Demonstrated](#-skills-demonstrated)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔭 Overview

**PharmaIntel-AI** is an enterprise-grade, AI-powered sales intelligence platform purpose-built for laboratory and pharmaceutical sales teams. It unifies fragmented data — hospitals, diagnostic labs, CRM records, competitor catalogs, and tender documents — into a single AI-driven system that identifies leads, recommends products, analyzes competitors, and predicts sales opportunities.

Instead of manual research across spreadsheets and PDFs, sales reps get a conversational AI assistant, live analytics dashboards, and semantic search over their entire document library.

**Built for:** Sales Executives · Regional Sales Managers · Business Development Executives · Product Managers · Marketing Teams · Distributors · Laboratory Equipment Companies

---

## 💡 Why PharmaIntel-AI

| Problem | PharmaIntel-AI Solution |
|---|---|
| Data scattered across CRM, Excel, PDFs, and email | Centralized data model + document ingestion (RAG) |
| Manual lead research takes hours | AI-scored leads, auto-generated customer summaries |
| No visibility into competitor positioning | Dedicated competitor intelligence module |
| Reps don't know which product fits which customer | ML-based product recommendation engine |
| Sales forecasting is guesswork | Forecasting models on historical sales data |
| Reports built manually every week | Auto-generated AI reports (weekly, territory, pipeline) |

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🧑‍💼 Customer Intelligence
- 360° customer profiles
- Purchase history timeline
- AI-driven lead scoring
- Behavioral customer segmentation

### 🤖 AI Sales Assistant
- Natural language query interface
- Context-aware recommendations
- Smart follow-up reminders
- Auto-generated sales pitches

### 📦 Product Intelligence
- Full product catalog
- Side-by-side product comparison
- Alternative/substitute suggestions
- Pricing & margin analysis

### 🏢 Company Intelligence
- Pharma company profiles
- Hospital & diagnostic lab database
- Research institute tracking

</td>
<td width="50%" valign="top">

### 🥊 Competitor Analysis
- Competitor product mapping
- Market positioning insights
- Feature-by-feature comparison
- Competitive pricing intelligence

### 📊 Sales Analytics
- Real-time revenue dashboard
- Sales trend visualization
- Region-wise performance breakdown
- Monthly / quarterly KPI tracking

### 📑 AI-Generated Reports
- Customer summary reports
- Weekly insight digests
- Territory performance analysis
- Sales pipeline reports

### 🔍 Document Intelligence (RAG)
- Semantic search over brochures, datasheets, tenders
- Auto-summarization of technical documents
- Source-cited AI answers

</td>
</tr>
</table>

---

## 🧠 AI Capabilities

The AI Agent (LangChain-orchestrated) can handle queries like:

```text
💬 "Show top laboratories in Gujarat."
💬 "Which customers haven't placed an order in the last 6 months?"
💬 "Recommend products for pathology labs."
💬 "Summarize this product brochure."
💬 "Compare Product A and Product B."
💬 "Generate a sales pitch for this customer."
💬 "Find similar products from our portfolio."
```

**Agent capabilities:** question answering · product recommendation · product comparison · sales pitch generation · brochure summarization · customer insight extraction · follow-up suggestions · market intelligence synthesis

---

## 🛠 Tech Stack

<table>
<tr><th>Layer</th><th>Technologies</th></tr>
<tr><td><b>Frontend</b></td><td>React, TypeScript, Vite, Tailwind CSS, shadcn/ui, Radix UI, Lucide Icons</td></tr>
<tr><td><b>State Management</b></td><td>TanStack Query (React Query), Zustand</td></tr>
<tr><td><b>Forms & Validation</b></td><td>React Hook Form, Zod</td></tr>
<tr><td><b>Data Visualization</b></td><td>Recharts, Chart.js</td></tr>
<tr><td><b>Backend</b></td><td>FastAPI, Python 3.11+, Uvicorn, Pydantic, SQLAlchemy, Alembic</td></tr>
<tr><td><b>API</b></td><td>REST, OpenAPI (Swagger), Async endpoints</td></tr>
<tr><td><b>Database</b></td><td>PostgreSQL</td></tr>
<tr><td><b>Authentication</b></td><td>JWT, Refresh Tokens, RBAC, bcrypt</td></tr>
<tr><td><b>AI Orchestration</b></td><td>LangChain, LangGraph (optional), OpenAI GPT / Gemini / Ollama</td></tr>
<tr><td><b>RAG Pipeline</b></td><td>PyMuPDF, pdfplumber, Unstructured, python-docx, Pandas</td></tr>
<tr><td><b>Embeddings</b></td><td>OpenAI Embeddings, BGE, Sentence Transformers</td></tr>
<tr><td><b>Vector Database</b></td><td>ChromaDB, FAISS, Qdrant</td></tr>
<tr><td><b>Machine Learning</b></td><td>Scikit-learn, XGBoost, LightGBM, Pandas, NumPy</td></tr>
<tr><td><b>Data Engineering</b></td><td>Pandas / Polars / SQL, Airflow (optional), Celery, Cron</td></tr>
<tr><td><b>File Storage</b></td><td>Local, AWS S3, Azure Blob</td></tr>
<tr><td><b>DevOps</b></td><td>Docker, Docker Compose, GitHub Actions (CI/CD)</td></tr>
<tr><td><b>Deployment</b></td><td>Render, Railway, VPS, AWS (later)</td></tr>
</table>

---

## 🏗 System Architecture

```
┌─────────────────────┐
│   React Frontend     │  (TypeScript · Tailwind · shadcn/ui)
└──────────┬───────────┘
           │  REST / WebSocket
           ▼
┌─────────────────────┐
│   FastAPI Backend     │  (Auth · Business Logic · Async APIs)
└──────────┬───────────┘
           │
   ┌───────┼─────────────┬─────────────┐
   ▼       ▼              ▼             ▼
PostgreSQL  ChromaDB   ML Models    File Storage
(core data) (vectors)  (Sklearn/XGB) (S3/Blob)
   │           │             │
   └─────┬─────┴─────────────┘
         ▼
   AI Agent (LangChain)
         │
         ▼
   LLM (GPT / Gemini / Ollama) + RAG
```

**Flow:** User queries hit FastAPI → structured data is fetched from PostgreSQL, unstructured context from ChromaDB (RAG), and predictions from ML models → the LangChain agent composes everything into a single grounded LLM response.

---

## 🗄 Database Schema

Core entity groups (PostgreSQL):

```
Identity & Access   → Users, Roles
CRM Core            → Companies, Customers, Leads, Activities, Meetings
Sales               → Sales, Quotations, Orders, Regions
Catalog             → Products, Competitors
Knowledge           → Documents, Notes
Ops                 → Tasks, Emails
```

> Full ERD to be added in `docs/erd.png` once schema is finalized in Alembic migrations.

---

## 📁 Project Structure

```text
pharmaintel-ai/
│
├── frontend/                # React + TypeScript app
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── store/
│   │   └── lib/
│
├── backend/
│   ├── api/                 # Route handlers
│   ├── models/               # SQLAlchemy models
│   ├── schemas/               # Pydantic schemas
│   ├── services/               # Business logic
│   ├── repositories/            # DB access layer
│   ├── ai/                       # LangChain agent + prompts
│   ├── rag/                       # Ingestion, chunking, retrieval
│   ├── ml/                         # Training + inference pipelines
│   ├── auth/                        # JWT, RBAC
│   ├── database/                     # Session, migrations
│   ├── core/                          # Config, settings
│   └── utils/
│
├── data/                     # Sample / seed data
├── documents/                 # Source docs for RAG ingestion
├── vector_db/                  # ChromaDB persistence
├── notebooks/                   # ML experimentation
├── tests/                        # Pytest + Vitest suites
├── docker/                        # Dockerfiles, compose configs
└── docs/                            # Architecture docs, ERD, API docs
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Docker & Docker Compose (recommended)

### Quick Start (Docker)

```bash
git clone https://github.com/<your-username>/pharmaintel-ai.git
cd pharmaintel-ai
cp .env.example .env   # fill in your secrets
docker-compose up --build
```

### Manual Setup

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

Backend runs on `http://localhost:8000` · API docs at `http://localhost:8000/docs` · Frontend on `http://localhost:5173`

---

## 🔐 Environment Variables

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/pharmaintel

# Auth
JWT_SECRET=
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# AI / LLM
OPENAI_API_KEY=
LLM_PROVIDER=openai   # openai | gemini | ollama

# Vector DB
VECTOR_DB_URL=
VECTOR_DB_COLLECTION=pharmaintel_docs

# File Storage
STORAGE_PROVIDER=local   # local | s3 | azure_blob
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```

---

## 📡 API Reference

> Auto-generated Swagger docs available at `/docs` once the backend is running. Key route groups planned:

| Route Group | Purpose |
|---|---|
| `/auth` | Login, refresh, RBAC-protected routes |
| `/customers` | CRUD + lead scoring endpoints |
| `/products` | Catalog, comparison, recommendations |
| `/companies` | Hospitals, labs, pharma companies |
| `/competitors` | Competitor product & pricing data |
| `/sales` | Orders, quotations, revenue analytics |
| `/documents` | Upload, ingestion status, RAG search |
| `/ai/chat` | AI assistant conversational endpoint |
| `/reports` | Generated report retrieval |

---

## 🧪 Testing

| Layer | Tooling |
|---|---|
| Backend | Pytest |
| Frontend | Vitest, Playwright (E2E, optional) |
| API | Postman collection (`docs/postman`) |

```bash
# Backend
cd backend && pytest

# Frontend
cd frontend && npm run test
```

---

## 🛡 Security

- HTTPS enforced in production
- CORS policy scoped to known origins
- Rate limiting on public endpoints
- JWT auth with RBAC (role-based access control)
- Input validation via Pydantic/Zod
- SQL injection & XSS protection
- CSRF protection (if cookie-based sessions used)
- Secrets managed via environment variables (never committed)
- Audit logging on sensitive actions

---

## 🗺 Roadmap

- [ ] **Phase 1** — Project setup (Git, Docker, FastAPI, React scaffolding)
- [ ] **Phase 2** — Authentication & user/role management
- [ ] **Phase 3** — Database schema + CRUD APIs
- [ ] **Phase 4** — Analytics dashboard
- [ ] **Phase 5** — File upload & document management
- [ ] **Phase 6** — RAG pipeline (embeddings + vector DB)
- [ ] **Phase 7** — AI assistant & chat interface
- [ ] **Phase 8** — ML models (lead scoring, forecasting, churn)
- [ ] **Phase 9** — Notifications & external integrations
- [ ] **Phase 10** — Testing, hardening, and production deployment

---

## 🔮 Future Enhancements

- CRM integrations — Salesforce, HubSpot, Zoho
- Email & WhatsApp automation
- Smart lead recommendation engine
- Tender opportunity tracking
- Territory planning tools
- Voice AI assistant
- Native mobile application

---

## 🎓 Skills Demonstrated

`Full-Stack Development` `PostgreSQL Schema Design` `REST API Development` `JWT & RBAC` `LLM Integration` `Retrieval-Augmented Generation` `Vector Databases & Semantic Search` `Applied Machine Learning` `ETL & Data Processing` `BI Dashboards` `Docker & CI/CD` `Enterprise Software Architecture`

---

## 🤝 Contributing

This is currently a solo portfolio build. Contribution guidelines will be added once the core MVP (Phases 1–3) is complete. In the meantime, feel free to open an issue for suggestions or bugs.

```bash
# Suggested workflow once open for contributions
git checkout -b feature/your-feature-name
git commit -m "feat: description of change"
git push origin feature/your-feature-name
# open a Pull Request
```

---

## 📄 License

License to be decided before the repository goes public (MIT recommended for a portfolio project).

---

<div align="center">

**Built with ❤️ by [Adarsh Shukla](https://github.com/your-username)**

*An AI + Data Engineering + Full-Stack portfolio project for the pharma & laboratory sales domain.*

</div>