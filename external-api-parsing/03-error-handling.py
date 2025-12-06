"""
Error Handling - Comprehensive error handling patterns
Demonstrates production-ready error handling for API calls
"""

import requests
import json
from typing import Dict, Any, Optional, Union
from requests.exceptions import (
    RequestException,
    HTTPError,
    ConnectionError,
    Timeout,
    TooManyRedirects
)


def handle_http_errors() -> None:
    """Handle different HTTP status codes"""
    print("=" * 60)
    print("1. HTTP ERROR HANDLING")
    print("=" * 60)
    
    # Test different status codes
    test_urls = [
        ("https://jsonplaceholder.typicode.com/posts/1", "Valid"),
        ("https://jsonplaceholder.typicode.com/posts/999999", "Not Found"),
    ]
    
    for url, description in test_urls:
        print(f"\nTesting: {description}")
        try:
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print(f"✓ Success: {response.status_code}")
                data = response.json()
                print(f"  Data: {data.get('title', 'N/A')[:50]}")
            elif response.status_code == 404:
                print(f"✗ Not Found: {response.status_code}")
            elif response.status_code >= 500:
                print(f"✗ Server Error: {response.status_code}")
            else:
                print(f"? Unexpected: {response.status_code}")
                
        except HTTPError as e:
            print(f"✗ HTTP Error: {e}")
        except RequestException as e:
            print(f"✗ Request Error: {e}")


def handle_network_errors() -> None:
    """Handle network-related errors"""
    print("\n" + "=" * 60)
    print("2. NETWORK ERROR HANDLING")
    print("=" * 60)
    
    # Test timeout
    print("\nTesting timeout:")
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=0.001  # Very short timeout
        )
        print("✓ Request completed")
    except Timeout:
        print("✗ Timeout: Request took too long")
    except RequestException as e:
        print(f"✗ Error: {e}")
    
    # Test connection error
    print("\nTesting invalid domain:")
    try:
        response = requests.get(
            "https://this-domain-does-not-exist-12345.com",
            timeout=5
        )
        print("✓ Request completed")
    except ConnectionError:
        print("✗ Connection Error: Cannot reach server")
    except RequestException as e:
        print(f"✗ Error: {e}")


def handle_json_errors() -> None:
    """Handle JSON parsing errors"""
    print("\n" + "=" * 60)
    print("3. JSON PARSING ERROR HANDLING")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        # Try to parse JSON
        try:
            data = response.json()
            print("✓ JSON parsed successfully")
            print(f"  Keys: {list(data.keys())}")
        except json.JSONDecodeError as e:
            print(f"✗ JSON Decode Error: {e}")
            print(f"  Raw content: {response.text[:100]}")
            
    except RequestException as e:
        print(f"✗ Request Error: {e}")


def safe_api_call(
    url: str,
    method: str = "GET",
    **kwargs
) -> Optional[Dict[str, Any]]:
    """
    Safe API call wrapper with comprehensive error handling
    
    Args:
        url: API endpoint URL
        method: HTTP method (GET, POST, PUT, DELETE)
        **kwargs: Additional arguments for requests
    
    Returns:
        Parsed JSON response or None if error
    """
    try:
        # Set default timeout if not provided
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 10
        
        # Make request
        response = requests.request(method, url, **kwargs)
        
        # Check status
        response.raise_for_status()
        
        # Parse JSON
        return response.json()
        
    except Timeout:
        print(f"✗ Timeout: Request to {url} took too long")
        return None
    except ConnectionError:
        print(f"✗ Connection Error: Cannot reach {url}")
        return None
    except HTTPError as e:
        print(f"✗ HTTP Error {e.response.status_code}: {e}")
        return None
    except json.JSONDecodeError:
        print(f"✗ JSON Error: Invalid JSON response")
        return None
    except RequestException as e:
        print(f"✗ Request Error: {e}")
        return None


def demonstrate_safe_wrapper() -> None:
    """Demonstrate the safe API call wrapper"""
    print("\n" + "=" * 60)
    print("4. SAFE API CALL WRAPPER")
    print("=" * 60)
    
    # Successful call
    print("\nTest 1: Valid endpoint")
    data = safe_api_call("https://jsonplaceholder.typicode.com/posts/1")
    if data:
        print(f"✓ Success: {data['title'][:50]}")
    
    # Not found
    print("\nTest 2: Not found")
    data = safe_api_call("https://jsonplaceholder.typicode.com/posts/999999")
    if data:
        print(f"✓ Success")
    else:
        print("  Handled gracefully")
    
    # Invalid domain
    print("\nTest 3: Invalid domain")
    data = safe_api_call("https://invalid-domain-12345.com")
    if data:
        print(f"✓ Success")
    else:
        print("  Handled gracefully")


def retry_with_backoff() -> None:
    """Implement retry logic with exponential backoff"""
    print("\n" + "=" * 60)
    print("5. RETRY WITH BACKOFF")
    print("=" * 60)
    
    import time
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    max_retries = 3
    backoff_factor = 2
    
    for attempt in range(max_retries):
        try:
            print(f"\nAttempt {attempt + 1}/{max_retries}")
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            print(f"✓ Success: {data['title'][:50]}")
            break
            
        except RequestException as e:
            print(f"✗ Failed: {e}")
            
            if attempt < max_retries - 1:
                wait_time = backoff_factor ** attempt
                print(f"  Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print("  Max retries reached")


def validate_response_data() -> None:
    """Validate response data structure"""
    print("\n" + "=" * 60)
    print("6. RESPONSE DATA VALIDATION")
    print("=" * 60)
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        
        # Validate required fields
        required_fields = ['userId', 'id', 'title', 'body']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            print(f"✗ Missing fields: {missing_fields}")
        else:
            print("✓ All required fields present")
        
        # Validate data types
        if not isinstance(data.get('id'), int):
            print("✗ Invalid type for 'id'")
        else:
            print("✓ Valid type for 'id'")
        
        if not isinstance(data.get('title'), str):
            print("✗ Invalid type for 'title'")
        else:
            print("✓ Valid type for 'title'")
        
        # Validate value ranges
        if data.get('userId', 0) <= 0:
            print("✗ Invalid userId value")
        else:
            print("✓ Valid userId value")
            
    except RequestException as e:
        print(f"✗ Request Error: {e}")


if __name__ == "__main__":
    handle_http_errors()
    handle_network_errors()
    handle_json_errors()
    demonstrate_safe_wrapper()
    retry_with_backoff()
    validate_response_data()
    
    print("\n" + "=" * 60)
    print("COMPLETED: Error Handling")
    print("=" * 60)
