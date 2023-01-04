import sys
import requests
from bs4 import BeautifulSoup

# Take url as input from the user

type = int(input("Is the Website HTTPS(1) or HTTP(2) ?"))
if type == 1:
    s = 'https://'
    print('--------------------------------------------------')
    print('\nEnter the Name of the Website you want to Scrape: ')
    print('--------------------------------------------------')
    data = input(s + "")
    Data = (s + data)
    url = Data
if type == 2:
    p = 'http://'
    print('--------------------------------------------------')
    print('\nEnter the Name of the Website you want to Scrape: ')
    print('--------------------------------------------------')
    data = input(p + "")
    Data = (p + data)
    url = Data


def scrape_html_elements():
    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all HTML elements
    elements = soup.find_all(True)  # True means that all tags will be returned

    # Save the elements to a list
    element_list = []
    for element in elements:
        print(element)
        element_list.append(element.prettify())  # Convert each element to a string and append to the list
    print()
    print('--------------------------------------------------')
    choice = input('would you like to save output? (y) (n) ')
    if choice == 'y':
        # Prompt the user for a file name
        print()
        print('--------------------------------------------------')
        file_name = input("Enter a name for the output file: ")

        # Open the file for writing
        with open(file_name, 'w', encoding='utf-8') as output_file:
            # Write each element to the file
            for element in element_list:
                output_file.write(element)
        print()
        print("File is succesfully saved.")
        print("Thank you for using Web Scrapper!")
        print("Quitting ...")
        sys.exit()
    if choice == 'n':
        print()
        print('--------------------------------------------------')
        print("Thank you for using Web scrapper!")
        print("Quitting ...")
        sys.exit()


scrape_html_elements()
