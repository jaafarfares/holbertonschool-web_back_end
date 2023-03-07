import redis
import requests

redis_client = redis.Redis()


def get_page(url: str) -> str:
    """Returns the HTML content of a URL."""
    if redis_client.exists(url):
        return redis_client.get(url).decode('utf-8')
    response = requests.get(url)
    content = response.content.decode('utf-8')
    redis_client.setex(url, 10, content)
    redis_client.incr(f"count:{url}")
    return content
