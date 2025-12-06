"""
Real-world Examples - Multiple API integrations
Demonstrates practical scenarios with different public APIs
"""

import requests
import json
from typing import Dict, Any, List, Optional
from datetime import datetime


def github_api_example() -> None:
    """
    GitHub API - Get repository information
    Demonstrates: Headers, authentication, nested JSON
    """
    print("=" * 60)
    print("1. GITHUB API - Repository Info")
    print("=" * 60)
    
    url = "https://api.github.com/repos/python/cpython"
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Python-API-Practice"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        repo = response.json()
        
        # Parse nested data
        print(f"\nRepository: {repo['full_name']}")
        print(f"Description: {repo['description']}")
        print(f"Stars: {repo['stargazers_count']:,}")
        print(f"Forks: {repo['forks_count']:,}")
        print(f"Language: {repo['language']}")
        print(f"Created: {repo['created_at']}")
        print(f"Last Updated: {repo['updated_at']}")
        
        # Owner information (nested object)
        owner = repo['owner']
        print(f"\nOwner: {owner['login']}")
        print(f"Type: {owner['type']}")
        
        # License information (nested object, may be None)
        license_info = repo.get('license')
        if license_info:
            print(f"\nLicense: {license_info['name']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def rest_countries_api() -> None:
    """
    REST Countries API - Get country information
    Demonstrates: Complex nested arrays and objects
    """
    print("\n" + "=" * 60)
    print("2. REST COUNTRIES API - Country Info")
    print("=" * 60)
    
    url = "https://restcountries.com/v3.1/name/canada"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        countries = response.json()
        country = countries[0]  # Get first result
        
        # Basic info
        print(f"\nCountry: {country['name']['common']}")
        print(f"Official Name: {country['name']['official']}")
        print(f"Capital: {country['capital'][0]}")
        print(f"Region: {country['region']}")
        print(f"Subregion: {country['subregion']}")
        print(f"Population: {country['population']:,}")
        
        # Languages (nested object)
        languages = country.get('languages', {})
        print(f"\nLanguages: {', '.join(languages.values())}")
        
        # Currencies (nested object with dynamic keys)
        currencies = country.get('currencies', {})
        print("\nCurrencies:")
        for code, info in currencies.items():
            print(f"  {code}: {info['name']} ({info['symbol']})")
        
        # Borders (array)
        borders = country.get('borders', [])
        if borders:
            print(f"\nBorders: {', '.join(borders)}")
        
        # Coordinates (nested in multiple levels)
        latlng = country.get('latlng', [])
        if latlng:
            print(f"\nCoordinates: {latlng[0]}, {latlng[1]}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except (KeyError, IndexError) as e:
        print(f"Parsing Error: {e}")


def jsonplaceholder_complex() -> None:
    """
    JSONPlaceholder - Complex multi-endpoint example
    Demonstrates: Multiple API calls, data aggregation
    """
    print("\n" + "=" * 60)
    print("3. JSONPLACEHOLDER - User Dashboard")
    print("=" * 60)
    
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = 1
    
    try:
        # Fetch user
        user_response = requests.get(f"{base_url}/users/{user_id}", timeout=10)
        user_response.raise_for_status()
        user = user_response.json()
        
        # Fetch user's posts
        posts_response = requests.get(
            f"{base_url}/posts",
            params={"userId": user_id, "_limit": 3},
            timeout=10
        )
        posts_response.raise_for_status()
        posts = posts_response.json()
        
        # Fetch user's albums
        albums_response = requests.get(
            f"{base_url}/albums",
            params={"userId": user_id, "_limit": 2},
            timeout=10
        )
        albums_response.raise_for_status()
        albums = albums_response.json()
        
        # Fetch user's todos
        todos_response = requests.get(
            f"{base_url}/todos",
            params={"userId": user_id, "_limit": 5},
            timeout=10
        )
        todos_response.raise_for_status()
        todos = todos_response.json()
        
        # Aggregate data
        print(f"\n{'='*40}")
        print(f"USER DASHBOARD")
        print(f"{'='*40}")
        
        # User info (deeply nested)
        print(f"\nUser: {user['name']} (@{user['username']})")
        print(f"Email: {user['email']}")
        print(f"Phone: {user['phone']}")
        print(f"Website: {user['website']}")
        
        # Address (nested object)
        address = user['address']
        print(f"\nAddress:")
        print(f"  {address['street']}, {address['suite']}")
        print(f"  {address['city']}, {address['zipcode']}")
        print(f"  Coordinates: ({address['geo']['lat']}, {address['geo']['lng']})")
        
        # Company (nested object)
        company = user['company']
        print(f"\nCompany: {company['name']}")
        print(f"  {company['catchPhrase']}")
        print(f"  {company['bs']}")
        
        # Posts
        print(f"\nRecent Posts ({len(posts)}):")
        for post in posts:
            print(f"  • {post['title'][:50]}...")
        
        # Albums
        print(f"\nAlbums ({len(albums)}):")
        for album in albums:
            print(f"  • {album['title']}")
        
        # Todos
        completed = sum(1 for todo in todos if todo['completed'])
        print(f"\nTodos: {completed}/{len(todos)} completed")
        for todo in todos:
            status = "✓" if todo['completed'] else "○"
            print(f"  {status} {todo['title'][:50]}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Parsing Error: Missing key {e}")


def open_meteo_weather() -> None:
    """
    Open-Meteo API - Weather data
    Demonstrates: Query parameters, time series data
    """
    print("\n" + "=" * 60)
    print("4. OPEN-METEO API - Weather Forecast")
    print("=" * 60)
    
    # New York coordinates
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,precipitation_probability",
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "America/New_York",
        "forecast_days": 3
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Current weather
        current = data['current']
        print(f"\nCurrent Weather (New York):")
        print(f"  Temperature: {current['temperature_2m']}°C")
        print(f"  Wind Speed: {current['wind_speed_10m']} km/h")
        print(f"  Time: {current['time']}")
        
        # Daily forecast (arrays)
        daily = data['daily']
        print(f"\n3-Day Forecast:")
        for i in range(len(daily['time'])):
            date = daily['time'][i]
            temp_max = daily['temperature_2m_max'][i]
            temp_min = daily['temperature_2m_min'][i]
            print(f"  {date}: {temp_min}°C - {temp_max}°C")
        
        # Hourly data (first 6 hours)
        hourly = data['hourly']
        print(f"\nHourly Forecast (next 6 hours):")
        for i in range(min(6, len(hourly['time']))):
            time = hourly['time'][i]
            temp = hourly['temperature_2m'][i]
            precip = hourly['precipitation_probability'][i]
            print(f"  {time}: {temp}°C, {precip}% rain")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Parsing Error: Missing key {e}")


def cat_facts_api() -> None:
    """
    Cat Facts API - Simple random data
    Demonstrates: Simple API, array handling
    """
    print("\n" + "=" * 60)
    print("5. CAT FACTS API - Random Facts")
    print("=" * 60)
    
    url = "https://catfact.ninja/facts"
    params = {"limit": 5}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Pagination info
        print(f"\nTotal Facts Available: {data['total']}")
        print(f"Showing: {data['per_page']} per page")
        print(f"Current Page: {data['current_page']}")
        
        # Facts array
        facts = data['data']
        print(f"\nRandom Cat Facts:")
        for i, fact in enumerate(facts, 1):
            print(f"\n{i}. {fact['fact']}")
            print(f"   (Length: {fact['length']} characters)")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Parsing Error: Missing key {e}")


def data_aggregation_example() -> None:
    """
    Aggregate data from multiple API calls
    Demonstrates: Data combination, transformation
    """
    print("\n" + "=" * 60)
    print("6. DATA AGGREGATION - Multiple Sources")
    print("=" * 60)
    
    try:
        # Get multiple users
        users_response = requests.get(
            "https://jsonplaceholder.typicode.com/users",
            params={"_limit": 3},
            timeout=10
        )
        users_response.raise_for_status()
        users = users_response.json()
        
        # Aggregate data for each user
        user_stats = []
        
        for user in users:
            # Get posts count
            posts_response = requests.get(
                "https://jsonplaceholder.typicode.com/posts",
                params={"userId": user['id']},
                timeout=10
            )
            posts_count = len(posts_response.json()) if posts_response.ok else 0
            
            # Get todos count
            todos_response = requests.get(
                "https://jsonplaceholder.typicode.com/todos",
                params={"userId": user['id']},
                timeout=10
            )
            todos = todos_response.json() if todos_response.ok else []
            todos_completed = sum(1 for todo in todos if todo.get('completed', False))
            
            # Aggregate
            user_stats.append({
                "name": user['name'],
                "email": user['email'],
                "city": user['address']['city'],
                "company": user['company']['name'],
                "posts": posts_count,
                "todos_total": len(todos),
                "todos_completed": todos_completed,
                "completion_rate": (
                    f"{(todos_completed/len(todos)*100):.1f}%"
                    if len(todos) > 0 else "N/A"
                )
            })
        
        # Display aggregated data
        print("\nUser Activity Summary:")
        print(f"{'='*80}")
        
        for stats in user_stats:
            print(f"\n{stats['name']} ({stats['email']})")
            print(f"  Location: {stats['city']}")
            print(f"  Company: {stats['company']}")
            print(f"  Posts: {stats['posts']}")
            print(f"  Todos: {stats['todos_completed']}/{stats['todos_total']} "
                  f"({stats['completion_rate']})")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Parsing Error: Missing key {e}")


if __name__ == "__main__":
    github_api_example()
    rest_countries_api()
    jsonplaceholder_complex()
    open_meteo_weather()
    cat_facts_api()
    data_aggregation_example()
    
    print("\n" + "=" * 60)
    print("COMPLETED: Real-world Examples")
    print("=" * 60)
