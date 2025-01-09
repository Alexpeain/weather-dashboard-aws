# Weather data collection and storage system

A simple weather data collection built with Python that fetches weather data from an API and stores it in an AWS S3 bucket.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [License](#license)

## Features

- Fetch current weather data for any city.
- Store weather data in JSON format in an AWS S3 bucket.
- Easy to set up and run with minimal dependencies.

## Technologies Used

- **Python**: Programming language used for development.
- **Boto3**: AWS SDK for Python to interact with AWS services.
- **Requests**: Library for making HTTP requests to the weather API.
- **Python-dotenv**: To manage environment variables securely.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/alexpeain/weather-dashboard.git
   cd weather-dashboard
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Add AWS and Weather API credentials to the `.env` file

   ```python
   region=ap-southeast-1
   aws_access_key_id=YOUR_AWS_ACCESS_KEY
   aws_secret_access_key=YOUR_AWS_SECRET_KEY
   bucket_name=your-s3-bucket-name
   weather_api_key=your-weather-api-key

   ```

## Usage

1. Run the Weather Dashboard:

```bash
   python main.py
```

## License

This project is licensed under the MIT License.
