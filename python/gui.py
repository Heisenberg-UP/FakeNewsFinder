# Imports
import PySimpleGUI as sg
import pandas as pd
import requests
from bs4 import BeautifulSoup


# Functions
def Article_Format(event):  # Set-Up New window for Article to read

    """
    Function creates new window that summarizes article, and provides a value to the factualness of the article.
    """

    def getdata(url):  # Gets URL as a string

        """
        Function uses requests library to get the URL and returns it as text.
        """
    
        r = requests.get(url)
        return r.text

    htmldata = getdata(df['Link'][event])
    soup = BeautifulSoup(htmldata, 'html.parser')
    data = ''
    for data in soup.find_all('div', attrs={'class': 'short-on-time'}):
        data.get_text().strip()

    layout_new = [[sg.T(df['Statement'][event], size=(55, None), text_color='#FF7F00')],
                  [sg.T('If your time is short: ', size=(55, None), text_color='#FF7F00')],
                  [sg.T(data.get_text().strip(), size=(60, None))],
                  [sg.T('Source: ' + df['Source'][event])],
                  [sg.T('Detection: ' + df['Label'][event])]]
    values, events = sg.Window('Article', layout_new, size=(400, 300)).read(close=True)
    return values, events


# Uploading File from Fake News Scraper file
NEWS = pd.read_csv('csv/NEWS.csv', encoding='utf-8') # Reads .csf file
df = pd.DataFrame(NEWS, columns=['Statement', 'Link', 'Date', 'Source', 'Label']) # Sparses file into columns
pd.set_option('display.max_columns', None) # Displays all of the columns

# Re-Labelling labels
df['Label'] = df['Label'].replace(['pants-fire'], 'Extremely False')
df['Label'] = df['Label'].replace(['false'], 'False')
df['Label'] = df['Label'].replace(['barely-true'], 'Barely True')
df['Label'] = df['Label'].replace(['true'], 'True')


# Create GUI for showing the .csv file data
sg.theme('Topanga')  # Theme for GUI

# Basic Layout
layout = [[sg.Text("All news is based on PolitiFact's website. \nPolitiFact.com is an American nonprofit project "
                   "operated by the Poynter Institute in St. Petersburg, Florida, with offices there and in "
                   "Washington, D.C. \n\n\nHere is a brief summary of the 5 most recent stories:", size=(90, None))],
          [sg.B(df['Statement'][0], key='0')], # Story 1
          [sg.B(df['Statement'][1], key='1')], # Story 2
          [sg.B(df['Statement'][2], key='2')], # Story 3
          [sg.B(df['Statement'][3], key='3')], # Story 4
          [sg.B(df['Statement'][4], key='4')]] # Story 5

window = sg.Window('Fake News Finder', layout, size=(600, 250)) # Sets Window Size and Label


# If statement for program to run
if __name__ == "__main__":

    try:

        # The Event Loop to run program
        while True:
            event, values = window.read()

            # Assigns a key to Article_Format() Function for proper article opening
            if event == '0':
                Article_Format(0)
            elif event == '1':
                Article_Format(1)
            elif event == '2':
                Article_Format(2)
            elif event == '3':
                Article_Format(3)
            elif event == '4':
                Article_Format(4)

            if event == sg.WIN_CLOSED or event == 'Exit': # Closes program
                break

    except KeyboardInterrupt:

        SystemExit


window.close()
