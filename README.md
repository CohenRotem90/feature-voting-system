
# Feature Voting System

A Django-based feature voting app where users can propose and vote on feature requests.

## Features
- Submit new features
- Upvote existing features
- Login/logout and admin interface
- Responsive UI styled with Bootstrap

## Tech Stack
- Django
- MySQL
- Docker & Docker Compose

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/feature-voting-system.git
cd feature-voting-system
2. Start the app
bash
Copy
Edit
docker-compose up --build
This command will build and start both the Django app and MySQL database. It also runs migrations and creates the default superuser.

3. Admin Login
Visit: http://localhost:8000/admin

Username: admin

Password: Admin1234!

Note: The default superuser is created automatically by the startup script inside the Docker container.

4. Access the application
Visit http://localhost:8000/ to use the feature voting UI.

Troubleshooting
Make sure port 3306 is free on your host machine before running Docker.

Ensure Docker and Docker Compose are installed and running correctly.

If you modify the start.sh script, verify it still creates the superuser and runs migrations properly.

Prompts Used
See prompts.txt for all AI interactions and task delegation history.

Enjoy voting on features!
