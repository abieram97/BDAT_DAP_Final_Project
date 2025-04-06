===============================
  DATA INSIGHT HUB - README
===============================

This is a full-featured Flask web application for uploading, analyzing, and visualizing CSV datasets. It includes user authentication, dataset storage, API access, admin role features, and export to Google Sheets.

===============================
  DATA INSIGHT HUB - Team
===============================
Bitto Benny
Ashik Kulanjaraveliyil Shajimon
Neha Anna Mathew
Abhiram Raveendran
Rishita Setia
Gurleen kaur

-------------------------------
         FEATURES
-------------------------------
- User registration and login
- Upload and store CSV files
- Display datasets in an interactive table
- Export datasets to Google Sheets
- Interactive filters and charting using Google Charts
- REST API for accessing and querying data
- Admin dashboard with role promotion, dataset delete/restore

-------------------------------
        TECH STACK
-------------------------------
- Backend: Python, Flask, SQLAlchemy
- Frontend: Bootstrap 5, HTML, JS, Google Charts
- Database: SQLite
- API Integration: Google Sheets (via service account)

-------------------------------
    PROJECT STRUCTURE
-------------------------------
FlaskDataApp/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── data.py
│   ├── api.py
│   ├── models.py
│   ├── utils.py
│   ├── templates/
│   └── static/
├── run.py
├── requirements.txt
├── README.txt
└── instance/
    └── data.db

-------------------------------
    SETUP INSTRUCTIONS
-------------------------------
1. Install Python and pip
2. Create virtual environment:
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python run.py

5. Open in browser:
   http://127.0.0.1:5000

-------------------------------
    MAKE YOURSELF ADMIN
-------------------------------
1. Open terminal and run:
   flask shell

2. Paste this:
   from app import create_app, db
   from app.models import User
   app = create_app()
   with app.app_context():
       user = User.query.filter_by(username="your_username").first()
       user.role = "admin"
       db.session.commit()

-------------------------------
      API ENDPOINTS
-------------------------------
GET  /api/datasets
GET  /api/datasets/<dataset_id>/records?filter=value
PUT  /api/datasets/<dataset_id>/records   (admin only)
DELETE /api/datasets/<dataset_id>/records (admin only)

-------------------------------
    SUBMISSION NOTES
-------------------------------
- All project requirements are implemented
- Bonus features (admin dashboard, soft delete, restore) are included
- Ready for demo and evaluation

-------------------------------
© 2025 | joe
===============================
