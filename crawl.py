import json
import requests

url = "https://resell.seetickets.com/api/adverts_search?tickets.product.category=4054&existAvailableTickets=true&status=1&orderby[nbCartTickets]=asc&&orderby[tickets.resaleValue]=asc&page=1&itemsPerPage=12"

payload = {}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Referer": "https://resell.seetickets.com/astateoftrance25/category/4054/weekend-tickets",
    "Cookie": "resale=fu7pgufcdl4agj6pfafg26i2j7; resale=jris3sltgr7buqk6f3dq04hmct",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
    "If-None-Match": 'W/"aa19c5cfb778a0387c66ce83cd3dd821"',
    "TE": "trailers",
}

response = requests.request("GET", url, headers=headers, data=payload)

with open("results.json", "w") as f:
    json.dump(response.json()["hydra:member"], f)
