from get_urls_engine import Crawler
import pandas as pd
import pickle

def main(website,depth,production=True):
    vets_creds = pickle.load(open("vets_creds.pickle","r"))
    df = pd.DataFrame()
    website = "https://" + website
    if production:
        c = Crawler(website,int(depth))
    else:
        c = Crawler(website,int(depth),username=vets_creds[0],password=vets_creds[1],basic_auth_required=True,testing=True)
    c.crawl()
    c.uniqueify()
    for i in c.unique_data:
        df = df.append(i,ignore_index=True)
    df.to_csv("results.csv")
        
if __name__ == '__main__':
    #main("staging.vets.gov/",6,production=False)
    main("www.vets.gov/",6,production=True)
