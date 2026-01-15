# Flask User Management REST API

This is a simple REST API built with **Flask**, **PostgreSQL**, and **Docker Compose** for user and admin management.  
It supports:

- User signup, login, and profile update
- Admin signup, login, and managing users
- JWT-based authentication with role-based access
- PostgreSQL as the database
- Fully containerized using Docker Compose

---

## 🛠 Features

- Users can register, login, and update their details
- Admins can create users, update, or delete them
- JWT authentication with role claims (`user` or `admin`)
- UUIDs for user and admin IDs
- Optional soft-delete for users
- Pydantic validation for request payloads
- Dockerized for easy deployment

---

## 📦 Setup & Run with Docker

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_folder>
```

2. Create a .env file at the root with your environment variables:
```bashLOG_FILE=
JWT_SECRET_KEY=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_NAME=
DB_PORT=
```

3. Build and start the containers:
```bash
docker compose up --build
```

