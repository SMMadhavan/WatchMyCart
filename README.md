# WatchMyCart

WatchMyCart is a personal price-intelligence system that monitors product prices over time and notifies users when buying conditions become favorable.  
It is designed as an intelligent shopping assistant rather than a simple price tracker.

This project currently supports multi-product tracking, historical price analysis, and automated email alerts based on user-defined conditions.

---

## What the system does

At its current stage, WatchMyCart can:

- Accept a product URL  
- Fetch the current price of the product  
- Store price history with timestamps  
- Track multiple products independently  
- Analyze price trends per product  
- Detect when a product enters a target price range  
- Send real email alerts when conditions are met  

The system runs as a real data pipeline:

**Product URL → Price Collection → Data Storage → Analysis → Alert → User**

---

## Current Architecture

The project is structured as a modular system:

```text
src/
├── collector.py # Fetches product title and price from a URL
├── storage.py # Saves price history with timestamp and URL
├── analysis.py # Analyzes historical data and triggers alerts
├── notifier.py # Sends email alerts
├── main.py # Orchestrates the full workflow
data/
└── prices.csv # Historical price database (not committed to GitHub)
```

Each component has a single responsibility, making the system easy to extend and maintain.

---

## How it works

1. The user enters:
   - Product URL  
   - Target price range  
   - Email address  

2. WatchMyCart:
   - Fetches the product name and price  
   - Stores it in the price database  
   - Analyzes past prices for that product  
   - Checks if the price has entered the desired range  
   - Sends an email alert if the condition is met  

The alert system is event-based, meaning users are notified only when the price enters the desired range, not continuously while it remains there.

---

## Email system

WatchMyCart currently uses Gmail SMTP in developer mode.  
A single service email account sends alerts to users.

Users do **not** need to provide any credentials — they only receive emails.

This will later be upgraded to a production email service (SendGrid / Mailgun) for public deployment.

---

## Supported data source

The current implementation uses the public demo site:

**https://books.toscrape.com**

This site allows free and reliable price tracking for development and testing.  
The system is designed so that the collector can later be upgraded to support real e-commerce platforms.

---

## Current status

The project currently supports:

- Multi-product tracking  
- Historical price storage  
- Price trend analysis  
- Price-range based alerts  
- Real email notifications  

This represents a fully working **end-to-end intelligent price tracking system**.

---

## Future roadmap

Planned upgrades include:

- Web interface (GitHub Pages + backend)  
- Scheduled background tracking  
- Dashboard for all tracked products  
- Smarter price predictions  
- Production-grade email service  
- Support for real e-commerce websites  

---

WatchMyCart is designed to evolve from a learning project into a real consumer-facing tool, combining automation, data analysis, and human-centric decision support.
