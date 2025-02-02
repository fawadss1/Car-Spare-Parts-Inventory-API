# Car Spare Parts Inventory API

## Features

- Create, Read, Update, and Delete (CRUD) spare parts
- Filter spare parts by compatible car model and price range
- Uses Django REST Framework (DRF)
- SQLite as database options
- Includes faker for papulating data

## Technologies Used

- Python 3
- Django 5
- Django REST Framework
- SQLite
- Django Filters

## Installation

### 1. Clone the Repository

```sh
 git clone https://github.com/fawadss1/Car-Spare-Parts-Inventory-API.git
 cd car-spare-parts-api
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

```sh
pip install django djangorestframework django-filter faker
```

### 4. Start the Server

```sh
python manage.py runserver
```

## API Endpoints

| Method | Endpoint               | Description                 |
| ------ | ---------------------- | --------------------------- |
| GET    | /api/spare-parts/      | Fetch all spare parts       |
| GET    | /api/spare-parts/{id}/ | Fetch a specific spare part |
| POST   | /api/spare-parts/      | Add a new spare part        |
| PUT    | /api/spare-parts/{id}/ | Update a spare part         |
| DELETE | /api/spare-parts/{id}/ | Delete a spare part         |

## Filtering Spare Parts

Use query parameters to filter spare parts:

- `model=Toyota` (Filter by compatible car model)
- `min_price=50` (Filter by minimum price)
- `max_price=200` (Filter by maximum price)

Example:

```sh
GET http://127.0.0.1:8000/api/spare-parts/?model=Toyota&min_price=50&max_price=200
```

### Example Postman Testing

#### 1. Fetch All Spare Parts

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/spare-parts/`

#### 2. Fetch Spare Part by ID

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/spare-parts/1/`

#### 3. Create a Spare Part

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/api/spare-parts/`
- **Body:**

```json
{
  "name": "Brake Pad",
  "price": 75.99,
  "compatible_models": "Toyota, Honda",
  "quantity": 10,
  "description": "High-quality brake pad."
}
```

#### 4. Update a Spare Part

- **Method:** PUT
- **URL:** `http://127.0.0.1:8000/api/spare-parts/1/`
- **Body:**

```json
{
  "name": "Updated Brake Pad",
  "price": 80.99,
  "compatible_models": "Toyota, Nissan",
  "quantity": 5,
  "description": "Updated high-quality brake pad."
}
```

#### 5. Delete a Spare Part

- **Method:** DELETE
- **URL:** `http://127.0.0.1:8000/api/spare-parts/1/`

### Papulate Data

```sh
python papulateData.py
```
