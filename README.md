# ToDo CLI App

A simple command-line ToDo list manager built in Python. This application allows users to create, list, delete, and analyze tasks based on priority — all in memory, with no external dependencies.

---

## ✨ Features

- ✅ Add tasks with a custom priority (lower number = higher priority)
- 📋 List all tasks sorted by priority
- 🗑️ Delete tasks using their unique task ID
- 📉 View all missing priorities between 1 and the current maximum
- 🧠 In-memory only (no database or file persistence required)

---


## 🖥️ Why I Chose a CLI Approach

The prompt emphasized building a simple, interactive, in-memory application — no persistence or complex infrastructure required.

A command-line interface allowed me to:

- Quickly implement all required features
- Focus on core logic, data structures, and user interaction
- Keep the solution lightweight and testable

The application is built with a class-based structure to ensure:

- Modular and maintainable code
- Easy extension in future phases (e.g., updating tasks, saving to file, etc.)

This design makes it easy to later:

- Add persistence
- Build a web API (e.g., Flask or FastAPI)
- Layer a UI (e.g., React or HTML/JS)

For a 90-minute take-home assessment focused on functionality and clarity, the CLI was the most efficient and appropriate choice.

---

## 🔧 Next Steps / How I’d Extend This

If given more time or if this were intended for deployment or collaboration, I would consider the following enhancements:

- **Persistence**  
  Save and load tasks using:
  - JSON or CSV files (lightweight)
  - SQLite or a local database (for structured storage)

- **API Integration**  
  Refactor core logic into a backend powered by:
  - Flask or FastAPI to expose REST endpoints

- **Web UI Layer**  
  Build a simple frontend using:
  - HTML/CSS and JavaScript, or
  - React for a dynamic and responsive experience

- **Testing**  
  Add unit tests with `unittest` or `pytest`  
 
