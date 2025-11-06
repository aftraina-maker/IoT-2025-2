# -*- coding: utf-8 -*-
"""
API test script for the SmartCrop IoT Monitor.
"""

import requests

def test_api():
    """
    Sends a test request to the API.
    """
    try:
        response = requests.get("http://localhost:5000/")
        print(f"API Response: {response.json()}")
    except requests.exceptions.ConnectionError as e:
        print(f"Error connecting to API: {e}")

if __name__ == "__main__":
    test_api()
