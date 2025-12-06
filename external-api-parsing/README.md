# External API Parsing Practice

This folder contains comprehensive examples for practicing API calls and JSON parsing for senior developer interviews.

## Topics Covered

1. **Basic API Calls** - GET, POST, PUT, DELETE
2. **Deep JSON Parsing** - Nested objects, arrays, complex structures
3. **Error Handling** - Network errors, API errors, parsing errors
4. **Best Practices** - Type safety, async/await, proper error handling
5. **Real-world Examples** - Multiple public APIs
6. **Interview Questions** - Common scenarios and solutions

## Files

- `01-basic-api-calls.py` - Basic HTTP methods and response handling
- `02-deep-json-parsing.py` - Complex nested JSON parsing (7 examples)
- `03-error-handling.py` - Comprehensive error handling patterns
- `04-best-practices.py` - Production-ready code with all best practices
- `05-real-world-examples.py` - Multiple API integrations (6 different APIs)
- `06-interview-questions.py` - Common interview scenarios with solutions
- `BEST_PRACTICES.md` - Complete guide to API best practices
- `requirements.txt` - Python dependencies

## Setup

```bash
# Install dependencies
pip install -r requirements.txt
```

## Run Examples

```bash
# Run all examples in order
python 01-basic-api-calls.py
python 02-deep-json-parsing.py
python 03-error-handling.py
python 04-best-practices.py
python 05-real-world-examples.py
python 06-interview-questions.py

# Or run individually based on what you want to practice
```

## What You'll Learn

### 1. Basic API Calls (01-basic-api-calls.py)
- GET requests with and without parameters
- POST requests to create resources
- PUT requests to update resources
- DELETE requests
- Response inspection (headers, status codes, timing)

### 2. Deep JSON Parsing (02-deep-json-parsing.py)
- Simple flat JSON structures
- Nested objects (2-3 levels deep)
- Arrays of objects
- Complex nested structures
- Safe nested access patterns
- Filtering and transforming data
- Mixed arrays and objects

### 3. Error Handling (03-error-handling.py)
- HTTP error handling (404, 500, etc.)
- Network errors (timeout, connection)
- JSON parsing errors
- Safe API call wrapper
- Retry logic with exponential backoff
- Response data validation

### 4. Best Practices (04-best-practices.py)
- Production-ready API client class
- Type hints and dataclasses
- Logging and monitoring
- Session management
- Context managers for cleanup
- Helper functions for safe access
- Data transformation patterns

### 5. Real-world Examples (05-real-world-examples.py)
- GitHub API - Repository information
- REST Countries API - Complex nested data
- JSONPlaceholder - Multi-endpoint aggregation
- Open-Meteo - Weather data with time series
- Cat Facts API - Simple pagination
- Data aggregation from multiple sources

### 6. Interview Questions (06-interview-questions.py)
- Rate limiting implementation
- Response caching with TTL
- Pagination handling
- Error recovery in batch operations
- JSON schema validation
- Data transformation (flattening)
- Concurrent API requests
- API versioning

## APIs Used (All Free, No Auth Required)

1. **JSONPlaceholder** - `https://jsonplaceholder.typicode.com`
   - Fake REST API for testing
   - Users, posts, comments, albums, todos

2. **GitHub API** - `https://api.github.com`
   - Repository information
   - No auth needed for public repos

3. **REST Countries** - `https://restcountries.com`
   - Country information
   - Complex nested structures

4. **Open-Meteo** - `https://api.open-meteo.com`
   - Weather forecasts
   - Time series data

5. **Cat Facts** - `https://catfact.ninja`
   - Random cat facts
   - Pagination examples

## Key Concepts for Senior Developer Interviews

### Must Know
- ✅ Error handling (try/except, specific exceptions)
- ✅ Timeouts (always set them!)
- ✅ Type hints (Dict, List, Optional, Any)
- ✅ Logging (info, error, debug)
- ✅ Safe JSON access (.get() method)
- ✅ Session management (reuse connections)
- ✅ Retry logic (exponential backoff)
- ✅ Data validation (schema checking)

### Should Know
- ✅ Rate limiting (token bucket algorithm)
- ✅ Caching (TTL-based, LRU)
- ✅ Pagination (automatic page fetching)
- ✅ Concurrent requests (ThreadPoolExecutor)
- ✅ API versioning (URL or header based)
- ✅ Context managers (resource cleanup)
- ✅ Dataclasses (structured data)
- ✅ Enums (type-safe constants)

### Nice to Have
- ✅ Async/await (aiohttp)
- ✅ Circuit breaker pattern
- ✅ Request/response middleware
- ✅ API mocking for tests
- ✅ Metrics and monitoring

## Practice Tips

1. **Start Simple** - Run 01-basic-api-calls.py first
2. **Go Deep** - Practice 02-deep-json-parsing.py multiple times
3. **Handle Errors** - Study 03-error-handling.py patterns
4. **Learn Patterns** - Understand 04-best-practices.py structure
5. **Real APIs** - Experiment with 05-real-world-examples.py
6. **Interview Prep** - Master 06-interview-questions.py scenarios
7. **Read Guide** - Study BEST_PRACTICES.md thoroughly

## Common Mistakes to Avoid

❌ Not setting timeouts
❌ Not handling exceptions
❌ Using requests without sessions
❌ Hardcoding API keys
❌ Not validating response data
❌ Ignoring rate limits
❌ Not using type hints
❌ Poor error messages
❌ Not logging important events
❌ Trusting external data

## Interview Preparation Checklist

- [ ] Can explain HTTP methods (GET, POST, PUT, DELETE)
- [ ] Can handle all common exceptions
- [ ] Can parse deeply nested JSON (3+ levels)
- [ ] Can implement retry logic
- [ ] Can implement rate limiting
- [ ] Can implement caching
- [ ] Can handle pagination
- [ ] Can make concurrent requests
- [ ] Can validate JSON schemas
- [ ] Can write production-ready code
- [ ] Can explain security best practices
- [ ] Can write tests for API code

## Next Steps

1. Run all examples to see them in action
2. Modify examples to experiment
3. Try different APIs
4. Implement your own API client
5. Practice explaining your code
6. Review BEST_PRACTICES.md before interviews

Good luck with your senior developer interview! 🚀
