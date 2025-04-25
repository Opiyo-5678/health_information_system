                                               Health Information System 

Project Overview

This project is a basic Health Information System designed to manage clients and health programs/services. The system enables doctors (system users) to manage health programs, register clients, and enroll them in various health programs. Additionally, it provides an API to expose client data to other systems.

The system supports the management of health programs (e.g., TB, Malaria, HIV) and the enrollment of clients into these programs. The API allows for easy retrieval of client profiles and their enrolled programs.

 Features

- Create Health Programs : Doctors can create health programs (e.g., TB, Malaria, HIV).
- Register Clients: New clients can be added to the system.
- Enroll Clients in Programs: Clients can be enrolled in one or more health programs.
- Search Clients: Doctors can search for clients from a list of registered clients.
- View Client Profiles: Doctors can view detailed profiles of clients, including the health programs they are enrolled in.
- API Exposure: Client profiles are exposed via a RESTful API so that other systems can retrieve and use this information.

 Technologies Used

- Backend: Django (Python)
- Database: MySQL
- API Framework: Django REST Framework
- Database ORM: Django ORM for database management
- Docker (Optional): Containerization for easy deployment

 Installation & Setup

To set up the project locally, follow these steps:

 Prerequisites

- Python 3.9+ (or compatible version)
- MySQL 8.0+ (or compatible version)
- pip (Python package manager)
- Docker (optional for containerization)

 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/Opiyo-5678/health_information_system.git
cd health_information_system

 2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database (make sure MySQL is running):
    - Update the `DATABASES` setting in `settings.py` for MySQL.

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```
