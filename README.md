# Automation Test Project: Modul 12.3

This repository contains a comprehensive automation testing framework developed during a QA course. It includes tests for **UI**, **API**, and **database** layers, using **Pytest**, **Selenium**, and the **Page Object Model** architecture.

---

## Project Structure

```bash
automation_test_modul12.3/ 
|── modules/ 
| ├── api/clients/ 
│ │ └── github.py 
│ ├── common/ 
│ │ └── database.py 
│ └── ui/
│   ├── base_page.py 
│   ├── amazon_search_page.py 
|   ├── witamin_cart_page.py
│   ├── sign_in_page.py 
│   └── test_ui.py 
├── tests/ 
│ ├── api/ 
│ │ ├── test_api.py 
│ │ ├── test_fixture.py 
│ │ ├── test_github_api.py 
│ │ └── test_http.py 
│ ├── database/ 
│ │ ├── test_database.py 
│ │ ├── test_db_product.py 
| | └── test_db_structure.py
│ └── ui/ 
│   ├── test_ui_github_login.py 
|   ├── test_amazon_search.py
│   ├── test_ui_page_object.py 
|   ├── test_witamin_add_to_cart.py
├── conftest.py 
├── pytest.ini 
└── README.md
```

---

## Technologies Used

- **Python 3.12**
- **Pytest** — test framework
- **Selenium** — UI automation
- **Requests** — API testing
- **SQLite / PostgreSQL** — database layer
- **Page Object Model** — UI architecture
- **webdriver-manager** — driver handling

---

## Test Coverage

### UI Tests:
- GitHub login page validation
- Page title verification
- Page Object structure

### API Tests:
- GitHub API response validation
- HTTP status checks
- Fixture-based test setup

### Database Tests:
- SQL query validation
- Connection and data integrity checks
---

## How to Run Tests

```bash

# Run all tests
pytest 

# Run only UI tests
pytest -m ui
Notes
This project demonstrates multi-layer testing skills and a clean modular structure. It was developed as part of a certified QA automation course and includes both required and extended functionality.
