# Structure
```
graphql_app/
│
├── app/
│   ├── api/
│   │   ├── v1/                   # Version 1 of the API
│   │   │   ├── graphql/
│   │   │   │   ├── schema.py        # Defines GraphQL types and resolvers for pets
│   │   │   │   ├── mutations.py     # GraphQL mutations (e.g., addPet, updatePet)
│   │   │   │   ├── queries.py       # GraphQL queries (e.g., getPet, listPets)
│   │   │   │   └── subscriptions.py # GraphQL subscriptions for real-time updates (if needed)
│   │   │   └── routers.py           # FastAPI routes (GraphQL endpoint)
│   │
│   ├── core/
│   │   ├── config.py                # Application configuration
│   │   ├── database.py              # Database connection (using SQLModel)
│   │   ├── exceptions.py            # Custom exceptions
│   │   └── middleware/              # Middleware for requests
│   │       ├── auth_middleware.py   # Middleware for authentication
│   │       ├── logging_middleware.py # Middleware for request/response logging
│   │       └── __init__.py
│   │
│   ├── models/                      # SQLModel data models
│   │   └── models.py                   # Pet model (e.g., id, name, breed, age)
│   │
│   ├── repositories/                # Data access logic
│   │   ├── pet_repository.py        # Queries and updates for pets
│   │   └── owner_repository.py      # Queries and updates for owners
│   │
│   ├── services/                    # Business logic
│   │   ├── pet_service.py           # Logic for managing pets
│   │   └── owner_service.py         # Logic for managing owners
│   │
│   └── main.py                      # Application entry point
│
├── tests/                           # Test cases
│   ├── test_pets.py                 # Tests for pet-related functionality
│   ├── test_owners.py               # Tests for owner-related functionality
│   └── test_api.py                  # Tests for the API endpoints
│
├── Dockerfile                       # Docker container configuration
├── docker-compose.yml               # Infrastructure setup (PostgreSQL, Redis)
└── requirements.txt                 # Project dependencies
```

