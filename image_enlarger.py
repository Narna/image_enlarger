### PYTHON 3.4 PROGRAM TO ENLARGE IMAGES ###
### THE PROGRAM ONLY WORKS IF IT IS IN THE SAME FOLDER AS THE IMAGES YOU WISH TO ENLARGE ###


# IMPORTS #
import PIL
from PIL import Image
import os

# FUNCTIONS #
def setup():
    '''
    FUNCTION TO REQUEST AND VALIDATE USER INPUT TO RETURN THE SCALE FACTOR AND FOLDER PATH.
    INPUTS: NONE
    OUTPUTS: SF, PATH
    
    '''
    
    ### SETTING SCALE FACTOR ###
    while True: 
        try:
            sf = int(input("Scale Factor >> "))
            if sf > 0:
                break
            else:
                print("Scale factor must be an integer above 0. ")
        except ValueError:
            print("Scale factor must be an integer above 0. ")
    
    ### SETTING FOLDER PATH ###
    while True:
        try:
            path = input("Folder path >> ")
            
            if os.path.exists(path) == True:
                listing = os.listdir(path)
                found = False

                for file in listing:
                    if file == 'image_enlarger.py':
                        found = True
                if found == True:
                    break
                else:
                    print("Path must be existing and input like the following: ")
                    print("C:/Users/Hannah/Documents/Computer Science/resizer/Year 7 photos")                    
                
            else:
                print("Path must be existing and input like the following: ")
                print("C:/Users/Hannah/Documents/Computer Science/resizer/Year 7 photos")
        except ValueError:
            print("Path must be existing and input like the following: ")
            print("C:/Users/Hannah/Documents/Computer Science/resizer/Year 7 photos")
            
    return sf, path
    
def enlarge(sf, path):
    '''
    FUNCTION TO ENLARGEN ALL THE IMAGES IN A SPECIFIED FOLDER BY A SPECIFIED SCALE FACTOR.
    INPUTS: SF, PATH
    OUTPUTS: NONE
    
    '''
    
    listing = os.listdir(path) ### CREATES A LIST OF ALL OF THE FILE NAMES ###
    
    for file_name in listing:
        if file_name != 'image_enlarger.py' and file_name != 'Thumb.db': ### ENSURES THAT THE PROGRAM IS NOT TAKEN AS INPUT ###
            
            original = Image.open(file_name) ### OPENS IMAGE SO THE PROGRAM HAS ACCESS TO IT ###
            
            new_width = original.size[0] * sf ### MULTIPLIES ORIGINAL DIMENSIONS BY SCALE FACTOR TO GIVE NEW DIMENSIONS ###
            new_height = original.size[1] * sf
            
            v2 = original.resize((new_width, new_height), PIL.Image.ANTIALIAS) ### RESIZES IMAGE, KEEPING THE PROPORTIONS THE SAME ###
            v2.save(file_name) ### SAVES IMAGE UNDER THE SAME FILE NAME ###
        else:
            continue ### ALLOWS THE PROGRAM AND ANY THUMBNAIL CACHES TO BE SKIPPED ###
        
        
# RUN #
sf, path = setup()
enlarge(sf, path)
print("Success. ")