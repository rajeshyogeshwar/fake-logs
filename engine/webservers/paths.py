"""Path module."""

import random
from faker import Faker
from itertools import product

class RequestedPath:
    """Generates a requested path for the log entries."""
    
    product_ids = list(range(1, 51))
    base_paths = [
        "GET /", 
        "GET /login/",
        "POST /login/",
        "GET /logout/",
        "GET /categories/",
        "GET /categories/medical-devices/",
        "GET /categories/mobiles/",
        "GET /categories/tablets/",
        "GET /categories/laptops/",
        "GET /categories/home-appliances/",
        "GET /categories/books/",
        "GET /categories/video-games/", 
        "GET /cart/", 
        "GET /checkout/"
        "POST /make-payment/"
    ]

    detail_paths = [
        "GET /categories/medical-devices/products/",
        "GET /categories/mobiles/products/",
        "GET /categories/tablets/products/",
        "GET /categories/laptops/products/",
        "GET /categories/home-appliances/products/",
        "GET /categories/books/products/",
        "GET /categories/video-games/products/",
        "POST /add-to-cart/",
        "DELETE /remove-from-cart/",
        "POST /rate-product/",
        "GET /product-reviews/"
        "POST /add-review-for-product/",
    ]

    @classmethod
    def generate(cls) -> str:
        """Generate a random requested path."""

        choice = random.choice([0,1,2])
        
        if choice == 0:
            return random.choice(cls.base_paths)
        elif choice == 1:
            fk = Faker()
            query_param = "".join(fk.random_letters())
            return f"GET /search/?query={query_param}"
        else:
            product_id = random.randrange(1, 51)
            path = random.choice(cls.detail_paths)
            return f"{path}{product_id}/"
