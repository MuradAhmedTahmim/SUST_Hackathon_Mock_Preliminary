# Ticket Sorter API

A Django REST Framework based CRM ticket classification service.

## Features

* Wrong Transfer Detection
* Payment Failure Detection
* Refund Request Detection
* Phishing Detection
* Bangla Language Support
* Confidence Scoring
* Human Review Flagging

## Tech Stack

* Python
* Django
* Django REST Framework

## Endpoints

### GET /health

Response:

{
"status": "ok"
}

### POST /sort-ticket

Request:

{
"ticket_id": "T-001",
"message": "I sent money to wrong number"
}

Response:

{
"ticket_id": "T-001",
"case_type": "wrong_transfer",
"severity": "high",
"department": "dispute_resolution",
"agent_summary": "Customer reports sending money to the wrong recipient.",
"human_review_required": true,
"confidence": 0.90
}

## Installation

pip install -r requirements.txt

python manage.py runserver

## Deployment

Render
