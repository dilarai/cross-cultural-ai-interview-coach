# Project Plan

## Project Name

Cross-Cultural AI Interview Coach

---

## Problem Statement

Candidates applying for jobs abroad often struggle not because of their technical skills, but because they are unfamiliar with the communication styles and cultural expectations of interviews in different countries.

Most interview preparation tools provide generic feedback and do not account for country-specific hiring cultures.

This project aims to help candidates prepare for interviews by providing culturally-aware interview coaching and feedback.

---

## Goal

Build an AI-powered interview coaching platform that:

* Simulates interview sessions
* Evaluates candidate responses
* Provides country-specific feedback
* Suggests culturally appropriate improvements
* Helps users adapt their communication style for different job markets

---

## Target Users

* New graduates
* Software developers applying abroad
* Professionals changing careers
* International job seekers

---

## MVP Scope (Version 0.1)

### Country Support

* Germany

### Features

* Start interview session
* Ask predefined interview questions
* Collect user responses
* Evaluate responses using an LLM
* Provide coaching feedback
* Suggest improvements before moving to the next question

### Excluded from MVP

* RAG
* Memory
* Multi-country support
* Authentication
* Database persistence

---

## Core Components

### Interviewer

Responsible for:

* Asking interview questions
* Managing interview flow

### Cultural Coach

Responsible for:

* Reviewing user responses
* Detecting culturally weak answers
* Suggesting improvements

Example:

User:
"I basically did everything myself."

Coach:
"This answer may sound overly individualistic in a German interview context. Consider highlighting teamwork and collaboration."

---

## User Flow

1. User selects Germany.
2. Interviewer asks a question.
3. User submits an answer.
4. Cultural Coach evaluates the answer.
5. User can:

   * Accept the suggestion
   * Edit their answer
   * Continue anyway
6. Interview proceeds to the next question.

---

## Planned Technology Stack

### Frontend

* Next.js
* TypeScript
* Tailwind CSS

### Backend

* FastAPI

### LLM

* OpenAI API

### Deployment

* Docker

---

## Future Roadmap

### Version 0.2

* Session Memory
* Adaptive follow-up questions

### Version 0.3

* RAG
* Cultural knowledge base
* Country-specific retrieval

### Version 0.4

* Multiple countries

  * Germany
  * United Kingdom
  * United States

### Version 1.0

* Real-time Cultural Coach
* Personalized coaching
* Recruiter and Coach personas
* User progress tracking

---

## Long-Term Vision

The platform should act as an intelligent interview coach rather than a simple chatbot.

Users should learn how to communicate effectively in different professional cultures and improve their interview performance through interactive coaching.

---

## Success Criteria

A user can:

1. Select Germany as a target country.
2. Complete a mock interview.
3. Receive culturally-aware coaching feedback.
4. Improve responses before continuing.

The system should function as an interview coach rather than a simple question-answer system.
