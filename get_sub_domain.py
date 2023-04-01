import requests
from tqdm import tqdm
import multiprocessing
import json

def get_sub_domains(domain,filepath):
  url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"
  querystring = {"children_only":"false"}
  headers = {
  'accept': "application/json",
  'apikey': "ENTER_YOUR_API_KEY_HERE"
  }
  API_response = requests.get(url, headers=headers, params=querystring)

  result_json=json.loads(API_response.text)

  sub_domains=[i+'.'+domain for i in result_json['subdomains']]
  f=open(filepath,'w+')
  for i in sub_domains:
    f.write("https://"+i+'\n')
  f.close()

  with open(filepath, 'r') as f:
    links_all = f.read().splitlines()

  return links_all

def get_resp(link):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        requests.packages.urllib3.disable_warnings()
        response = requests.get(link, timeout=3, verify=False, headers=headers)
        status_code = str(response.status_code)
        values = link + " returns " + status_code
    except:
        values = link + " returns nothing"
    return values

def run():
    results=[]
    dom = input("\nEnter Domain name to find its sub-domains : ")
    file = input("\nOutput Filename to save all domain names from API response : ")
    links = get_sub_domains(dom,file)

    with multiprocessing.Pool() as pool:
        for result in tqdm(pool.imap(get_resp, links), total=len(links)):
            results.extend([result])

    output_file = str(dom) + "_response_code.txt"
    with open(output_file,'w') as tfile:
	    tfile.write('\n'.join(results))

if __name__ == "__main__":
    run()