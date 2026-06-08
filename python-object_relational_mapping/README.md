# Python - Object-relational mapping

## Description
This project explores two ways to interact with a MySQL database from Python:
- **MySQLdb**: connecting to MySQL and executing raw SQL queries directly from Python
- **SQLAlchemy**: using an ORM (Object-Relational Mapper) to manipulate database objects without writing SQL queries

## Requirements
- Python 3.8.5
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- MySQL 8.0

## Installation
```bash
pip3 install mysqlclient==2.0.3 --break-system-packages
pip3 install SQLAlchemy==1.4.22 --break-system-packages
```

## Usage
Scripts take 3 arguments: mysql username, mysql password, database name
```bash
./0-select_states.py <username> <password> <database>
```

## Author
Sagalou
