# Uptime Monitor Bot

## Overview
Telegram bot for website monitoring:
- BASIC plan: limited monitors, auto-expire
- PRIME plan: unlimited monitors, live debug, full analytics

## Features
- Inline keyboard UI (one-message policy)
- APScheduler for periodic checks
- SQLite database (Render compatible)
- Logs for PRIME users
- Admin panel for user & plan management

## Project Structure
- app.py → Entry point
- config.py → Bot token, admin IDs, limits
- bot/ → Inline keyboard UI, handlers
- core/ → Scheduler, monitor logic, restore jobs, limits
- database/ → SQLite connection, models, queries
- services/ → Business logic (user, prime, admin, logs)
- utils/ → Validators, cleaner, time helpers
- helpers/ → Wrapper functions
- logs/ → Runtime logs

## Requirements
