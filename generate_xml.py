
# coding: utf-8

# In[3]:


import cv2
import os
from lxml import etree
import xml.etree.cElementTree as ET


# In[ ]:


def create_xml(folder,img,objects,tl,br,savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image=cv2.imread(img.path)
    height,width,depth=image.shape

    annotation=ET.Element('annotaion')
    ET.SubElement(annotation,'folder').text='folder'
    ET.SubElement(annotation,'filename').text=img.name
    ET.SubElement(annotation,'segmented').text='0'
    size=ET.SubElement(annotation,'size')
    ET.SubElement(size,'width').text=str(width)
    ET.SubElement(size,'height').text=str(height)
    ET.SubElement(size,'depth').text=str(depth)


    for obj,topl,botr in zip(objects,tl,br):
        ob=ET.SubElement(annotation,'object')
        ET.SubElement(ob,'name').text=obj
        ET.SubElement(ob,'pose').text='Unspecified'
        ET.SubElement(ob,'truncated').text='0'
        ET.SubElement(ob,'dificult').text='0'

        bbox=ET.SubElement(ob,'bndbox')
        ET.SubElement(bbox,'xmin').text=str(topl[0])
        ET.SubElement(bbox,'ymin').text=str(topl[1])
        ET.SubElement(bbox,'xmax').text=str(botr[0])
        ET.SubElement(bbox,'ymax').text=str(botr[1])

    xml_str=ET.tostring(annotation)
    root=etree.fromstring(xml_str)
    xml_str=etree.tostring(root,pretty_print=True)
    save_path=os.path.join(savedir,img.name.replace('JPG','xml'))
    with open(save_path,'wb') as temp_xml:
        temp_xml.write(xml_str)

#for testing the function

if __name__=='__main__':
    folder='images'
    img = [im for im in os.scandir('images') if '235' in im.name][0]
    objects = ['dent']
    tl = [(10, 10)]
    br = [(100, 100)]
    savedir = 'annotations'
    create_xml(folder, img, objects, tl, br, savedir)
    
    
    

