DOMAINS = ["homepage1.nifty.com",
    "homepage2.nifty.com",
    "homepage3.nifty.com"]

from sys import argv
from time import sleep

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

out = open(argv[1], "a")

for domain in DOMAINS:
    print("Scraping domain {}".format(domain))
    t = tqdm()
    of = 0
    while True:
        urls = []
        try:
            tries = 0
            r = requests.get("http://b.hatena.ne.jp/entrylist?url=http%3A%2F%2F"+domain+"&of={}".format(of))
            
            assert r.status_code == 200
            
            soup = BeautifulSoup(r.text, "lxml")
            for link in soup.find_all(class_='entry-link'):
                url = str(link['href']).strip()
                if url:
                    urls.append(url)
        
        except Exception as ex:
            print(ex)
            print("Failed at domain={} of={}, retrying".format(domain, of))
            sleep(1)
            tries += 1
            if tries > 3:
                break
        
        for url in urls:
            out.write(url+"\n")
        
        of += len(urls)
        t.update()
        
        if not urls:
            print("No urls at domain={} of={}, scraping next domain".format(domain, of))
            break
