# SEP300: Assignment file 1
# Arian Amiri: 186610218

import requests
import asyncio


async def fetch_data(url):
    response = ""
    status_code = 0

    while 200 > status_code or status_code >= 400:
        response = requests.get(url)
        status_code = response.status_code

    if 200 <= status_code < 400:
        print("The following is the response from " + url + ":")
        print(response.status_code)
        return ("fetched data from the " + url +
                " with status code " + str(status_code))


async def main():
    tasks = [
        fetch_data("http://crysxd.github.io/Herbboy-Dummy-Website/"),
        fetch_data("https://www.yorku.ca/edu/research/public-lecture-series/"),
        fetch_data("https://dummyjson.com/products"),
    ]

    results = await asyncio.gather(*tasks)
    print("Complete!")

    for result in results:
        print(result)

asyncio.run(main())
