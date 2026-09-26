\# Report Generation \& Analytics



\## Project Description



Report Generation \& Analytics is a web-based application developed using Python Flask and MySQL. The system allows users to register, log in, generate reports, and view analytics through a simple dashboard.



\## Technologies Used



\* Python

\* Flask

\* MySQL

\* HTML

\* CSS

\* JavaScript

\* SQLAlchemy

\* PyMySQL

\* Chart.js

\* Git \& GitHub



\## Features



\* User Registration

\* User Login

\* Dashboard

\* Report Generation

\* Report Management

\* Analytics Dashboard

\* MySQL Database Integration



\## Project Structure



```text

report-generation-analytics/

│

├── app.py

├── README.md

├── database.sql

├── requirements.txt

├── .gitignore

├── venv/

│

└── templates/

&#x20;   ├── register.html

&#x20;   ├── login.html

&#x20;   ├── dashboard.html

&#x20;   ├── report.html

&#x20;   ├── report\_success.html

&#x20;   ├── analytics.html

&#x20;   └── static/

&#x20;       └── style.css

```



\## Database



The project uses MySQL database named `report\_analytics`.



Database tables:



\* `users`

\* `reports`



The `database.sql` file contains the database structure and table definitions.



\## Installation



\### 1. Clone the Repository



```bash

git clone https://github.com/divya-bharathi-4400/report-generation-analytics.git

cd report-generation-analytics

```



\### 2. Create Virtual Environment



```bash

py -m venv venv

```



\### 3. Activate Virtual Environment



For Windows PowerShell:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### 4. Install Required Packages



```bash

pip install -r requirements.txt

```



\### 5. Configure Database



Create a `.env` file in the project root and add your local MySQL configuration.



```text

MYSQL\_USER=root

MYSQL\_PASSWORD=your\_mysql\_password

MYSQL\_HOST=localhost

MYSQL\_DB=report\_analytics

SECRET\_KEY=your\_secret\_key

```



Do not upload the `.env` file to GitHub.



\### 6. Run the Application



```bash

python app.py

```



Open the application in your browser:



```text

http://127.0.0.1:5000

```



\## Application Workflow



1\. Register a new user.

2\. Login using the registered account.

3\. Open the dashboard.

4\. Generate a report.

5\. View generated report information.

6\. Open the analytics page to view report analytics.



\## Objective



The main objective of this project is to develop a simple web-based system for report generation and analytics using Flask, MySQL, HTML, CSS, and JavaScript.



\## Future Enhancements



\* Password hashing and improved authentication

\* Export reports as PDF

\* Advanced analytics and visualizations

\* Search and filtering

\* REST API integration

\* Cloud deployment



\## Author



\*\*Divya Bharathi\*\*



B.Tech Information Technology Student



