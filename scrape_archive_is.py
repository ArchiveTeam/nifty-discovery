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
        found_next = False
        tries = 0
        while True:
            try:
                r = requests.get("http://archive.is/offset={}/{}".format(of, domain))
                
                assert r.status_code == 200
                
                soup = BeautifulSoup(r.text, "lxml")
                for link in soup.find_all(style="display:block;margin-top:10px;color:#1D2D40;font-size:10px"):
                    url = str(link.text).strip()
                    if url:
                        urls.append(url)
                
                if soup.find("a", id="next") != None:
                    found_next = True
                
                break
            
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
        
        if not found_next:
            print("No next link found at domain={} of={}, scraping next domain".format(domain, of))
            break
