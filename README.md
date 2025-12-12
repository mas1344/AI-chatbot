# AI-chatbot
This repository is for a AI RAG chat bot.
Här är ett utkast på en professionell och snygg `README.md` för ditt projekt. Den är strukturerad för att vara tydlig för både lärare och framtida arbetsgivare, och förklarar flödet i din RAG-applikation.

-----

# 🤖 The Data Engineer AI Chatbot

Välkommen till **The Data Engineer AI Chatbot**\! Detta projekt är en avancerad RAG-applikation (Retrieval-Augmented Generation) som låter användare ställa frågor om Data Engineering och få svar baserade på transkriptioner från "The Youtuber".

Chatboten är byggd med en personlighet som speglar en entusiastisk expert inom fältet och använder de senaste verktygen inom AI-utveckling.

-----

## 🚀 Kom igång (Getting Started)

Följ dessa steg för att sätta upp projektet lokalt:

### 1\. Förutsättningar

  * Python 3.11+
  * En **Google Gemini API-nyckel** (för embeddings och textgenerering).

### 2\. Installation

Klona repot och installera beroenden (exempel med `uv`):

```bash
git clone <din-repo-url>
cd AI-chatbot
uv sync
```

### 3\. Miljövariabler

Skapa en `.env`-fil i rotkatalogen och lägg till din API-nyckel:

```bash
GEMINI_API_KEY="din_api_nyckel_här"
```

### 4\. Ingesta data (Skapa din Knowledge Base)

Innan du kör chatboten måste du bearbeta transkriptionerna och lagra dem i vektordatabasen:

```bash
# Kör skriptet som omvandlar .md till .txt och skapar embeddings i LanceDB
python backend/ingest_data.py
```

### 5\. Starta applikationen

Starta FastAPI-servern och Streamlit-frontend i två olika terminaler:

**Terminal 1 (Backend):**

```bash
uv run uvicorn api:app --reload
```

**Terminal 2 (Frontend):**

```bash
streamlit run app.py
```

-----

## 🏗️ Arkitektur & Systemöversikt

Projektet är uppdelat i en tydlig pipeline där data flödar mellan olika komponenter:

1.  **Data Ingestion:** `.md`-filer läses in, städas och delas upp.
2.  **Vector Database:** **LanceDB** används för att lagra text och dess vektorgenererade motsvarigheter via `gemini-embedding-001`.
3.  **RAG-logik:** **PydanticAI** agerar som orkestrerare. När en fråga ställs hämtar den relevant kontext från LanceDB via ett "Tool".
4.  **API:** **FastAPI** serverar chatbotens logik genom en POST-endpoint.
5.  **Frontend:** **Streamlit** erbjuder ett användarvänligt gränssnitt för att chatta med agenten.
6.  **Deployment:** API:et är förberett för serverless deployment via **Azure Functions**.

-----

## ✨ Höjdpunkter (Highlights)

  * **Personlighet:** Agenten är instruerad via en system-prompt att svara med energin hos en Youtuber – pedagogiskt, engagerat och direkt.
  * **Strukturerad Output:** Tack vare `PydanticAI` returnerar agenten alltid svar i ett strikt definierat format (`RagResponse`), vilket minimerar fel.
  * **Vektorsökning:** Använder semantisk sökning för att hitta rätt information även om användaren inte använder exakt samma ord som i videon.

-----

## 📸 Skärmdumpar



> **Exempel:** Här ser vi hur agenten svarar på en fråga om "API trafiklab" och samtidigt anger källfilen den använde.

-----

### 🛠 Verktyg i urval

  * **LanceDB** - Vektordatabas.
  * **PydanticAI** - Agent-ramverk.
  * **Google Gemini** - LLM & Embeddings.
  * **FastAPI** - API-hantering.
  * **Streamlit** - Användargränssnitt.

-----

