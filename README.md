# Diploma Project by Tach
## Purpose:
The application is designed to schedule the lessons of teachers working in the same classroom. And also to show off free time for recording, which parents can enroll.

## Overview

This repository contains the source code for a diploma project developed by Tach. The project is structured as a Django web application, with several apps included to handle different functionalities.


## Getting Started

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- PostgreSQL 13 or higher (or another supported database)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/tach-by/diploma_by_tach.git
```

2. Navigate to the project directory:

```bash
cd diploma_by_tach
```

3. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Apply migrations to set up the database:

```bash
python manage.py migrate
```

6. Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your superuser account.

### Running the Development Server

To start the development server, run:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

For any questions or issues, please open an issue on GitHub.

## Acknowledgments

- Django and Django REST Framework for providing a powerful and flexible framework for web development.
- All contributors to the project.

## Future Work

- Implement additional features and functionalities.
- Enhance the user interface and user experience.
- Add more comprehensive documentation and examples.
