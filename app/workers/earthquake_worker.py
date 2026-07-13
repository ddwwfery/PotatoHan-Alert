import requests

URL = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001"


def get_latest():

    r = requests.get(URL)

    print(r.status_code)

    print(r.text[:500])


if __name__ == "__main__":

    get_latest()