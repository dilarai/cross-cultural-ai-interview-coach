# Architecture

## Overview

The system consists of:

* Next.js frontend
* FastAPI backend
* OpenAI API integration

---

## MVP Architecture

User
↓
Frontend (Next.js)
↓
Backend (FastAPI)
↓
OpenAI API
↓
Coach Feedback

---

## Components

### Frontend

Responsibilities:

* Country selection
* Interview UI
* Answer submission
* Feedback display

### Backend

Responsibilities:

* Session management
* Interview flow
* Prompt construction
* OpenAI communication

### Cultural Coach

Responsibilities:

* Evaluate answers
* Detect cultural issues
* Suggest improvements

---

## Future Components

### Memory

Store:

* Previous answers
* Common mistakes
* Accepted suggestions

### RAG

Provide:

* Country-specific interview knowledge
* Cultural context
* Hiring expectations

### Multi-Country Support

Supported countries:

* Germany
* United Kingdom
* United States
