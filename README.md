
---

# Flask API for LGD Data Processing

This project implements a Flask API for processing LGD-related JSON data in India. It also allows for retrieving state mappings from an SQLite database, and creating a mapped dataset based on provided input.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [Endpoints](#endpoints)
- [Examples](#examples)
  - [Processing LGD Data](#processing-lgd-data)
  - [Retrieving State Mappings](#retrieving-state-mappings)
  - [Creating Mapped Dataset](#creating-mapped-dataset)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- Python (>= 3.6)
- Flask
- Pandas

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bippisb/Map2LGD-APIs.git
   cd your-repo
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the API

To start the Flask API, run the following command in your terminal:

```bash
python app.py
```

The API will start, and you can access it at `http://localhost:5000`.

### Endpoints

The API provides the following endpoints:

- `POST /process_json`: Process a JSON request related to LGD and return a subset of the data.
- `GET /state_mappings`: Retrieves state mappings from the SQLite database.
- `POST /create_mapped_dataset`: Create a mapped dataset based on the provided dataset and mapping.

## Examples

### Processing LGD Data

Send a POST request to `http://localhost:5000/process_json` with a JSON payload containing LGD-related data. The API will return a JSON response with the specified columns.

Example Request:

```json
{
  "state_name": ["JAMMU AND KASHMIR", "JAMMU AND KASHMIR", "JAMMU AND KASHMIR", "JAMMU AND KASHMIR", "JAMMU AND KASHMIR"],
  "district_name": ["KUPWARA", "KUPWARA", "KUPWARA", "KUPWARA", "KUPWARA"],
  "sub_district_name": ["Kupwara", "Kupwara", "Kupwara", "Kupwara", "Kupwara"],
  "block_name": ["Hayhama", "Hayhama", "Hayhama", "Qadirabad", "Qadirabad"]
  "code":[239712, 288853, 239712, 288853, 7246, 239705, 239704, 7257, 7278, 7247, 239342, 239348, 7382]
}
```

Example Response:

```json
{
  "state_name": ["JAMMU AND KASHMIR", "JAMMU AND KASHMIR", "JAMMU AND KASHMIR", "JAMMU AND KASHMIR", "JAMMU AND KASHMIR"],
  "district_name": ["KUPWARA", "KUPWARA", "KUPWARA", "KUPWARA", "KUPWARA"],
  "sub_district_name": ["Kupwara", "Kupwara", "Kupwara", "Kupwara", "Kupwara"],
  "block_name": ["Hayhama", "Hayhama", "Hayhama", "Qadirabad", "Qadirabad"]
}
```

### Retrieving State Mappings

Send a GET request to `http://localhost:5000/state_mappings`. The API will return a JSON response with the mapping of Indian state names to codes.

Example Response:

```json
{
    "andaman & nicobar island": 35,
    "andaman and nicobar islands": 35,
    "andhra pradesh": 28,
    "arunachal pradesh": 12,
    "assam": 18,
    "bihar": 10,
    "chandigarh": 4,
    "chhattisgarh": 22,
    "dadra and nagar haveli": 26,
    "daman and diu": 25,
    "delhi": 7,
    "goa": 30,
    "gujarat": 24,
    "haryana": 6,
    "himachal pradesh": 2,
    "jammu and kashmir": 1,
    "jharkhand": 20,
    "karnatak": 29,
    "karnataka": 29,
    "kerala": 32,
    "ladakh": 37,
    "lakshadweep": 31,
    "madhya pradesh": 23,
    "maharashtra": 27,
    "manipur": 14,
    "meghalaya": 17,
    "mizoram": 15,
    "nagaland": 13,
    "odisha": 21,
    "puducherry": 34,
    "punjab": 3,
    "rajasthan": 8,
    "sikkim": 11,
    "tamil nadu": 33,
    "telangana": 36,
    "the dadra and nagar haveli and daman and diu": 38,
    "tripura": 16,
    "ut of dnh and dd": 38,
    "uttar pradesh": 9,
    "uttarakhand": 5,
    "west bengal": 19
}
```


### Creating Mapped Dataset

Send a POST request to `http://localhost:5000/create_mapped_dataset` with a JSON payload containing a 'dataset' and 'mapping'. The API will return a JSON response with the mapped dataset.

Example Request:

```json
{
  "dataset": {
    "state_name": ["JAMMU AND KASHMIR", "JAMMU AND KASHMIR", "JAMMU AND KASHMIR"],
    "district_name": ["KUPWARA", "KUPWARA", "KUPWARA"],
    "sub_district_name": ["Kupwara", "Kupwara", "Kupwara"],
    "block_name": ["Hayhama", "Hayhama", "Hayhama"]
  },
  "mapping": {
    "jammu and kashmir": "01",
    "jk": "01",
    "j&k": "01",
    "jnk": "01"
  }
}
```

Example Response:

```json
[
  {
    "state_name": "JAMMU AND KASHMIR",
    "district_name": "KUPWARA",
    "sub_district_name": "Kupwara",
    "block_name": "Hayhama",
    "state_code": "01"
  },
  {
    "state_name": "JAMMU AND KASHMIR",
    "district_name": "KUPWARA",
    "sub_district_name": "Kupwara",
    "block_name": "Hayhama",
    "state_code": "01"
  },
  {
    "state_name": "JAMMU AND KASHMIR",
    "district_name": "KUPWARA",
    "sub_district_name": "Kupwara",
    "block_name": "Hayhama",
    "state_code": "01"
  }
]
```

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Description of changes'`
4. Push to the branch: