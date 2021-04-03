import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse


def get_short_link(input_url):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
      "Authorization": f"Bearer {token}"}
    payload = { "long_url": input_url}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    shorten_link = response.json()['link']
    return(shorten_link) 

def get_total_clicks(input_url):
    headers = {
      "Authorization": f"Bearer {token}"}
    parsed = urlparse(input_url)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc}{parsed.path}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return(response.json["total_clicks"])

def get_bitly_info(token,input_url):
    headers = {
      "Authorization": f"Bearer {token}"}
    parsed = urlparse(input_url)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc}{parsed.path}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'shorten link.')
    parser.add_argument("echo")

    load_dotenv()
    token = os.getenv("BIT.LY_TOKEN")
    args = parser.parse_args()
    input_url = args.echo
    try:
        get_bitly_info(token,input_url)
        print("количество переходов:", get_total_clicks(input_url))
    except requests.exceptions.HTTPError:
        try:
            print(get_short_link(input_url))
        except requests.exceptions.HTTPError:
            print("error")