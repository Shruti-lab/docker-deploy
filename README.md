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

## Setup & Run with Docker

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

4. Stop containers:
```bash
docker compose down
```

## API Endpoints & Testing with cURL
### 1. Admin Signup
```bash
curl -X POST http://localhost:80/admin/signup \
  -H "Content-Type: application/json" \
  -d '{
        "username": "john",
        "password": "secure123",
        "email": "john@example.com"
      }'

```

### 2. User/Admin Login
```bash
curl -X POST http://localhost:80/auth/login \
  -H "Content-Type: application/json" \
  -d '{
        "email": "john@example.com",
        "password": "secure123",
        "role": "admin"
      }'
```
Response returns access_token and role.


### 3. Update User Profile (PUT /aboutme)
```bash
curl -X PUT http://localhost:80/user/aboutme \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
        "name": "John Doe",
        "password": "newpassword123"
      }'
```
- Fields name and password are optional; include only the ones you want to update.


### 4. Admin: Get All Users
```bash
curl -X GET http://localhost:80/admin/users \
  -H "Authorization: Bearer <ADMIN_ACCESS_TOKEN>"

```


### 5. Admin: Delete a User
```bash
curl -X DELETE http://localhost:80/admin/users/<USER_UUID> \
  -H "Authorization: Bearer <ADMIN_ACCESS_TOKEN>"
```



