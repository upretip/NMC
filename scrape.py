#!./venv/bin/python3

"""
This script takes in the doctor's Nepal Medical Council ID and then returns the information that is available on NMC website
"""

from typing import List
import logging

import requests
from bs4 import BeautifulSoup


logging.basicConfig(filename='scrape.log', filemode='w', 
    format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)

# URL = f{}'
# headers = {"Host": "nmc.org.np",
#             "Connection": "keep-alive",
#             "Content-Length": '255',
#             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#             "Content-Type": "application/x-www-form-urlencoded",
#             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "X-Requested-With":"XMLHttpRequest",
#             "DNT": "1",
#             "Referer": "https://nmc.org.np",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Accept-Language": "en-US, en; q=0.8;q=0.6"}


def get_doctor_info(nmc_number: int = None) -> List:
    """
    Function that takes NMC ID no and retrieves the info on the doctor
    @param: nmc_number(int): the Doctor's ID 
    Returns: List(str): [name, nmc_number, city, gender, degree]

    Usage:
    get_doctor_info(123):
    >> ['Dr. Heralal Babu Shrestha' 123, 'Pokhara, Kaski', 'Male', 'MBBS']

    """
    try:
        URL = f"https://nmc.org.np/searchPractitioner?name=&degree=&nmc_no={nmc_number}"
        data = requests.get(URL).text
        soup = BeautifulSoup(data, "html.parser")
        result = soup.find("tbody")
        return [row.find_all("td")[1].text.strip() for row in result.find_all("tr")]

    except Exception as e:
        logging.warn(f"{e} for nmc number {nmc_number}")
        pass


if __name__ == "__main__":
    print(get_doctor_info(5))
