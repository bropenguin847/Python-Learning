"""
APIs (Application Programming Interfaces) are an essential part of modern software development,
allowing different applications to communicate and share data.


Libraries to install:
        - pandas fastparquet    (do: pip install pandas fastparquet)
        - requests library      (do: pip install requests)

data.gov.my is Malaysia's official open data portal.
This file details the API's response code and what each code means

Query Response:
CODE        STATUS              DESCRIPTION
200         OK                  Successful Request
400         Bad Request         Invalid request. Check error message for more information.
404	        Not Found	        The resource requested doesn't exist.
429	        Too Many Requests	Your client is currently being rate limited.
                                Request an API token at Authentication to increase usage limits.
500	        Server Error	    Something went wrong with OpenAPI!

By default, the API returns a list of records.
If more details are needed, implement the meta parameter:
Use & to combine meta parameter together.

Example: 
    (Without Meta)  "https://api.data.gov.my/data-catalogue?id=YOURID&limit=3"
    (With Meta)     "https://api.data.gov.my/data-catalogue?id=YOURID&limit=3&meta=true"


Query Parameters:

"""


import requests

# Making a GET request
def get_post(url, meta=bool):
    """
    If request successfully, returns json of response.
    If failed, returns error message
    """

    try:
        if meta is True:
            url += "&meta=true"
        
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None


def main():
    """
    Example code with Meta parameters
    """

    url = "https://api.data.gov.my/data-catalogue?id=prisoners_state&limit=3"
    posts = get_post(url, meta=True)

    if posts:
        # print('Posts Meta:', posts['meta'])
        # print('Fetched Data:', posts['data'])
        print(posts)
    else:
        print('Failed to fetch posts from API.')

    # Output
    # {'meta': {'catalogue_id': 'prisoners_state',  'data_as_of': '2022-12-31 23:59', 'last_updated': '2023-12-31 12:00', 'next_update': '2024-12-31 12:00', 'data_source': ['Penjara'], 'update_frequency': 'YEARLY', 'total': 3, 'limit': 3},
    #  'data': [{'sex': 'both', 'date': '2017-01-01', 'state': 'Malaysia', 'prisoners': 120048},
    #           {'sex': 'both', 'date': '2018-01-01', 'state': 'Malaysia', 'prisoners': 115488},
    #           {'sex': 'both', 'date': '2019-01-01', 'state': 'Malaysia', 'prisoners': 136145}]}

if __name__ == "__main__":
    main()
