import urllib.request
import os
import shutil

os.makedirs('assets/img/me', exist_ok=True)
os.makedirs('assets/icon', exist_ok=True)
os.makedirs('src/testing', exist_ok=True)

def dl(url, path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(path, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded {path}")
    except Exception as e:
        print(f"Failed {path}: {e}")

# Copy logo to logoBlack.png
try:
    shutil.copyfile('assets/img/logo.png', 'assets/img/logoBlack.png')
    print("Copied logoBlack.png")
except Exception as e:
    print(f"Failed logoBlack: {e}")

# Download avatar
dl("https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=200&h=200&fit=crop&q=80", "assets/img/me/me.jpg")

# Download refresh icon 
dl("https://dummyimage.com/32x32/fff/000.png&text=R", "assets/icon/icons8_refresh_32.png")

# Create empty testing.css needed for admin.html
open("src/testing/testing.css", "w").close()
print("Created testing.css")
