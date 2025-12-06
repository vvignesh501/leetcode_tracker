"""
Interview Questions & Answers
Common senior developer interview scenarios for API/JSON handling
"""

import requests
import json
from typing import Dict, Any, List, Optional, Set
from collections import defaultdict
import time


def question_1_rate_limiting() -> None:
    """
    Q: How would you implement rate limiting for API calls?
    A: Use token bucket or sliding window algorithm
    """
    print("=" * 60)
    print("Q1: RATE LIMITING")
    print("=" * 60)
    
    class RateLimiter:
        """Simple rate limiter using token bucket algorithm"""
        
        def __init__(self, max_calls: int, time_window: int):
            self.max_calls = max_calls
            self.time_window = time_window
            self.calls = []
        
        def can_make_call(self) -> bool:
            """Check if we can make another API call"""
            now = time.time()
            
            # Remove old calls outside time window
            self.calls = [
                call_time for call_time in self.calls
                if now - call_time < self.time_window
            ]
            
            # Check if under limit
            if len(self.calls) < self.max_calls:
                self.calls.append(now)
                return True
            
            return False
        
        def wait_time(self) -> float:
            """Calculate wait time until next call is allowed"""
            if len(self.calls) < self.max_calls:
                return 0.0
            
            oldest_call = min(self.calls)
            return self.time_window - (time.time() - oldest_call)
    
    # Demo
    limiter = RateLimiter(max_calls=3, time_window=5)
    
    print("\nRate Limiter Demo (3 calls per 5 seconds):")
    for i in range(5):
        if limiter.can_make_call():
            print(f"  Call {i+1}: ✓ Allowed")
        else:
            wait = limiter.wait_time()
            print(f"  Call {i+1}: ✗ Rate limited (wait {wait:.1f}s)")


def question_2_caching() -> None:
    """
    Q: How would you implement caching for API responses?
    A: Use TTL-based cache with LRU eviction
    """
    print("\n" + "=" * 60)
    print("Q2: RESPONSE CACHING")
    print("=" * 60)
    
    from functools import lru_cache
    from datetime import datetime, timedelta
    
    class APICache:
        """Simple cache with TTL"""
        
        def __init__(self, ttl_seconds: int = 300):
            self.cache: Dict[str, tuple[Any, datetime]] = {}
            self.ttl = timedelta(seconds=ttl_seconds)
        
        def get(self, key: str) -> Optional[Any]:
            """Get cached value if not expired"""
            if key in self.cache:
                value, timestamp = self.cache[key]
                if datetime.now() - timestamp < self.ttl:
                    return value
                else:
                    del self.cache[key]
            return None
        
        def set(self, key: str, value: Any) -> None:
            """Cache a value with current timestamp"""
            self.cache[key] = (value, datetime.now())
        
        def clear(self) -> None:
            """Clear all cached values"""
            self.cache.clear()
    
    # Demo
    cache = APICache(ttl_seconds=60)
    
    print("\nCache Demo:")
    cache.set("user:1", {"name": "John", "email": "john@example.com"})
    
    result = cache.get("user:1")
    print(f"  First fetch: {result}")
    
    result = cache.get("user:1")
    print(f"  Second fetch (cached): {result}")
    
    result = cache.get("user:999")
    print(f"  Non-existent key: {result}")


def question_3_pagination() -> None:
    """
    Q: How do you handle paginated API responses?
    A: Implement iterator pattern with automatic page fetching
    """
    print("\n" + "=" * 60)
    print("Q3: PAGINATION HANDLING")
    print("=" * 60)
    
    def fetch_all_pages(base_url: str, params: Dict = None) -> List[Dict]:
        """Fetch all pages from paginated API"""
        all_items = []
        page = 1
        
        while True:
            current_params = params.copy() if params else {}
            current_params['_page'] = page
            current_params['_limit'] = 10
            
            try:
                response = requests.get(base_url, params=current_params, timeout=10)
                response.raise_for_status()
                
                items = response.json()
                
                if not items:  # No more pages
                    break
                
                all_items.extend(items)
                page += 1
                
                # Safety limit
                if page > 5:
                    break
                    
            except requests.exceptions.RequestException:
                break
        
        return all_items
    
    # Demo
    print("\nFetching paginated data:")
    url = "https://jsonplaceholder.typicode.com/posts"
    posts = fetch_all_pages(url, {"userId": 1})
    print(f"  Total items fetched: {len(posts)}")


def question_4_error_recovery() -> None:
    """
    Q: How do you handle partial failures in batch API calls?
    A: Implement circuit breaker pattern and collect errors
    """
    print("\n" + "=" * 60)
    print("Q4: ERROR RECOVERY IN BATCH OPERATIONS")
    print("=" * 60)
    
    def batch_fetch_with_recovery(ids: List[int]) -> Dict[str, Any]:
        """Fetch multiple resources, continue on individual failures"""
        results = {
            "success": [],
            "failed": [],
            "errors": []
        }
        
        base_url = "https://jsonplaceholder.typicode.com/posts"
        
        for post_id in ids:
            try:
                response = requests.get(f"{base_url}/{post_id}", timeout=5)
                response.raise_for_status()
                
                data = response.json()
                results["success"].append(data)
                
            except requests.exceptions.RequestException as e:
                results["failed"].append(post_id)
                results["errors"].append(str(e))
        
        return results
    
    # Demo
    print("\nBatch fetch with error recovery:")
    ids = [1, 2, 999999, 3]  # 999999 will fail
    results = batch_fetch_with_recovery(ids)
    
    print(f"  Successful: {len(results['success'])}")
    print(f"  Failed: {len(results['failed'])}")
    if results['failed']:
        print(f"  Failed IDs: {results['failed']}")


