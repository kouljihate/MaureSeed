# Changelog

All notable changes to MaureSeed will be documented in this file.

## [1.2.0] - 2026-09-07

### Added
- Seed data generator script (`data/generate_seeds.py`)
- 10,000 seed entries across 6 categories: vegetables, herbs, flowers, cereals, legumes, fruitiers
- 5 countries coverage: Morocco, Algeria, Tunisia, Mauritania, Mali
- Bilingual names (EN/AR) with variety prefixes and suffixes
- Trilingual descriptions (EN/FR/AR)

### Changed
- Arabic font VIP Rawy Thin applied to all RTL elements (buttons, inputs, labels, etc.)

## [1.1.0] - 2026-09-07

### Changed
- Removed "Our Countries" section from landing page and footer
- Replaced Google Fonts Noto Kufi Arabic with local VIP Rawy Thin font
- Grouped rounded language buttons in header (pill-style)
- Footer redesigned: About (left) / Empty (middle) / Useful Links (right) with extreme alignment
- Footer columns set to equal 3-column grid layout

### Added
- Local font file: `assets/fonts/VIP_Rawy_Thin.ttf`
- `@font-face` declaration for VIP Rawy Thin
- RTL-aware font switching: Comfortaa for EN/FR, VIP Rawy Thin for AR

## [1.0.0] - 2026-09-07

### Added
- Initial project structure with Flask backend
- MongoDB integration for seed storage
- Multilingual support (Arabic, French, English)
- Seed catalog with filtering by country and category
- Landing page with hero section, features, countries, and featured seeds
- Catalogue page with filters
- About and Contact pages
- Structured logging system with error context (script, function, line, code, description)
- Seed data for 5 countries: Morocco, Algeria, Tunisia, Mauritania, Mali
- API endpoints: /api/health, /api/seeds, /api/seeds/<id>, /api/countries, /api/categories
- Responsive CSS design inspired by seemaille.com
- Comfortaa font for English/French
- Noto Kufi Arabic font for Arabic
- Database seeding script
- README and CHANGELOG documentation
