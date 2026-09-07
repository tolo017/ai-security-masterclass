# Week 1 Day 2 — Security Policy Decisions

## Concepts

- Comparison operators
- Boolean logic
- if / elif / else
- AND / OR / NOT
- Policy precedence
- Boundary testing

## Project

AI Security Policy Engine.

## Decision Model

BLOCK
REVIEW
ALLOW

## Security Lessons

- Authentication should be evaluated explicitly.
- Security conditions should be deterministic where appropriate.
- Policy order matters.
- Security rules require boundary testing.
- Decisions should include reasons.

## Limitations

The detector is intentionally simplistic and
is not a production prompt-injection defense.
