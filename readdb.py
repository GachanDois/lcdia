import pandas as pd
import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.dom import minidom
import numpy as np
import lxml
from lxml import objectify
import io


xml_data = open('full_db.xml', 'r',encoding="utf8").read()  # Read file
root = ET.XML(xml_data)  # Parse XML
with open("full_db.xml") as fp:
    soup = BeautifulSoup(fp, 'xml')
h = soup.find_all('product')

data = []
cols = []

for ix, child in enumerate(h):
    try:
        data.append([subchild.text for subchild in child])
        cols.append(child.tag)
        print(cols)
    except:
        data = None
    

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
df


