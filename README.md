# PetRescue WhatsApp Automation

## Overview
This project demonstrates a simple automation pipeline that processes pet rescue or adoption messages. The system extracts important information from incoming messages and automatically stores the data in Google Sheets and schedules a follow-up call using Google Calendar.

The goal of this assignment is to build an automation workflow without using any LLM APIs.

---

## Problem Statement
When a rescue message is received (for example via WhatsApp), important information such as:

- Pet type
- Owner name
- Phone number
- Location

needs to be captured and stored. Additionally, a follow-up call must be scheduled.

This project automates that workflow.

---

## Example Input Message

Dog available for adoption  
Owner: Rahul  
Phone: 9876543210  
Location: Hyderabad  

---

## Workflow

1. Receive a text message containing pet rescue information
2. Parse the message and extract important details
3. Store the data in Google Sheets
4. Automatically create a follow-up call event in Google Calendar

---

## Project Structure

PetRescue-whatsapp/

main.py → Main script that runs the automation pipeline  
parser.py → Extracts pet rescue details from text messages  
sheets.py → Handles Google Sheets integration  
calendar_event.py → Creates Google Calendar events  
data/sample_message.txt → Example message for testing  
requirements.txt → Project dependencies  

---

## Technologies Used

- Python
- Google Sheets API
- Google Calendar API
- Regular Expressions
- spaCy (for entity extraction)

---

## Setup Instructions

### Clone the repository

git clone https://github.com/meghanahch1605/PetRescue-whatsapp.git

cd PetRescue-whatsapp

---

### Install dependencies

pip install -r requirements.txt

---

### Install spaCy model

python -m spacy download en_core_web_sm

---

### Configure Google APIs

1. Enable Google Sheets API
2. Enable Google Calendar API
3. Create OAuth credentials from Google Cloud
4. Download credentials file
5. Save it as:

client_secret.json

Place the file in the project directory.

---

### Run the project

python main.py

---

## Expected Output

### Google Sheets

Pet | Owner | Phone | Location  
Dog | Rahul | 9876543210 | Hyderabad  

---

### Google Calendar

Event created:

Pet Rescue Follow-up  
WhatsApp call with Rahul

---

## Features

- Automated message processing
- Data extraction from text
- Google Sheets data storage
- Google Calendar event scheduling
- API-based automation pipeline

---

## Author

Meghana harini Chollangi  
B.Tech Computer Science & Engineering (Data Science)  
Raghu Institute of Technology

---

## GitHub Repository

https://github.com/meghanahch1605/PetRescue-whatsapp
