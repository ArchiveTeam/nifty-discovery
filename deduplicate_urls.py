from sys import argv

urls = set()

for url in open(argv[1]):
    url = url.strip()
    urls.add(url)

for arg in argv[2:]:
    for url in open(arg):
        url = url.strip()
        urls.discard(url)

for url in sorted(list(urls)):
    print(url)

