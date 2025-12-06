"""
Basic API Calls - GET, POST, PUT, DELETE
Demonstrates fundamental HTTP methods and response handling
"""

import requests
import json
from typing import Dict, Any, Optional


def get_request_basic() -> None:
    """Basic GET request example"""
    print("=" * 60)
    print("1. BASIC GET REQUEST")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url)
        
        # Check status code
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}\n")
        
        # Convert to JSON
        data = response.json()
        print(f"Response Data:\n{json.dumps(data, indent=2)}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def get_request_with_params() -> None:
    """GET request with query parameters"""
    print("\n" + "=" * 60)
    print("2. GET REQUEST WITH PARAMETERS")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {
        "userId": 1,
        "_limit": 3
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad status
        
        data = response.json()
        print(f"Retrieved {len(data)} posts:")
        for post in data:
            print(f"  - Post {post['id']}: {post['title'][:50]}...")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def post_request() -> None:
    """POST request to create new resource"""
    print("\n" + "=" * 60)
    print("3. POST REQUEST")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Data to send
    payload = {
        "title": "Senior Developer Interview",
        "body": "Practicing API calls and JSON parsing",
        "userId": 1
    }
    
    # Headers
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        created_data = response.json()
        print(f"Created Resource:")
        print(json.dumps(created_data, indent=2))
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def put_request() -> None:
    """PUT request to update resource"""
    print("\n" + "=" * 60)
    print("4. PUT REQUEST")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated body content",
        "userId": 1
    }
    
    try:
        response = requests.put(url, json=payload)
        response.raise_for_status()
        
        updated_data = response.json()
        print(f"Updated Resource:")
        print(json.dumps(updated_data, indent=2))
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def delete_request() -> None:
    """DELETE request to remove resource"""
    print("\n" + "=" * 60)
    print("5. DELETE REQUEST")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.delete(url)
        response.raise_for_status()
        
        print(f"Status Code: {response.status_code}")
        print("Resource deleted successfully")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def response_inspection() -> None:
    """Inspect all aspects of HTTP response"""
    print("\n" + "=" * 60)
    print("6. RESPONSE INSPECTION")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url)
        
        print(f"URL: {response.url}")
        print(f"Status Code: {response.status_code}")
        print(f"Reason: {response.reason}")
        print(f"Encoding: {response.encoding}")
        print(f"Response Time: {response.elapsed.total_seconds()}s")
        print(f"\nContent-Type: {response.headers.get('Content-Type')}")
        print(f"Content-Length: {response.headers.get('Content-Length')}")
        
        # Raw text
        print(f"\nRaw Text (first 100 chars):\n{response.text[:100]}...")
        
        # JSON
        print(f"\nParsed JSON:")
        print(json.dumps(response.json(), indent=2))
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_request_basic()
    get_request_with_params()
    post_request()
    put_request()
    delete_request()
    response_inspection()
    
    print("\n" + "=" * 60)
    print("COMPLETED: Basic API Calls")
    print("=" * 60)
