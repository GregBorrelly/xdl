#!/usr/bin/env
"""
This script takes a list of Youtube URLS and proceeds to download the videos 
It finds or creates a directory to place the files in them.

This script is more of an add-on to youtube-dl.

Dependencies: 
youtube-dl 
python-pip 

If your new to programming and are using linux, install python-pip
and then install youtube-dl. 

Contact me: gregborrelly@gmail.com 
"""



import os
import sys
import feedparser

flag = len(sys.argv)

if flag == 1: 
    print("Please Specify Options.")

podcast_list = ['http://feeds.feedburner.com/ALLJupiterVideos']


def identify_directory():
    """Finds or Creates a directory and goes into it  -_- """
    #Set up Video Directory
    print("Hint: Type Directory Name to be created.")
    directory = input("\nDirectory: ")
    
    if os.path.exists(directory):
        os.chdir(directory)

    else:
        os.mkdir(directory)
        os.chdir(directory)

def download_playlist():
    """ Utilizes youtube-dl to download an entire playlist """
    url = input("Url: ")
    os.system("youtube-dl -cit %s"%url)

def get_podcasts(url):
    feed = feedparser.parse(url)
    podcasts = {}
    podcast_titles = {} 
    current_path = str(os.getcwd())
    
    for podcast in range(0,10):
        podcasts[podcast] = feed['entries'][podcast]['link']
        
        #This creates the Path to test, wherever files have alredy been downloaded.  
        podcast_titles[podcast] = current_path + feed['entries'][podcast]['title']
    
    for podcast in range(0,10):
        if os.path.isfile(podcast_titles[podcast])
            pass 
        else:
            os.system("youtube-dl %s"%podcasts[podcast])

if sys.argv[1] == '-p':
    download_playlist()

elif sys.argv[1] == '-up':
    for podcast in podcast_list:
        get_podcasts(podcast)

elif sys.argv[1] == '-l':
    counter = 1 
    print("\nHINT: Leave Area blank and Press ENTER  to begin downloading process.\n")
    url = input(str(counter) + ". url: ")

    if url == "":
        print("\nError Blank URL")
        os.system("exit")

        urls= [] 

        while url != "":
            urls.append(str(url))
            counter += 1 
            url = input(str(counter) + ". url: ")

        for url in urls:
            os.system("youtube-dl %s"%url)

else:
    print("Need Flags")
