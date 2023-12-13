'''
Objectives:
Create a Python script that performs the following:

Prompt the user to type a string input as the variable for your destination URL.

Prompt the user to select a HTTP Method of the following options:
GET
POST
PUT
DELETE
HEAD
PATCH
OPTIONS
Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.

For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

For the given URL, print response header information to the screen.

Resources: 
https://chat.openai.com/share/94d24fb7-8e26-497d-a682-0156b5052946
'''

import requests

def get_user_input(prompt):
    return input(prompt).strip()

def get_http_method():
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']
    while True:
        method = get_user_input(f"Choose HTTP Method ({', '.join(methods)}): ").upper()
        if method in methods:
            return method
        else:
            print("Invalid method. Please choose from the provided options.")

def translate_status_code(status_code):
    # Add more translations as needed
    status_code_translations = {
        200: 'OK',
        201: 'Created',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        500: 'Internal Server Error'
        # Add more as needed
    }
    return status_code_translations.get(status_code, f'Unknown Status Code: {status_code}')

def print_response(response):
    print(f"\nResponse from {response.url}:")
    print(f"Status Code: {response.status_code} ({translate_status_code(response.status_code)})")
    print("Headers:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")

def main():
    destination_url = get_user_input("Enter destination URL: ")
    http_method = get_http_method()

    print("\nRequest to be sent:")
    print(f"URL: {destination_url}")
    print(f"HTTP Method: {http_method}")

    confirm = get_user_input("\nDo you want to proceed? (yes/no): ").lower()
    if confirm != 'yes':
        print("Operation aborted.")
        return

    response = requests.request(http_method, destination_url)

    print_response(response)

if __name__ == "__main__":
    main()
