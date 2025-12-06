# API & JSON Best Practices for Senior Developers

## 1. Error Handling

### Always Handle Exceptions
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    # Handle timeout
except requests.exceptions.HTTPError as e:
    # Handle HTTP errors (4xx, 5xx)
except requests.exceptions.RequestException as e:
    # Handle other request errors
except json.JSONDecodeError:
    # Handle JSON parsing errors
```

### Use Specific Exception Types
- `Timeout` - Request took too long
- `ConnectionError` - Network problem
- `HTTPError` - Bad HTTP status code
- `TooManyRedirects` - Redirect loop
- `RequestException` - Base class for all

## 2. Timeouts

### Always Set Timeouts
```python
# Good
response = requests.get(url, timeout=10)

# Bad - can hang forever
response = requests.get(url)
```

### Use Tuple for Connect/Read Timeouts
```python
# (connect timeout, read timeout)
response = requests.get(url, timeout=(3, 10))
```

## 3. Session Management

### Use Sessions for Multiple Requests
```python
# Good - reuses connection
with requests.Session() as session:
    session.headers.update({'User-Agent': 'MyApp/1.0'})
    response1 = session.get(url1)
    response2 = session.get(url2)

# Bad - creates new connection each time
response1 = requests.get(url1)
response2 = requests.get(url2)
```

## 4. Type Hints

### Use Type Hints for Better Code Quality
```python
from typing import Dict, Any, Optional, List

def fetch_user(user_id: int) -> Optional[Dict[str, Any]]:
    """Fetch user by ID"""
    response = requests.get(f"/users/{user_id}")
    return response.json() if response.ok else None
```

## 5. Logging

### Log Important Events
```python
import logging

logger = logging.getLogger(__name__)

try:
    response = requests.get(url)
    logger.info(f"API call successful: {url}")
except RequestException as e:
    logger.error(f"API call failed: {url} - {e}")
```

## 6. Safe JSON Parsing

### Use .get() for Optional Fields
```python
# Good
name = user.get('name', 'Unknown')
city = user.get('address', {}).get('city', 'N/A')

# Bad - can raise KeyError
name = user['name']
city = user['address']['city']
```

### Validate Data Structure
```python
def validate_response(data: Dict) -> bool:
    required_fields = ['id', 'name', 'email']
    return all(field in data for field in required_fields)
```

## 7. Rate Limiting

### Respect API Rate Limits
```python
import time

class RateLimiter:
    def __init__(self, calls_per_second: int):
        self.calls_per_second = calls_per_second
        self.last_call = 0
    
    def wait_if_needed(self):
        elapsed = time.time() - self.last_call
        if elapsed < 1.0 / self.calls_per_second:
            time.sleep(1.0 / self.calls_per_second - elapsed)
        self.last_call = time.time()
```

## 8. Retry Logic

### Implement Exponential Backoff
```python
import time

max_retries = 3
backoff_factor = 2

for attempt in range(max_retries):
    try:
        response = requests.get(url)
        response.raise_for_status()
        break
    except RequestException:
        if attempt < max_retries - 1:
            wait_time = backoff_factor ** attempt
            time.sleep(wait_time)
```

## 9. Caching

### Cache Responses When Appropriate
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fetch_static_data(endpoint: str) -> Dict:
    response = requests.get(endpoint)
    return response.json()
```

## 10. Security

### Never Hardcode Credentials
```python
# Good
import os
api_key = os.environ.get('API_KEY')

# Bad
api_key = "sk_live_abc123..."
```

### Use HTTPS
```python
# Good
url = "https://api.example.com"

# Bad
url = "http://api.example.com"
```

## 11. Headers

### Set Appropriate Headers
```python
headers = {
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}
```

## 12. Data Validation

### Validate Before Processing
```python
def is_valid_email(email: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def process_user(data: Dict) -> None:
    if not is_valid_email(data.get('email', '')):
        raise ValueError("Invalid email")
    # Process...
```

## 13. Pagination

### Handle Paginated Responses
```python
def fetch_all_pages(url: str) -> List[Dict]:
    all_items = []
    page = 1
    
    while True:
        response = requests.get(url, params={'page': page})
        items = response.json()
        
        if not items:
            break
        
        all_items.extend(items)
        page += 1
    
    return all_items
```

## 14. Async for Performance

### Use Async for Concurrent Requests
```python
import asyncio
import aiohttp

async def fetch_async(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```

## 15. Testing

### Write Tests for API Interactions
```python
import unittest
from unittest.mock import patch, Mock

class TestAPI(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_user(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'id': 1, 'name': 'John'}
        mock_response.ok = True
        mock_get.return_value = mock_response
        
        result = fetch_user(1)
        self.assertEqual(result['name'], 'John')
```

## Key Takeaways for Interviews

1. **Always use timeouts** - Prevent hanging requests
2. **Handle all exceptions** - Network is unreliable
3. **Use type hints** - Better code quality
4. **Log important events** - Debugging and monitoring
5. **Validate data** - Don't trust external data
6. **Use sessions** - Better performance
7. **Implement retries** - Handle transient failures
8. **Cache when possible** - Reduce API calls
9. **Never hardcode secrets** - Security first
10. **Test your code** - Mock external dependencies

## Common Interview Questions

1. How do you handle rate limiting?
2. What's the difference between GET and POST?
3. How do you handle authentication?
4. How do you parse deeply nested JSON?
5. How do you handle pagination?
6. What's your error handling strategy?
7. How do you make concurrent API calls?
8. How do you cache API responses?
9. How do you handle API versioning?
10. How do you test code that makes API calls?
