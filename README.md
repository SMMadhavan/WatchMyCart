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

