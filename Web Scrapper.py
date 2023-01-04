import sys
import time
import requests
from bs4 import BeautifulSoup

# Take url as input from the user and checking if the website is Valid
while True:
    try:
        choice = int(input('Is the Website HTTPS(1) or HTTP(2) ?'))
        break
    except ValueError:
        print("Please enter a valid input!")
if choice == 1:
    while True:
        try:
            s = 'https://'
            print('--------------------------------------------------')
            print('\nEnter the Name of the Website you want to Scrape: ')
            print('--------------------------------------------------')

            data = input(s + "")
            # concatenate
            Data = (s + data)
            url = Data

            test = requests.get(url)
            break
        except requests.exceptions.ConnectionError:
            print("Enter a Valid Website !")
if choice == 2:
    while True:
        try:
            p = 'http://'
            print('--------------------------------------------------')
            print('\nEnter the Name of the Website you want to Scrape: ')
            print('--------------------------------------------------')
            data = input(p + "")
            # concatenate
            Data = (p + data)
            url = Data
            test = requests.get(url)
            break
        except requests.exceptions.ConnectionError:
            print("Enter a Valid Website !")


def scrape():
    # Send a GET request to the website
    startTime = time.time()
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all HTML elements
    elements = soup.find_all(True)  # True means that all tags will be returned

    # Save the elements to a list
    element_list = []
    for element in elements:
        print(element)  # Print the Results on the Terminal
        # Convert each element to a string and append to the list
        element_list.append(element.prettify())
    print()
    print('--------------------------------------------------')
    totalTime = round(time.time() - startTime, 2)
    print("Scrapping Time Taken: ", totalTime)
    print('--------------------------------------------------')
    # Ask the User if he/she want to save the results
    while True:
        try:
            save = int(input('would you like to save output? (1) (2) '))
            break
        except ValueError:
            print("Enter a Valid input!")
    if save == 1:
        # Ask The User for a File Name
        print()
        print('--------------------------------------------------')
        file_name = input("Enter a name for the output file: ")

        # Open the file for writing
        with open(file_name, 'w', encoding='utf-8') as output_file:  # to encode all unicode characters
            # Write each element to the file
            for element in element_list:
                output_file.write(element)
            output_file.close()
        print()
        print("File is successfully saved.")
        print("Thank you for using Web Scrapper!")
        print("Quitting ...")
        sys.exit()
    if save == 2:
        print()
        print('--------------------------------------------------')
        print("Thank you for using Web scrapper!")
        print("Quitting ...")
        sys.exit()


# Call the Function
scrape()
