import os
import requests
import boto3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
region = os.getenv("region")
if not region:
    raise ValueError("Region is not set in the .env file")

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def save_to_s3(data):
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=region
    )
    s3.put_object(Bucket=os.getenv("BUCKET_NAME"), Key='weather_data.json', Body=str(data))

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    print(weather_data)

    save_to_s3(weather_data)
    print("Weather data saved to S3.")