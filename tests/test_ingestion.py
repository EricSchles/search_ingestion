from ingestion.engine import Crawler
import requests
from subprocess import call
import json

# def test_single_page_crawl():
#     c = Crawler("http://localhost:5000/test_one",1)
#     print "initialized crawler.."
#     c.crawl()
#     print "crawled website.."
#     assert c.urls == ["http://localhost:5000/test_one"] 
#     assert c.data == ["Hello World!"]
    
    
# def test_single_page_with_html_crawl():
#     c = Crawler("http://localhost:5000/test_two",1)
#     print "initialized crawler.."
#     c.crawl()
#     print "crawled website.."
#     assert c.urls == ["http://localhost:5000/test_two"] 
#     assert c.data == ["Hello World!"]
    
# def test_single_page_with_complex_content():
#     c = Crawler("http://hackingagainstslavery.github.io",1)
#     print "initalized crawler.."
#     c.crawl()
#     print "crawled website.."
#     assert c.urls == ['https://github.com/hackingagainstslavery', 'http://hackingagainstslavery.slack.com', 'http://hackingagainstslavery.github.io']
#     print c.data
#     assert c.data == ["Hacking Against Slavery HomeAboutBlog Welcome to Hacking Against Slavery! An informal organization for ending slavery Sign up for our slack channel: http://hackingagainstslavery.slack.com by emailing us at hackingagainstslavery@gmail.comCheck out our github: https://github.com/hackingagainstslaverySeperately our voices are weak. Together our voices are strong. It's up to all of us to fight the evil in the world. And it starts by ensuring freedom for all. email github.com/hackingagainstslavery"]
#requests.post("http://localhost:5000/shutdown")

def test_uniqueify():
    c = Crawler("https://www.vets.gov",2)
    c.crawl()
    c.uniqueify()
    c.save_to_json()
    index = json.load(open('index.json','r'))
    urls = []
    unique_urls = []
    for ind,elem in enumerate(index):
        urls.append(elem['url'])
    unique_urls = list(set(urls))
    urls = [str(url) for url in urls]
    unique_urls = [str(url) for url in unique_urls]
    urls.sort()
    unique_urls.sort()
    print
    print "unique urls",len(unique_urls)
    print unique_urls
    print
    print
    print "urls",len(urls)
    print urls
    
    
    assert urls == unique_urls
        
