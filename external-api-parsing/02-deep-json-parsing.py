"""
Deep JSON Parsing - Complex nested structures
Demonstrates parsing deeply nested JSON with various data types
"""

import requests
import json
from typing import Dict, Any, List, Optional


def parse_simple_json() -> None:
    """Parse simple flat JSON structure"""
    print("=" * 60)
    print("1. SIMPLE JSON PARSING")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        user = response.json()
        
        # Direct access
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Phone: {user['phone']}")
        
        # Safe access with .get()
        website = user.get('website', 'N/A')
        print(f"Website: {website}")
        
    except (requests.exceptions.RequestException, KeyError, json.JSONDecodeError) as e:
        print(f"Error: {e}")


def parse_nested_json() -> None:
    """Parse nested JSON objects"""
    print("\n" + "=" * 60)
    print("2. NESTED JSON PARSING")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        user = response.json()
        
        # Level 1: Direct fields
        print(f"User: {user['name']}")
        
        # Level 2: Nested object
        address = user['address']
        print(f"Street: {address['street']}")
        print(f"City: {address['city']}")
        print(f"Zipcode: {address['zipcode']}")
        
        # Level 3: Deeply nested
        geo = address['geo']
        print(f"Coordinates: ({geo['lat']}, {geo['lng']})")
        
        # Level 2: Another nested object
        company = user['company']
        print(f"Company: {company['name']}")
        print(f"Catchphrase: {company['catchPhrase']}")
        
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error: {e}")


def parse_array_of_objects() -> None:
    """Parse JSON arrays containing objects"""
    print("\n" + "=" * 60)
    print("3. ARRAY OF OBJECTS PARSING")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts?userId=1&_limit=3"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        posts = response.json()
        
        print(f"Total posts: {len(posts)}\n")
        
        for idx, post in enumerate(posts, 1):
            print(f"Post {idx}:")
            print(f"  ID: {post['id']}")
            print(f"  Title: {post['title']}")
            print(f"  Body: {post['body'][:50]}...")
            print()
            
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error: {e}")


def parse_complex_nested_structure() -> None:
    """Parse complex nested structures with arrays and objects"""
    print("\n" + "=" * 60)
    print("4. COMPLEX NESTED STRUCTURE")
    print("=" * 60)
    
    # Get user and their posts
    user_url = "https://jsonplaceholder.typicode.com/users/1"
    posts_url = "https://jsonplaceholder.typicode.com/posts?userId=1&_limit=2"
    
    try:
        # Fetch user
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user = user_response.json()
        
        # Fetch posts
        posts_response = requests.get(posts_url)
        posts_response.raise_for_status()
        posts = posts_response.json()
        
        # Create complex structure
        complex_data = {
            "user": user,
            "posts": posts,
            "metadata": {
                "total_posts": len(posts),
                "location": {
                    "city": user['address']['city'],
                    "coordinates": user['address']['geo']
                }
            }
        }
        
        # Parse deeply
        print(f"User: {complex_data['user']['name']}")
        print(f"Company: {complex_data['user']['company']['name']}")
        print(f"Location: {complex_data['metadata']['location']['city']}")
        print(f"Lat: {complex_data['metadata']['location']['coordinates']['lat']}")
        print(f"Lng: {complex_data['metadata']['location']['coordinates']['lng']}")
        print(f"\nPosts by {complex_data['user']['name']}:")
        
        for post in complex_data['posts']:
            print(f"  - {post['title']}")
            
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error: {e}")


def safe_nested_access() -> None:
    """Demonstrate safe access to deeply nested JSON"""
    print("\n" + "=" * 60)
    print("5. SAFE NESTED ACCESS")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        user = response.json()
        
        # Method 1: Try-except
        try:
            lat = user['address']['geo']['lat']
            print(f"Method 1 (try-except): Latitude = {lat}")
        except KeyError:
            print("Method 1: Key not found")
        
        # Method 2: Chained .get()
        lat = user.get('address', {}).get('geo', {}).get('lat', 'N/A')
        print(f"Method 2 (chained .get): Latitude = {lat}")
        
        # Method 3: Helper function
        def safe_get(data: Dict, *keys: str, default: Any = None) -> Any:
            """Safely get nested value from dictionary"""
            for key in keys:
                if isinstance(data, dict):
                    data = data.get(key, {})
                else:
                    return default
            return data if data != {} else default
        
        lat = safe_get(user, 'address', 'geo', 'lat', default='Unknown')
        print(f"Method 3 (helper function): Latitude = {lat}")
        
        # Test with non-existent path
        missing = safe_get(user, 'address', 'country', 'code', default='N/A')
        print(f"Non-existent path: {missing}")
        
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error: {e}")


def filter_and_transform_json() -> None:
    """Filter and transform JSON data"""
    print("\n" + "=" * 60)
    print("6. FILTER AND TRANSFORM JSON")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        users = response.json()
        
        # Extract specific fields
        user_summaries = [
            {
                "name": user['name'],
                "email": user['email'],
                "city": user['address']['city'],
                "company": user['company']['name']
            }
            for user in users
        ]
        
        print("User Summaries:")
        for summary in user_summaries[:3]:  # Show first 3
            print(json.dumps(summary, indent=2))
            print()
        
        # Filter users by city
        city_filter = "Gwenborough"
        filtered_users = [
            user for user in users 
            if user['address']['city'] == city_filter
        ]
        
        print(f"Users in {city_filter}:")
        for user in filtered_users:
            print(f"  - {user['name']}")
        
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error: {e}")


def parse_json_with_arrays() -> None:
    """Parse JSON with mixed arrays and objects"""
    print("\n" + "=" * 60)
    print("7. MIXED ARRAYS AND OBJECTS")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts/1/comments"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        comments = response.json()
        
        print(f"Total comments: {len(comments)}\n")
        
        # Group by email domain
        domains = {}
        for comment in comments:
            email = comment['email']
            domain = email.split('@')[1]
            
            if domain not in domains:
                domains[domain] = []
            
            domains[domain].append({
                "name": comment['name'],
                "email": email
            })
        
        print("Comments grouped by domain:")
        for domain, users in domains.items():
            print(f"\n{domain}: {len(users)} comment(s)")
            for user in users[:2]:  # Show first 2
                print(f"  - {user['name']} ({user['email']})")
        
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    parse_simple_json()
    parse_nested_json()
    parse_array_of_objects()
    parse_complex_nested_structure()
    safe_nested_access()
    filter_and_transform_json()
    parse_json_with_arrays()
    
    print("\n" + "=" * 60)
    print("COMPLETED: Deep JSON Parsing")
    print("=" * 60)
