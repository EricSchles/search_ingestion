from ingestion.engine import Crawler
from backend_api.clients import i14yClient
from sys import argv
import json

def main(website,depth,production=True):
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
        i14yClient.create(ind,elem['content'],elem['path'],
                          elem['created'],os.environ["drawer_handle"],os.environ["search_secret_token"],
                          title=elem['title'],description=elem['description'],
                          promote=elem['promote'],language=elem['language']) 
    
