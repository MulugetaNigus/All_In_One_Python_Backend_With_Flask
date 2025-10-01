# Flask Backend API

A robust REST API backend built with Flask, featuring user authentication, product management, and secure endpoints. Uses Supabase for database, Pydantic for validation, and JWT for authentication.

## Features

- **Authentication**: Register, login, logout, password reset
- **Product Management**: CRUD operations for products with filtering
- **Security**: JWT tokens with expiration, rate limiting, CORS
- **Validation**: Pydantic models for input/output validation
- **Database**: Supabase integration
- **Testing**: Unit tests with pytest
- **Deployment**: Ready for Heroku/Gunicorn

## Tech Stack

- **Backend**: Flask
- **Database**: Supabase (PostgreSQL)
- **Validation**: Pydantic
- **Auth**: PyJWT
- **Rate Limiting**: Flask-Limiter
- **CORS**: Flask-CORS
- **Deployment**: Gunicorn
- **Testing**: Pytest, Pytest-Mock

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd backend_with_py
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   JWT_SECRET_KEY=your_secret_key_here
   SUPABASE_URL=your_supabase_url
   SUPABASE_ANON_KEY=your_supabase_anon_key
   ```

5. **Run the app**:
   ```bash
   python app.py
   ```
   Or for production:
   ```bash
   gunicorn app:app
   ```

## Usage

The API is versioned under `/api/v1/`.

### Authentication Endpoints

- **POST** `/api/v1/register` - Register a new user
  - Body: `{"email": "user@example.com", "password": "securepassword"}`
- **POST** `/api/v1/login` - Login user
  - Body: `{"email": "user@example.com", "password": "securepassword"}`
- **POST** `/api/v1/signout` - Logout user
- **POST** `/api/v1/send-reset-password` - Send password reset email
- **POST** `/api/v1/change-password` - Change password

### Product Endpoints

All product endpoints require `Authorization: Bearer <token>` header.

- **GET** `/api/v1/product` - Get all products (with optional query params for filtering)
  - Query: `?name=laptop&price_gt=100`
- **POST** `/api/v1/product` - Add new product
  - Body: `{"name": "Product", "price": 10.99, "description": "Description", "imageUrl": "url"}`
- **PUT** `/api/v1/update-product` - Update product
- **DELETE** `/api/v1/delete` - Delete product
- **POST** `/api/v1/filter-product` - Filter products
  - Body: `{"name": "filter", "priceL": 50, "priceG": 100}`

## Testing

Run unit tests:
```bash
pytest test_app.py
```

Tests cover auth, CRUD operations, validations, and error handling.

## Deployment

### Heroku
1. Push to Heroku Git.
2. Set environment variables in Heroku dashboard.
3. Use `Procfile`: `web: gunicorn app:app`

### Local Production
```bash
gunicorn app:app --bind 0.0.0.0:8000
```

## Project Structure

```
backend_with_py/
├── app.py                 # Main Flask app
├── client.py              # Supabase client
├── middleware.py          # Auth middleware
├── requirements.txt       # Dependencies
├── Procfile               # Heroku deployment
├── test_app.py            # Unit tests
├── .env                   # Environment variables
├── models/
│   ├── auth/
│   │   └── auth_model.py  # User model
│   └── product/
│       └── product_model.py # Product model
├── Routes/
│   ├── auth/
│   │   └── route.py       # Auth routes
│   └── product/
│       └── route.py       # Product routes
└── utils/
    └── test_limit.py      # Rate limit testing
```

## Contributing

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Push and create PR

## License

MIT License
