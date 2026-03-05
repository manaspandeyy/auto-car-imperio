import urllib.request
import os

os.makedirs('css/bootstrap', exist_ok=True)
os.makedirs('assets/img/cars', exist_ok=True)

def dl(url, path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(path, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded {path}")
    except Exception as e:
        print(f"Failed {path}: {e}")

images = {
    # Vintage Rolls Royce wedding car
    "VINTAGE.jpg": "https://images.unsplash.com/photo-1549646445-538964ac2605?w=600&q=80",
    
    # White Toyota SUV (Fortuner lookalike)
    "FORTUNER.jpg": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=600&q=80",
    
    # Red/Black Jeep Wrangler / Thar Lookalike
    "THAR.jpg": "https://images.unsplash.com/photo-1559416523-140ddc3d238c?w=600&q=80",
    
    # Red VW Golf/Polo
    "POLO.jpg": "https://images.unsplash.com/photo-1540940562573-0498305c6d32?w=600&q=80",
    
    # White modern crossover SUV (Creta lookalike)
    "CREATA.jpg": "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?w=600&q=80",
    
    # Tata Harrier/Safari dark SUV lookalike
    "TATA.jpg": "https://images.unsplash.com/photo-1563720224185-115f5a898df5?w=600&q=80",
    
    # Grey/Black Audi Sedan
    "AUDI.jpg": "https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?w=600&q=80",
    
    # Mercedes V-Class / Minivan
    "MINIVAN.jpg": "https://images.unsplash.com/photo-1567808291548-fc3eb04ce84d?w=600&q=80",
    
    # White compact sedan (Dzire Lookalike)
    "desire.jpg": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=600&q=80"
}

for name, url in images.items():
    dl(url, f"assets/img/cars/{name}")
