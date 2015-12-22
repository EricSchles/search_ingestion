from ingestion.engine import Crawler
from backend_api.clients import i14yClient
from sys import argv
import json
import pickle

def main(website,depth,production=True):
    staging = pickle.load(open("i14y_creds.pickle","r"))
    website = "https://" + website
    if production:
        c = Crawler(website,int(depth))
    else:
        c = Crawler(website,int(depth),username=os.environ["staging_username"],password=os.environ["staging_password"],basic_auth_required=True)
    c.crawl()
    c.save_to_json()
    index = json.load(open('index.json','r'))
    #ToDo: Create a staging drawer and request a second search token
    for ind,elem in enumerate(index):
        i14yClient.create(ind,elem['content'],elem['url'],
                          elem['created'],staging[0],staging[1],
                          title=elem['title'],description=elem['description'],
                          promote=elem['promote'],language=elem['language']) 
    
if __name__ == '__main__':
    main("www.vets.gov/",6,production=True)
