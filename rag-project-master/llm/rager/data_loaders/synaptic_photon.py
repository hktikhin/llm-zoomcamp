import requests
import json
from typing import List, Dict


@data_loader
def ingest_api_data(*args, **kwargs) -> List[Dict]:
    endpoint = kwargs.get('endpoint')

    response = requests.request(method='GET', url=endpoint)
    response.raise_for_status()

    print(response.json()[0].keys())
    print(response.json()[0]['documents'][0].keys())


    return [response.json()]