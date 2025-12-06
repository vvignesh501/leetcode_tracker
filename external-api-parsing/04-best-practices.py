"""
Best Practices - Production-ready code patterns
Demonstrates senior developer best practices for API integration
"""

import requests
import json
from typing import Dict, Any, Optional, List, TypedDict
from dataclasses import dataclass
from enum import Enum
import logging
from datetime import datetime


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Type definitions
class HTTPMethod(Enum):
    """HTTP methods enum for type safety"""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


@dataclass
class APIConfig:
    """API configuration with sensible defaults"""
    base_url: str
    timeout: int = 10
    max_retries: int = 3
    headers: Optional[Dict[str, str]] = None
    
    def __post_init__(self):
        if self.headers is None:
            self.headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }


class Post(TypedDict):
    """Type definition for Post object"""
    userId: int
    id: int
    title: str
    body: str


class APIClient:
    """
    Production-ready API client with best practices:
    - Type hints
    - Error handling
    - Logging
    - Retry logic
    - Session management
    - Resource cleanup
    """
    
    def __init__(self, config: APIConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(config.headers or {})
        logger.info(f"Initialized API client for {config.base_url}")
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - cleanup resources"""
        self.close()
    
    def close(self) -> None:
        """Close session and cleanup resources"""
        self.session.close()
        logger.info("API client closed")
    
    def _make_request(
        self,
        method: HTTPMethod,
        endpoint: str,
        **kwargs
    ) -> Optional[requests.Response]:
        """
        Internal method to make HTTP requests with retry logic
        
        Args:
            method: HTTP method
            endpoint: API endpoint path
            **kwargs: Additional request parameters
        
        Returns:
            Response object or None if all retries failed
        """
        url = f"{self.config.base_url}/{endpoint.lstrip('/')}"
        
        for attempt in range(self.config.max_retries):
            try:
                logger.debug(f"Request: {method.value} {url} (attempt {attempt + 1})")
                
                response = self.session.request(
                    method.value,
                    url,
                    timeout=self.config.timeout,
                    **kwargs
                )
                
                response.raise_for_status()
                logger.info(f"Success: {method.value} {url} - {response.status_code}")
                return response
                
            except requests.exceptions.Timeout:
                logger.warning(f"Timeout on attempt {attempt + 1}")
                if attempt == self.config.max_retries - 1:
                    logger.error(f"Max retries reached for {url}")
                    return None
                    
            except requests.exceptions.HTTPError as e:
                logger.error(f"HTTP Error: {e.response.status_code} - {url}")
                return None
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {e}")
                if attempt == self.config.max_retries - 1:
                    return None
        
        return None
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
        """
        GET request
        
        Args:
            endpoint: API endpoint
            params: Query parameters
        
        Returns:
            Parsed JSON response or None
        """
        response = self._make_request(HTTPMethod.GET, endpoint, params=params)
        return response.json() if response else None
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        POST request
        
        Args:
            endpoint: API endpoint
            data: Request body data
        
        Returns:
            Parsed JSON response or None
        """
        response = self._make_request(HTTPMethod.POST, endpoint, json=data)
        return response.json() if response else None
    
    def put(self, endpoint: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        PUT request
        
        Args:
            endpoint: API endpoint
            data: Request body data
        
        Returns:
            Parsed JSON response or None
        """
        response = self._make_request(HTTPMethod.PUT, endpoint, json=data)
        return response.json() if response else None
    
    def delete(self, endpoint: str) -> bool:
        """
        DELETE request
        
        Args:
            endpoint: API endpoint
        
        Returns:
            True if successful, False otherwise
        """
        response = self._make_request(HTTPMethod.DELETE, endpoint)
        return response is not None


def demonstrate_api_client() -> None:
    """Demonstrate the production-ready API client"""
    print("=" * 60)
    print("PRODUCTION-READY API CLIENT")
    print("=" * 60)
    
    # Configure API
    config = APIConfig(
        base_url="https://jsonplaceholder.typicode.com",
        timeout=10,
        max_retries=3
    )
    
    # Use context manager for automatic cleanup
    with APIClient(config) as client:
        # GET request
        print("\n1. GET Request:")
        post = client.get("posts/1")
        if post:
            print(f"   Title: {post['title']}")
        
        # GET with parameters
        print("\n2. GET with Parameters:")
        posts = client.get("posts", params={"userId": 1, "_limit": 3})
        if posts:
            print(f"   Retrieved {len(posts)} posts")
        
        # POST request
        print("\n3. POST Request:")
        new_post = {
            "title": "Senior Dev Interview",
            "body": "Best practices demonstration",
            "userId": 1
        }
        created = client.post("posts", new_post)
        if created:
            print(f"   Created post with ID: {created['id']}")
        
        # PUT request
        print("\n4. PUT Request:")
        updated_post = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated content",
            "userId": 1
        }
        updated = client.put("posts/1", updated_post)
        if updated:
            print(f"   Updated: {updated['title']}")
        
        # DELETE request
        print("\n5. DELETE Request:")
        deleted = client.delete("posts/1")
        print(f"   Deleted: {deleted}")


def safe_nested_get(data: Dict, *keys: str, default: Any = None) -> Any:
    """
    Safely get nested dictionary value
    
    Args:
        data: Dictionary to traverse
        *keys: Keys to traverse
        default: Default value if key not found
    
    Returns:
        Value at nested key or default
    
    Example:
        >>> data = {"a": {"b": {"c": 123}}}
        >>> safe_nested_get(data, "a", "b", "c")
        123
        >>> safe_nested_get(data, "a", "x", "y", default=0)
        0
    """
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data


def parse_with_validation(data: Dict[str, Any], schema: Dict[str, type]) -> bool:
    """
    Validate data against schema
    
    Args:
        data: Data to validate
        schema: Schema definition {field: type}
    
    Returns:
        True if valid, False otherwise
    """
    for field, expected_type in schema.items():
        if field not in data:
            logger.error(f"Missing required field: {field}")
            return False
        
        if not isinstance(data[field], expected_type):
            logger.error(
                f"Invalid type for {field}: "
                f"expected {expected_type}, got {type(data[field])}"
            )
            return False
    
    return True


def demonstrate_helper_functions() -> None:
    """Demonstrate helper functions"""
    print("\n" + "=" * 60)
    print("HELPER FUNCTIONS")
    print("=" * 60)
    
    # Safe nested get
    print("\n1. Safe Nested Get:")
    data = {
        "user": {
            "profile": {
                "name": "John Doe",
                "age": 30
            }
        }
    }
    
    name = safe_nested_get(data, "user", "profile", "name")
    print(f"   Name: {name}")
    
    missing = safe_nested_get(data, "user", "settings", "theme", default="light")
    print(f"   Theme (default): {missing}")
    
    # Validation
    print("\n2. Data Validation:")
    post_schema = {
        "userId": int,
        "id": int,
        "title": str,
        "body": str
    }
    
    valid_post = {
        "userId": 1,
        "id": 1,
        "title": "Test",
        "body": "Content"
    }
    
    invalid_post = {
        "userId": "1",  # Wrong type
        "id": 1,
        "title": "Test"
        # Missing body
    }
    
    print(f"   Valid post: {parse_with_validation(valid_post, post_schema)}")
    print(f"   Invalid post: {parse_with_validation(invalid_post, post_schema)}")


def demonstrate_data_transformation() -> None:
    """Demonstrate data transformation patterns"""
    print("\n" + "=" * 60)
    print("DATA TRANSFORMATION")
    print("=" * 60)
    
    config = APIConfig(base_url="https://jsonplaceholder.typicode.com")
    
    with APIClient(config) as client:
        posts = client.get("posts", params={"_limit": 5})
        
        if posts:
            # Transform to simplified structure
            simplified = [
                {
                    "id": post["id"],
                    "title": post["title"],
                    "preview": post["body"][:50] + "..."
                }
                for post in posts
            ]
            
            print("\n1. Simplified Posts:")
            for post in simplified[:3]:
                print(f"   {post['id']}: {post['title']}")
            
            # Group by userId
            by_user = {}
            for post in posts:
                user_id = post["userId"]
                if user_id not in by_user:
                    by_user[user_id] = []
                by_user[user_id].append(post["title"])
            
            print("\n2. Grouped by User:")
            for user_id, titles in by_user.items():
                print(f"   User {user_id}: {len(titles)} posts")


if __name__ == "__main__":
    demonstrate_api_client()
    demonstrate_helper_functions()
    demonstrate_data_transformation()
    
    print("\n" + "=" * 60)
    print("COMPLETED: Best Practices")
    print("=" * 60)
