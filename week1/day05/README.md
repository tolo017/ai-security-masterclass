# Week 1 Day 5 — AI Security API Scanner

## Overview

This project is part of my 16-week hands-on Generative AI Security Masterclass.

The objective of Week 1 is to build the core Python and software-engineering foundations required for later work in:

- Generative AI Security
- LLM Application Security
- AI Red Teaming
- Security Automation
- AI Security SaaS Engineering

Day 5 introduces HTTP, APIs, JSON payloads, API response handling, error handling, and basic security analysis.

The result is a small Python-based security scanner that communicates with an HTTP API, processes structured data, performs deterministic security checks, and generates machine-readable security results.

---

## Learning Objectives

By completing this project, I practiced:

- HTTP fundamentals
- GET and POST requests
- API request/response flow
- JSON request payloads
- JSON response parsing
- HTTP status codes
- Request timeouts
- Exception handling
- Response validation
- Basic prompt analysis
- Deterministic security policy decisions
- Structured security reporting

---

## Project Objective

Build a simple security-oriented API client that can:

1. Accept a prompt.
2. Send the prompt to an HTTP endpoint.
3. Receive a JSON response.
4. Validate the response.
5. Extract the relevant data.
6. Analyze the prompt.
7. Calculate a basic risk score.
8. Assign a security decision.
9. Save the result as JSON.
10. Generate a human-readable security report.

---

## Architecture

```text
                Prompt
                   |
                   v
        +---------------------+
        | Python Security     |
        | API Scanner         |
        +----------+----------+
                   |
                   | HTTP POST
                   v
        +---------------------+
        | Test HTTP API       |
        | (httpbin)           |
        +----------+----------+
                   |
                   | JSON Response
                   v
        +---------------------+
        | Response Validation |
        +----------+----------+
                   |
                   v
        +---------------------+
        | Prompt Analysis     |
        +----------+----------+
                   |
                   v
        +---------------------+
        | Risk Scoring        |
        +----------+----------+
                   |
                   v
        +---------------------+
        | Security Policy     |
        | ALLOW / REVIEW /    |
        | BLOCK               |
        +----------+----------+
                   |
                   v
        +---------------------+
        | JSON + Text Report  |
        +---------------------+
