from sys import argv
from tqdm import tqdm

urls = set()

for url in tqdm(open(argv[1])):
    url = url.strip()
    urls.add(url)
    url = "/".join(url.split("/", 5)[0:4])+"/"
    urls.add(url)

for url in sorted(list(urls)):
    print(url)
