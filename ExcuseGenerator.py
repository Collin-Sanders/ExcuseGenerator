#########################################################################
#########################################################################
########################### Import Dependencies #########################   
#########################################################################
######################################################################### 

try:
    # Used for GUI
    import tkinter as tk
    # Used to generate a random number
    import random
    # Used for downloading files from GitHub
    import urllib.request
    # Used for renaming and deleting old files
    import os
    # Used to compare files and convert formats
    from datetime import datetime
    # Used to create nifty log file
    import logging
except:
    logging.info("module import failed")
    
try:
    with open("ExcuseFile.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
finally:        
    file.close

# Set up logging
logging.basicConfig(filename="ExcuseGenerator.log", level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s')

#########################################################################
#########################################################################
########################### Gui Setup ###################################   
#########################################################################
#########################################################################     
# Create a window    
window = tk.Tk()
# Set the window size
window.geometry("500x200")
# Define window title
window.title("Excuse Generator")
# Set the background color
window.configure(bg="black")
logging.info("Window created")

# Configure resizeable objects
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)


# Create excuse title
title = tk.Label(text="Excuse:",font=(25), bg = "black", fg = "white")
#  Place title in window
title.grid(row=0,column=0,columnspan=2, sticky=tk.NW)

# Create excuse
excuse = tk.Label(text="",font=(50), wraplength=500, anchor = tk.CENTER, justify = tk.CENTER, bg = "black", fg = "white")
#Place excuse in window
excuse.grid(row=1,column=0,columnspan=2,pady=25) 

logging.info("Created labels")   
    
    
    
#########################################################################
#########################################################################
########################### Definitions #################################   
#########################################################################
#########################################################################   

def ReadUpdatedExcuses():
    try:
        with open("ExcuseFileTest.txt") as file:
            linesTest = file.readlines()
            linesTest = [line.rstrip() for line in linesTest]
            logging.info("Number of lines in test file: " & len(linesTest))
    finally:        
        file.close
    return linesTest    
 
    
def ExcuseGenerator():
    number = random.randint(1, (len(lines) - 3))
    excuse.config(text = lines[number])
    logging.info("Number of lines in excuse file: " & len(lines))
    
    
def ExcuseCheck():
    # Get time stamp from current excuse file
    timeStamp = lines[len(lines)-1]
    logging.info("Current excuses timestamp: " & timeStamp)
    
    # GitHub URL for latest excuse file
    url = "https://raw.githubusercontent.com/Collin-Sanders/ExcuseGenerator/main/ExcuseFile.txt"
    logging.info(url)
    
    # Download latest file from GitHub
    filename, headers = urllib.request.urlretrieve(url, filename="ExcuseFileTest.txt")
    logging.info("File downloaded from GitHub successfully")
    
    # Get lines from excuse file on GitHub
    linesTest = ReadUpdatedExcuses()
    
    # Get time stamp from excuse file on GitHub
    timeStamp2 = linesTest[len(lines)-1]
    logging.info("GitHub excuses timestamp: " & timeStamp2)
    
    # Convert string times to time objects
    t1 = datetime.strptime(timeStamp, "%m/%d/%Y %I:%M%S%p")
    t2 = datetime.strptime(timeStamp2, "%m/%d/%Y %I:%M%S%p")
    
    # Determine which time is the latest
    latest = max((t1, t2))
    logging.info("Latest timestamp " & str(latest))
    
    # Compare and remove the oldest file
    if t1 == t2:
        os.remove("ExcuseFileTest.txt")
        logging.info("File is already the latest file")
    elif latest == t2:
        os.remove("ExcuseFile.txt")
        print("Removing")
        os.rename("ExcuseFileTest.txt", "ExcuseFile.txt")
        logging.info("File was updated")
        
        
    
    
    
    
    
    
    
#########################################################################
#########################################################################
########################### Gui Setup ###################################   
#########################################################################
######################################################################### 
    
# Create button to generate excuse
generateExcuse = tk.Button(text="Generate Excuse", command = ExcuseGenerator, height = 5, width = 34)
# Place generate button in window
generateExcuse.grid(row=2, column=0, sticky=tk.SW)
logging.info("Generate button populated")


# Create button to check for new list of excuses
checkForNewExcuses = tk.Button(text="Check for new excuses", command = ExcuseCheck, height = 5, width = 34)
# Place check button in window
checkForNewExcuses.grid(row=2, column=1,sticky=tk.SE)
logging.info("Check button populated")

# Populate
window.mainloop()


