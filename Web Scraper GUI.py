import tkinter as tk
import sys
import time
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox

def on_select(v):
    global s, p
    if v == 1:
        s = 'https://'
    elif v == 2:
        p = 'http://'

def stop_scraping():
    global scraping
    scraping = False

def scrape():
    global scraping
    scraping = True
    var = tk.IntVar()
    on_select(var.get())
    url = s + txt_website.get() if s != "" else p + txt_website.get()
    startTime = time.time()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(True)
    element_list = []
    for element in elements:
        if not scraping:
            break
        element_list.append(element.prettify())
    totalTime = round(time.time() - startTime, 2)
    messagebox.showinfo("Scrapping Time Taken", "Scrapping Time Taken: " + str(totalTime))
    save_file(element_list)



def save_file(element_list):
    if save_var.get() == 1:
        file_name = txt_file_name.get()
        with open(file_name, 'w', encoding='utf-8') as output_file:
            for element in element_list:
                output_file.write(element)
            output_file.close()
        messagebox.showinfo("Info", "File is successfully saved.")
        scrape_again = messagebox.askyesno("Scrape Again?", "Do you want to scrape another website?")
        if scrape_again:
            validate()
        else:
            messagebox.showinfo("Info", "Quitting...")
            sys.exit()
    else:
        messagebox.showinfo("Info", "Quitting...")
        sys.exit()


def validate():
    global url
    if (s == 'https://' or p == 'http://') and txt_website.get() != "":
        url = s + txt_website.get() if s != "" else p + txt_website.get()
        try:
            test = requests.get(url)
            messagebox.showinfo("Website is Valid", "Website is valid!")
            scrape()
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "Enter a valid website!")
    else:
        messagebox.showerror("Error", "Enter a valid input!")
root = tk.Tk()
root.geometry("400x300")
root.title("Web Scraper")

lbl_protocol = tk.Label(root, text="Is the Website HTTPS or HTTP ?")
lbl_protocol.pack()

var = tk.IntVar()
r1 = tk.Radiobutton(root, text="HTTPS", variable=var, value=1, command=lambda: on_select(1))
r1.pack()
r2 = tk.Radiobutton(root, text="HTTP", variable=var, value=2, command=lambda: on_select(2))
r2.pack()

lbl_website = tk.Label(root, text="Enter the name of the website you want to scrape: ")
lbl_website.pack()

txt_website = tk.Entry(root)
txt_website.pack()

lbl_save = tk.Label(root, text="Do you want to save the output? ")
lbl_save.pack()

save_var = tk.IntVar()
c1 = tk.Checkbutton(root, text="Save", variable=save_var)
c1.pack()

lbl_file_name = tk.Label(root, text="Enter a name for the output file: ")
lbl_file_name.pack()

txt_file_name = tk.Entry(root)
txt_file_name.pack()

btn_scrape = tk.Button(root, text="Scrape", command=validate)
btn_scrape.pack()

btn_stop = tk.Button(root, text="Stop", command=stop_scraping)
btn_stop.pack()

scraping = False
s = ""
p = ""

root.mainloop()
