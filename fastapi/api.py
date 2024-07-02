# Exemple de script pour interagir avec les APIs The Muse et Adzuna
import requests
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello World"}

def fetch_jobs_from_themuse(api_url):
    response = requests.get(api_url)
    return response.json()

def fetch_jobs_from_adzuna(api_url, app_id, app_key):
    headers = {'Content-Type': 'application/json'}
    params = {'app_id': app_id, 'app_key': app_key}
    response = requests.get(api_url, headers=headers, params=params)
    return response.json()

# Exemple d'utilisation
themuse_url = 'https://www.themuse.com/api/public/jobs'
adzuna_url = 'https://api.adzuna.com/v1/api/jobs'
adzuna_app_id = 'c23db5bf'
adzuna_app_key = 'aea5e40eda96c0ca90a5bbc23d75e311'
themuse_data = fetch_jobs_from_themuse(themuse_url)
adzuna_data = fetch_jobs_from_adzuna(adzuna_url, adzuna_app_id, adzuna_app_key)
print(themuse_data)
print(adzuna_data)
