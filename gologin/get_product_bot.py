import json
import requests
from collections import OrderedDict
import os
import glob

def get_product(location, sku):
    

    def get_json_files(folder_path):
        json_files = glob.glob(os.path.join(folder_path, '*.json'))
        return json_files

    folder_path = 'headers'  # Replace with the actual folder path
    header_files = get_json_files(folder_path)
    print(header_files)

    headers_array = []
    proxy_usernames = []
    for header_file in header_files:
        # Load headers from the JSON file
        with open(header_file, 'r') as json_file:
            headers_data = json.load(json_file)
        # print(headers_data['x-hermes-locale'])
        temp_headers = {}
        if location in headers_data['x-hermes-locale']:
            for header_name, header_value in headers_data.items():
                if header_name != "proxy_username":
                    temp_headers[header_name] = header_value
                else:
                    proxy_usernames.append(header_value)

            headers_array.append(temp_headers)

    if len(headers_array) == 0:
        print(f"No header for '{location}'")
        return f"No header for '{location}'"
    
    index = 0
    for _ in range(len(headers_array)):
        proxies = {
            'http': f'http://{proxy_usernames[index]}:b6wj9r5p2wqi@brd.superproxy.io:22225',
            'https': f'http://{proxy_usernames[index]}:b6wj9r5p2wqi@brd.superproxy.io:22225',
        }

        url = f"https://bck.hermes.com/product?locale={headers_array[index]['x-hermes-locale']}&productsku={sku}"
        print(url)
        response = requests.get(url, proxies=proxies, headers=headers_array[index])

        # Check if the response is in JSON format
        if response.headers.get('content-type') == 'application/json':
            # Parse the JSON response
            json_data = response.json()
            
            # Prettify the JSON
            prettified_json = json.dumps(json_data, indent=4)
            
            print(prettified_json)
            return prettified_json
        else:
            print("Response is not in JSON format.")
            json_data = response.json()
            
            # Prettify the JSON
            prettified_json = json.dumps(json_data, indent=4)
            
            print(prettified_json)
            # continue
            # continue
        index += 1

    return "Not found product"
    
