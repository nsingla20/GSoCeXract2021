import time
import requests
import csv
import json
def browse_and_scrape(url):
    with open("gsoc2021.csv",'w',encoding='utf-8') as file:
        writer=csv.writer(file)
        writer.writerow(["NAME","Organisation","Project"])
        try:
            while(url!=None):
                response=json.loads(requests.get(url).text)
                for i in range(40):
                    writer.writerow([response['results'][i]['student']['display_name'],response['results'][i]['organization']['name'],response['results'][i]['title']])
                url=response['next']
        except:
            print("Index exceeded. Exiting...")
        finally:
            print("COMPLETED!")
browse_and_scrape("https://summerofcode.withgoogle.com/api/program/current/project/?page=1&page_size=40")