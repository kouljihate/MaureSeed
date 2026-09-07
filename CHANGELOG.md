# Changelog

All notable changes to MaureSeed will be documented in this file.

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
