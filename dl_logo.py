import urllib.request

def dl(url, path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(path, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded {path}")
    except Exception as e:
        print(f"Failed {path}: {e}")

# ABI Text Logo
dl("https://dummyimage.com/200x200/2c3e50/fff.png&text=ABI", "assets/img/logo.png")
dl("https://dummyimage.com/200x200/2c3e50/fff.png&text=ABI", "assets/img/logoBlack.png")
