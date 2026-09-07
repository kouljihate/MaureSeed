# MaureSeed

> Organic & Ancient Seeds from North Africa 🌱

**Version:** 1.12.0

## Overview

MaureSeed is a web application dedicated to preserving and promoting the seed heritage of North Africa and the Sahel region. It focuses on organic, ancient, and peasant seeds from **Morocco, Algeria, Tunisia, Mauritania, and Mali**.

Inspired by [semaille.com](https://semaille.com), MaureSeed adapts the concept to the Maghreb and Sahel agricultural context.

## Features

- **Multilingual:** Arabic / French / English
- **Organic Seeds:** Certified organic seed catalog
- **Heritage Varieties:** Ancient and traditional seed preservation
- **Regional Focus:** Morocco, Algeria, Tunisia, Mauritania, Mali
- **Reproducible Seeds:** Seeds that can be saved and replanted

## Tech Stack

- **Backend:** Python Flask
- **Database:** MongoDB (local)
- **Frontend:** HTML/CSS/JS (Jinja2 templates)
- **Fonts:** VIP Rawy Thin (Arabic), Comfortaa (English/French)

## Project Structure

```
MaureSeed/
├── main.py              # Flask application entry point
├── VERSION              # Version file
├── requirements.txt     # Python dependencies
├── BE/                  # Backend (API routes)
│   └── routes.py
├── FE/                  # Frontend (templates)
│   ├── routes.py
│   └── templates/
├── shared/              # Shared modules
│   ├── logger.py        # Logging with error context
│   ├── database.py      # MongoDB connection
│   ├── i18n.py          # Internationalization
│   └── utils.py         # Utility functions
├── config/              # Configuration
│   ├── config.py        # App config
│   └── i18n.py          # Translations
├── assets/              # Static assets
│   ├── css/
│   ├── js/
│   ├── fonts/
│   └── img/
├── data/                # Seed data & DB scripts
│   ├── seed_data.json       # 10,000 seeds catalog
│   ├── seed_db.py           # MongoDB seeder
│   └── generate_seeds.py    # Data generator
└── log/                 # Application logs
```

## Setup

### Prerequisites

- Python 3.10+
- MongoDB (local instance)

### Installation

```bash
# Clone the repository
git clone https://github.com/kouljihate/MaureSeed.git
cd MaureSeed

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Seed the database
python data/seed_db.py

# Run the application
python main.py
```

The app will be available at `http://localhost:5000`

## Admin Access

- **URL:** `/admin/login`
- **Username:** `admin`
- **Password:** `admin123`

### Admin Capabilities
- Manage seeds (Add/Edit/Delete)
- Manage customers
- View dashboard stats
- Manage payments (future)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/seeds` | List seeds (filter by country, category) |
| GET | `/api/seeds/<id>` | Get single seed |
| GET | `/api/countries` | List countries |
| GET | `/api/categories` | List categories |

## Logging

The application uses a structured logging system that captures:
- Script name
- Function name
- Line number
- Code context
- Error description

Logs are written to `log/maureseed.log`.

## Languages

Switch language via URL parameter: `?lang=fr`, `?lang=en`, `?lang=ar`

## License

All rights reserved.
