# Imports
import PySimpleGUI as sg
import pandas as pd
import requests
from bs4 import BeautifulSoup


# Functions
def set_theme_and_open_window(layout, layout_x, layout_y, theme='DarkBlack1'):

    sg.set_options(element_padding=(0, 0))
    sg.theme(theme)
    window = sg.Window('', layout, resizable=True, size=(layout_x, layout_y), background_color='black', grab_anywhere=True)
    return window


def getdata(url):

    """
    Function uses requests library to get URL and return its text.
    """

    r = requests.get(url) # Gets url data

    return r.text # Returns text from url data

def Article_Format(event):  # Set-Up New window for Article to read

    """
    Function creates new window that summarizes article, and provides a value to the factualness of the article.
    """

    htmldata = getdata(df['Link'][event]) # Gets url text
    soup = BeautifulSoup(htmldata, 'html.parser') # Sparse data
    data = ''
    for data in soup.find_all('div', attrs={'class': 'short-on-time'}): # Strips words by spaces
        data.get_text().strip() 

    # Window layout
    layout_new = [[sg.T(df['Statement'][event], size=(55, None), text_color='#FF7F00', background_color='black')],
                  [sg.T('If your time is short: ', size=(55, None), text_color='#FF7F00', background_color='black')],
                  [sg.T(data.get_text().strip(), size=(60, None), background_color='black')],
                  [sg.T('Source: ' + df['Source'][event], background_color='black')],
                  [sg.T('Detection: ' + df['Label'][event], background_color='black')]
    ]

    new_window = set_theme_and_open_window(layout_new, 400, 400)
    new_window.read(close=True)

    return


# Uploading File from Fake News Scraper file
file_path = "NEWS.csv"
NEWS = pd.read_csv(file_path, encoding='utf-8') # Reads .csf file
df = pd.DataFrame(NEWS, columns=['Statement', 'Link', 'Date', 'Source', 'Label']) # Sparses file into columns
pd.set_option('display.max_columns', None) # Displays all of the columns

# Re-Labelling labels
label_mapping = {'pants-fire': 'Extremely False', 'false': 'False', 'barely-true': 'Barely True', 'true': 'True'}
df['Label'] = df['Label'].replace(label_mapping)


# Set the theme to black and white
sg.theme('DarkBlack1')

# Basic Layout
layout = [
    [sg.Text('FAKE NEWS FINDER', font=('Helvetica', 36), justification='center', size=(20, 1), background_color='black')],
    [sg.Text("Stories from Politico", 
             size=(90, None), font=('Helvetica', 14), text_color='dark grey', background_color='black', justification='center')],
    [sg.Text("\n\nTOP 5 STORIES:",
              size=(90, None), font=('Helvetica', 18), text_color='white', background_color='black', justification='center')],
    [sg.B(df['Statement'][0], key='0', pad=(20, 10), size=(50, 2))], # Story 1
    [sg.B(df['Statement'][1], key='1', pad=(20, 10), size=(50, 2))], # Story 2
    [sg.B(df['Statement'][2], key='2', pad=(20, 10), size=(50, 2))], # Story 3
    [sg.B(df['Statement'][3], key='3', pad=(20, 10), size=(50, 2))], # Story 4
    [sg.B(df['Statement'][4], key='4', pad=(20, 10), size=(50, 2))]  # Story 5
]

window = set_theme_and_open_window(layout, 400, 700)

# If statement for the program to run
if __name__ == "__main__":
    try:
        # The Event Loop to run the program
        while True:
            event, values = window.read()

            if event in ['Exit', sg.WIN_CLOSED]:  # Closes program
                break

            if event.isdigit() and 0 <= int(event) < 5:
                Article_Format(int(event))

    except KeyboardInterrupt:
        pass

    finally:
        window.close()

# Explicitly set the theme for the new window
sg.set_options(element_padding=(0, 0))
sg.theme('DarkBlack1')


window.close()