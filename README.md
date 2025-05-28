# Concert Planning CLI + ORM Project

## Project Description

This project is a command-line interface (CLI) application that allows users to manage artists and concerts using Python and SQLite3. It demonstrates how to implement a basic ORM-like layer with raw SQLite3, performing CRUD (Create, Read, Update, Delete) operations with a one-to-many relationship between Artists and their Concerts.

Users can:

- Add and delete artists.
- List all artists or find a specific artist by name.
- Schedule concerts for artists (concerts belong to one artist).
- List all concerts or delete concerts.
- See how deleting an artist cascades to deleting their concerts.

This project applies best practices in Python programming, database design, and CLI user interaction.

---

## Project Structure

concert_project/
├── concert_db.py # Main Python module managing database interactions
├── test_concert_db.py # Test script to demonstrate database functionalities
├── README.md # This file: project overview and instructions
├── Pipfile # Pipenv environment dependencies file
├── Pipfile.lock # Pipenv lock file for reproducible environments
└── .gitignore # To exclude pycache, DB files, and env files

## Technologies Used

- Python 3.x
- SQLite3 (built-in Python library)
- Pipenv (for environment and dependency management)

## Setup Instructions

### 1. Clone the repository

```bash
git clone <git@github.com:JoyMitchel/phase-3-project.git>
cd concert_project
```
