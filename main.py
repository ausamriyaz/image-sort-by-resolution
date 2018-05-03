
from PIL import Image


import os
def sort():
    current_directory = os.getcwd()

    Path = os.path.join(current_directory + '/new folder/')
    filelist = os.listdir(Path)
    x=[]
    for i in filelist:
        with Image.open(Path+i) as img:
            width, height = img.size
            x.append(str(width)+"x"+str(height))

    uniquelist = list(set(x))

    for u in uniquelist:

        final_directory = os.path.join(current_directory + '/new folder/', r''+u)
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)


    for i in filelist:
        width=0
        height=0
        with Image.open(Path+i) as img:
            width, height = img.size
            img.close()
        os.rename(Path+i, Path+str(width)+"x"+str(height)+"/"+i)


