# Weather Data ETL Pipeline

This project is an ETL pipeline built using Apache Airflow to extract weather data from an API, transform it, and load it into CSV formats. The pipeline is containerized using Docker and follows CI/CD best practices.

## Project Structure
```text
weather-data-etl/
├── dags/
│   └── weather_etl_dag.py            # Airflow DAG definition
|   └── scripts/
│       ├── __init__.py               # Makes scripts a package
│       ├── extract.py                # API data extraction
│       ├── transform.py              # Data transformation logic
│       └── load.py                   # Load to CSV/JSON
│
├── data/
│    └── raw_weather.json              # Raw data files
|    └── clean_weather.json            # Cleaned data        
|    └── weather_data.csv              # Final CSV output     
|
├── airflow/
│   ├── logs/                          # Ignored in git
│   └── plugins/                       # Ignored in git
|   └── init_airflow_users.sh          # Script to initialize users 
│
├── .env                               # Environment variables 
├── .gitignore                         # Ignore unnecessary files
├── docker-compose.yaml                # For spinning up Airflow via Docker
├── requirements.txt                   # Python dependencies
└── README.md                          # Project overview
```

## Features

- Fetches real-time weather data via an API
- Stores raw and cleaned data in JSON
- Loads final data into a CSV
- Scheduled and orchestrated using Apache Airflow
- Uses Docker for containerization

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Run the Project

1. Clone the repo:
   ```bash
   git clone https://github.com/CreativePrabhu/weather-data-etl.git
   cd weather-data-etl
2. Create your .env file (Add parameters: OPENWEATHER_API_KEY, WEATHER_CITY)
3. Start Airflow: docker-compose up --build
4. Access Airflow at: http://localhost:8080
5. Trigger the DAG
