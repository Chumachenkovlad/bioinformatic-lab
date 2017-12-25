import urllib.request
with open('links.txt') as f:
    for line in list(f.readlines())[1:3]:
        with urllib.request.urlopen(line.strip()) as response:
            html = response.read()
            print(html)