def question_5_json_schema_validation() -> None:
    """
    Q: How do you validate JSON structure before processing?
    A: Use schema validation with type checking
    """
    print("\n" + "=" * 60)
    print("Q5: JSON SCHEMA VALIDATION")
    print("=" * 60)
    
    def validate_user_schema(data: Dict) -> tuple[bool, List[str]]:
        """Validate user data against expected schema"""
        errors = []
        
        # Required fields
        required = ['id', 'name', 'email', 'address']
        for field in required:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        # Type validation
        if 'id' in data and not isinstance(data['id'], int):
            errors.append("Field 'id' must be integer")
        
        if 'name' in data and not isinstance(data['name'], str):
            errors.append("Field 'name' must be string")
        
        if 'email' in data and not isinstance(data['email'], str):
            errors.append("Field 'email' must be string")
        
        # Nested validation
        if 'address' in data:
            if not isinstance(data['address'], dict):
                errors.append("Field 'address' must be object")
            else:
                address_required = ['street', 'city']
                for field in address_required:
                    if field not in data['address']:
                        errors.append(f"Missing address.{field}")
        
        return len(errors) == 0, errors
    
    # Demo
    print("\nValidation Demo:")
    
    valid_user = {
        "id": 1,
        "name": "John",
        "email": "john@example.com",
        "address": {"street": "Main St", "city": "NYC"}
    }
    
    invalid_user = {
        "id": "1",  # Wrong type
        "name": "John",
        # Missing email
        "address": {"street": "Main St"}  # Missing city
    }
    
    is_valid, errors = validate_user_schema(valid_user)
    print(f"  Valid user: {is_valid}")
    
    is_valid, errors = validate_user_schema(invalid_user)
    print(f"  Invalid user: {is_valid}")
    if errors:
        for error in errors:
            print(f"    - {error}")


def question_6_data_transformation() -> None:
    """
    Q: How do you transform nested API responses into flat structures?
    A: Use recursive flattening or mapping functions
    """
    print("\n" + "=" * 60)
    print("Q6: DATA TRANSFORMATION")
    print("=" * 60)
    
    def flatten_dict(data: Dict, parent_key: str = '', sep: str = '.') -> Dict:
        """Flatten nested dictionary"""
        items = []
        
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            
            if isinstance(value, dict):
                items.extend(flatten_dict(value, new_key, sep=sep).items())
            elif isinstance(value, list):
                items.append((new_key, value))
            else:
                items.append((new_key, value))
        
        return dict(items)
    
    # Demo
    print("\nFlattening nested structure:")
    
    nested = {
        "user": {
            "name": "John",
            "address": {
                "city": "NYC",
                "geo": {
                    "lat": 40.7128,
                    "lng": -74.0060
                }
            }
        }
    }
    
    flat = flatten_dict(nested)
    print("\nOriginal:")
    print(json.dumps(nested, indent=2))
    print("\nFlattened:")
    for key, value in flat.items():
        print(f"  {key}: {value}")


def question_7_concurrent_requests() -> None:
    """
    Q: How do you make multiple API calls concurrently?
    A: Use threading or async/await for parallel requests
    """
    print("\n" + "=" * 60)
    print("Q7: CONCURRENT API REQUESTS")
    print("=" * 60)
    
    from concurrent.futures import ThreadPoolExecutor, as_completed
    
    def fetch_post(post_id: int) -> Optional[Dict]:
        """Fetch single post"""
        try:
            response = requests.get(
                f"https://jsonplaceholder.typicode.com/posts/{post_id}",
                timeout=5
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None
    
    def fetch_posts_concurrent(post_ids: List[int]) -> List[Dict]:
        """Fetch multiple posts concurrently"""
        results = []
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_id = {
                executor.submit(fetch_post, post_id): post_id
                for post_id in post_ids
            }
            
            for future in as_completed(future_to_id):
                result = future.result()
                if result:
                    results.append(result)
        
        return results
    
    # Demo
    print("\nFetching 5 posts concurrently:")
    start = time.time()
    posts = fetch_posts_concurrent([1, 2, 3, 4, 5])
    elapsed = time.time() - start
    
    print(f"  Fetched {len(posts)} posts in {elapsed:.2f}s")


def question_8_api_versioning() -> None:
    """
    Q: How do you handle API versioning?
    A: Use version in URL or headers, with fallback logic
    """
    print("\n" + "=" * 60)
    print("Q8: API VERSIONING")
    print("=" * 60)
    
    class VersionedAPIClient:
        """API client with version support"""
        
        def __init__(self, base_url: str, version: str = "v1"):
            self.base_url = base_url
            self.version = version
        
        def get(self, endpoint: str) -> Optional[Dict]:
            """Make versioned GET request"""
            url = f"{self.base_url}/{self.version}/{endpoint}"
            
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException:
                return None
    
    print("\nVersioned API client demo:")
    print("  Supports multiple API versions")
    print("  URL pattern: /api/v1/resource or /api/v2/resource")
    print("  Can fallback to older versions if needed")


if __name__ == "__main__":
    question_1_rate_limiting()
    question_2_caching()
    question_3_pagination()
    question_4_error_recovery()
    question_5_json_schema_validation()
    question_6_data_transformation()
    question_7_concurrent_requests()
    question_8_api_versioning()
    
    print("\n" + "=" * 60)
    print("COMPLETED: Interview Questions")
    print("=" * 60)
