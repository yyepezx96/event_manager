# Event Manager Company - User Management API

Welcome to the **Event Manager Company** onboarding project prepared by Yarlina Yepez Cuesta!  
This FastAPI-based secure REST API provides robust user management features, including registration, login, user profile updates, and authentication via JWT token-based OAuth2.  
It also serves as the foundation for future event management and registration capabilities that will be used for next project: *The final*

---

## 🛠️ Technologies Used

- FastAPI
- SQLAlchemy
- Alembic
- Docker & Docker Compose
- JWT Authentication (OAuth2 Password Flow)
- Pytest for Testing
- GitHub for Collaboration

---

## 📋 Issues Resolved

Below are the key issues I addressed during the assignment, each linked to its GitHub Issue and Pull Request:

1. [✅ Username Validation](https://github.com/yyepezx96/event_manager/issues/1) — Enforced allowed characters, min/max length (3–30), no spaces or special characters.
2. [✅ Password Validation](https://github.com/yyepezx96/event_manager/issues/3) — Enforced strong passwords (uppercase, lowercase, digit, special character, min 8+ chars).
3. [✅ Profile Field Edge Cases](https://github.com/yyepezx96/event_manager/issues/5) — Handled bio, profile picture, LinkedIn URL updates properly (together and individually).
4. [✅ 403 Forbidden for Admin Access to `/users/{user_id}`](https://github.com/yyepezx96/event_manager/issues/9) — Ensured only ADMIN and MANAGER roles can access sensitive endpoints.
5. [✅ Swagger UI Bearer Token + create_access_token Fix](https://github.com/yyepezx96/event_manager/issues/11) — Implemented Swagger HTTPBearer token support and verified JWT token behavior in tests.
6. [✅ Login Issue After Registration - 500 Error](https://github.com/yyepezx96/event_manager/issues/7) - Resolved a 500 Internal Server Error by ensuring newly registered users have verified emails and correct roles for successful login

---

## 🚀 Local Setup & Testing

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/event_manager.git
   cd event_manager
   ```

2. **Start with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Explore the App**
   - API Docs (Swagger): http://localhost/docs
   - PGAdmin: http://localhost:5050

4. **Run Tests**
   ```bash
   docker-compose exec fastapi pytest
   ```

5. **(Optional) Check Test Coverage**
   ```bash
   docker-compose exec fastapi pytest --cov=app --cov-report=term-missing
   ```

---

## 🐳 DockerHub Image

The project has been containerized for easy deployment and testing!

You can pull the latest image from DockerHub:

**DockerHub Repository:**

➡️ [yarlina/event_manager:latest](https://hub.docker.com/r/yarlina/event_manager)

**To pull and run the image locally:**

```bash
docker pull yarlina/event_manager:latest
docker run -d -p 8000:8000 yarlina/event_manager:latest
```
---

## ✨ Reflection

Throughout this assignment, I strengthened my skills in various areas of coding and issue resolution. Some of the areas I practice and improved are FastAPI development, REST API security, automated testing with Pytest, and collaborative GitHub workflows.  
I learned the importance of thorough test coverage, how to debug token-based auth issues, and how to customize documentation for usability. Specifically, I gained a better understanding of reading the code, finding where the issue is and understanding what the code is asking to do.

A major takeaway was fixing the 403 access bug tied to user roles and realizing how critical and important dependency injection and test fixtures are in complex backend systems. Out of all the issues encounteered, I can say this was the most tidious for me as I had to go back to various test files to ensure that the 403 and 401 were correctly used.  
I also gained hands-on experience enhancing Swagger UI, a skill that will be especially useful when developing and testing APIs in real-world environments and that I look forward to experimenting with.

---

## 📚 Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Alembic Migrations](https://alembic.sqlalchemy.org/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Docker](https://docs.docker.com/)

---

## ✅ Final Checklist

- [x] 5 Issues resolved with PRs plus 1 Issue from Professor's Video
- [x] All PRs merged into `main`
- [x] Full test suite passed (110+ tests)
- [x] Swagger UI Bearer token works
- [x] README updated with links and reflection

