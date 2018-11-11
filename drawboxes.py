
# coding: utf-8

# In[2]:


import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import create_xml

# In[17]:


img=None
tl_list=[]
br_list=[]
object_list=[]

image_folder='images'
savedir='annotations'
obj=['dent','Scratch_or_spot']



def insert(event):
    if event.key=='d':
        object_list.append(obj[0])
    elif event.key=='a':
        object_list.append(obj[1])

def line_select_callback(clk,rls):
    
    global tl_list
    global br_list
    global object_list
    tl_list.append((int(clk.xdata),int(clk.ydata)))
    br_list.append((int(rls.xdata),int(rls.ydata)))
    
def toggle_selector(event):
    toggle_selector.RS.set_active(True)

#
    
    
def onkeypress(event):
    global tl_list
    global br_list
    global object_list
    global img
    if event.key=='q':
        create_xml(image_folder,img,object_list,tl_list,br_list,savedir)
        img=None
        print(tl_list,br_list,object_list)
        tl_list=[]
        br_list=[]
        object_list=[]
        #plt.close()
    

if __name__=='__main__':
    for n,image_file in enumerate(os.scandir(image_folder)):
        img=image_file
        fig,ax=plt.subplots(1)
        image=cv2.imread(image_file.path)
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        #mngr=plt.get_current_fig_manager()
        #mngr.window.setGeometry(250,120,1280,1024)
        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )
        ax.imshow(image)
        plt.connect('key_press_event',toggle_selector)
        plt.connect('key_press_event',onkeypress)
        plt.connect('key_press_event',insert)

        plt.show()


