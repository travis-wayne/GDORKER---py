from googlesearch import search
import urllib.error
from termcolor import colored
import subprocess
import argparse

print (colored('''
 ____    ____    _   ____    _____   ____             ____ ____   ___  ____  _  _______ ____  
| ___|  |  _ \  / | |  _ \  |___ /  |  _ \           / ___|  _ \ / _ \|  _ \| |/ / ____|  _ \ 
|___ \  | |_) | | | | | | |   |_ \  | |_) |  _____  | |  _| | | | | | | |_) | ' /|  _| | |_) |
 ___) | |  __/  | | | |_| |  ___) | |  _ <  |_____| | |_| | |_| | |_| |  _ <| . \| |___|  _ < 
|____/  |_|     |_| |____/  |____/  |_| \_\          \____|____/ \___/|_| \_\_|\_\_____|_| \_\

''', 'cyan'))
from termcolor import colored
from googlesearch import search
import urllib.error

h ="""
--daterange: Return results in a specified range (requires julian dates) --link: Find pages that link to the target domain

--Inanchor: Find pages linked to with the specified anchor text/ phrase. Data is heavily sampled

--allinanchor: Find pages with all individual terms after "inanchor" in the inbound anchor text.

--inposttile: Finds pages with keywords in their post titles (i.e. for researching blogs)

--define: Pulls a card response from Google displaying the dictionary definition of the word or phrase

--cache: Returns the most up to date cache of an indexed web page

--filetype: Returns only files of a particular type associated with the keyword searched

--ext: As above, based on extension

--site: Limit results to those from one site

--related: Find similar domains to the queried domain

--intitle: Returns pages based on the searched query appearing in their title

--allintitle: Similar to intitle: but only returns titles where all the words in the title match

--inurl: Only returns results where the queried keyword(s) is present in the URL
example: python 5P1D3R-DOCKER.py -o filetype:pdf -d examole.com -n 5
"""

parser = argparse.ArgumentParser(description='Google dorking')
parser.add_argument('--operator', '-o', required=True, help=h)
parser.add_argument('--domain', '-d', required=True)
parser.add_argument('--no_of_result', '-n', required=True)
args = parser.parse_args()

operator = args.operator
domain = args.domain
num_of_result = int(args.no_of_result)
query = f'{operator} {domain}'
print(colored('search input = ' + query ,'blue'))

filename = f"{domain}.txt"
try:
    with open(filename, 'w') as file:
        for j in search(query, num=num_of_result, stop=num_of_result, pause=2):

            file.write(j + '\n')
except urllib.error.URLError:
    print(colored("Could not establish an internet connection. Please check your network connection.",'red'))

try:
    subprocess.run(['batcat', filename])
except FileNotFoundError:
    subprocess.run(['cat', filename])

