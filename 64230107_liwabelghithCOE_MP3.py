
from tkinter import *
from bs4 import BeautifulSoup
import requests
import re

class Scraping:
    def __init__(self):
        self.annountext = []
        self.announhref = []
        self.urls = [
            "https://www.medipol.edu.tr/en/announcements?page=0",
            "https://www.medipol.edu.tr/en/announcements?page=1",
            "https://www.medipol.edu.tr/en/announcements?page=2",
            "https://www.medipol.edu.tr/en/announcements?page=3",
            "https://www.medipol.edu.tr/en/announcements?page=4",
            "https://www.medipol.edu.tr/en/announcements?page=5"
        ]
        self.scrape_data()
        
    def scrape_data(self):
        for url in self.urls:
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            div_elements = soup.find_all('div', class_='col-md-4 col-sm-6 list-card')
            for div_element in div_elements:
                a_element = div_element.find('a')
                if a_element:
                    link_href = a_element.get('href')
                    self.announhref.append(link_href)
                   
            print(f"12 Announcements scraped from {url}")
        for urlh in self.announhref:
            req = requests.get(urlh)
            soup = BeautifulSoup(req.content, 'html.parser')
            h1elements = soup.find_all('h1', class_='page-title') 
            for h1_element in h1elements:
                span_elements = h1_element.find_all('span')
                for span_element in span_elements:
                    span_text = span_element.get_text(strip=True)
                    self.annountext.append(span_text) 

class GUI(Frame):
    def __init__(self, parent, annountext, announhref):
        super().__init__(parent)
        self.parent = parent
        self.previous_selection = None  
        self.value = "" 
        self.annountext = annountext
        self.announhref = announhref
        self.time = ""
        self.initUI()

    def on_select(self, event):
        self.listbox1.delete(0, END)  # Clear listbox1 content
        w = event.widget
        if not w.curselection():
            return
        index = int(w.curselection()[0])
        value = w.get(index)
        if self.previous_selection is not None:
            self.listbox.itemconfig(self.previous_selection, {'bg': 'lightgray'})
        self.listbox.itemconfig(index, {'bg': 'white'})
        self.previous_selection = index
        self.parent.title(f"Medipol University Announcements | {value}")

        # Scrape the selected announcement's page
        req = requests.get(self.announhref[index])
        soup = BeautifulSoup(req.content, 'html.parser')
        
        # Update the time
        timelement = soup.find('span', class_='xs-mt-10')
        self.time = timelement.get_text() if timelement else "No time available"
        self.label2.config(text=self.time)

        # Update the content
        div_elements = soup.find_all('div', class_=re.compile(r'^paragraph.*view-mode--default$'))
        for div_element in div_elements:
            text = div_element.get_text(separator=" ", strip=True)
            segments = text.split('.')  # Split text at each period
            for segment in segments:
                if segment.strip():  # Avoid adding empty segments
                    self.listbox1.insert(END, segment.strip() + '.')  # Re-add the period and insert
        # Add some space lines for better readability
        e="                              "
        z="                              "
        a="                              "
        w="                              "
        self.listbox1.insert(END,f"{e}")
        self.listbox1.insert(END,f"{z}")
        self.listbox1.insert(END,f"{w}")
        self.listbox1.insert(END,f"{a}")
        
        # Extract links
        a_elements = soup.select('div.paragraph > p > a')
        self.listbox1.insert(END,f"this the urls: ")
        for a_element in a_elements:
            link_text = a_element.get_text(strip=True)
            link_href = a_element.get('href')
            self.listbox1.insert(END, f"Link: {link_text} - {link_href}")
    
    def initUI(self):
        self.pack(fill=BOTH, expand=True)
        self.label = Label(self, text="Announcements")
        self.label.grid(row=0, column=0, padx=200, pady=10)
        self.listbox = Listbox(self, selectmode=NORMAL, height=35, width=100)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        self.listbox.grid(row=1, column=0)
        for text in self.annountext:
            self.listbox.insert(END, text)
        self.label1 = Label(self, text="Content of Announcement                                                                          ")
        self.label1.grid(row=0, column=1, sticky=W, pady=10, columnspan=3)
        self.label2 = Label(self, text="vz")
        self.label2.grid(row=0, column=4, sticky=W, pady=10)
        self.listbox1 = Listbox(self,selectmode=EXTENDED,height=35, width=100)
        self.listbox1.grid(row=1, column=1, columnspan=3)

def main():
    root = Tk()
    root.geometry("1300x700+100+50")
    root.title("Medipol University Announcements")

    scraping = Scraping()
    app = GUI(root, scraping.annountext, scraping.announhref)

    root.mainloop()

if __name__ == "__main__":
    main()
