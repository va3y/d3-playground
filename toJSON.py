import json
import csv

with open('./deputies.dsv', "r") as text:
    text = ''.join([i for i in text]).replace("\'", "&")
    text = ''.join([i for i in text]).replace("\"", "")
    text = ''.join([i for i in text]).replace("&", "\"")
    x = open("output.dsv", "w")
    x.writelines(text)
    x.close()
