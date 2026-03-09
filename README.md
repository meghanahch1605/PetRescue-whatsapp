# Pet Rescue WhatsApp Automation

This project implements a simple automation pipeline for a pet rescue/adoption workflow.

Instead of a website interface, the system processes incoming text messages describing pets available for adoption.

The system extracts important information, stores it in Google Sheets, and schedules a follow-up WhatsApp call using Google Calendar.

## Features

- NLP based text extraction using spaCy
- Extracts pet and owner information
- Saves data to Google Sheets
- Creates follow-up call events in Google Calendar
- Simple automation pipeline
- No LLM APIs used

## System Workflow

Text Message  
↓  
NLP Parsing  
↓  
Extract Pet + Owner Details  
↓  
Save to Google Sheets  
↓  
Schedule WhatsApp Call  

## Example Message

Hi, I want to give my dog for adoption.  
My name is Rahul and I live in Hyderabad.  
Please contact me at 9876543210.

## Technologies Used

Python  
spaCy NLP  
Google Sheets API  
Google Calendar API  

## Setup

Install dependencies

pip install -r requirements.txt

Download NLP model

python -m spacy download en_core_web_sm

Run the project

python main.py