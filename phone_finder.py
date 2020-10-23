#https://vestertraining.com/etiqueta/ciberseguridad/
# -*- CREATED BY: DtxdF -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-

from json import *
import json 
import requests
from colorama import init, Fore
from time import sleep



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def banner():

    print( bcolors.WARNING +("""
    
 /$$$$$$$  /$$                                             /$$$$$$$$ /$$                 /$$  /$$$$$$           
| $$__  $$| $$                                            | $$_____/|__/                | $$ /$$__  $$          
| $$  \ $$| $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$         | $$       /$$ /$$$$$$$   /$$$$$$$|__/  \ $$  /$$$$$$ 
| $$$$$$$/| $$__  $$ /$$__  $$| $$__  $$ /$$__  $$ /$$$$$$| $$$$$   | $$| $$__  $$ /$$__  $$   /$$$$$/ /$$__  $$
| $$____/ | $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$|______/| $$__/   | $$| $$  \ $$| $$  | $$  |___  $$| $$  \__/
| $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/        | $$      | $$| $$  | $$| $$  | $$ /$$  \ $$| $$      
| $$      | $$  | $$|  $$$$$$/| $$  | $$|  $$$$$$$        | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$/| $$      
|__/      |__/  |__/ \______/ |__/  |__/ \_______/        |__/      |__/|__/  |__/ \_______/ \______/ |__/                                                                                                                                                                                                                                                                                                                                                      
                             ----[Phone-Finder Admin Panel Finder]----
                                       ---[By  Rubickcuv]---
-----------------------------------------------------------------------------
 """) + bcolors.OKGREEN  + ("""Ejemplo: Phone-Finder >> 100-100-100
-----------------------------------------------------------------------------""") + bcolors.OKBLUE)



def error_msg(msg):
	print ("\n")
	print (color.error+color.red+"Error {0} not found".format(msg)+color.reset)

def check_connection(phone_number):
    access_key  = 'b143e99cdfc4bf3355a824b8b0fca756'
    url ="http://apilayer.net/api/validate?access_key="+ access_key + '&number=' + phone_number+"&country_code=MX&format=1"
    code_error = "Apparently you are not connected to the internet, The answer was not positive:"
	
    res =requests.get(url)
    api_json_res = json.loads(res.content)
    return api_json_res






if __name__ == "__main__":

    parametros = 'valid,number,local_format,international_format,country_prefix,country_code,country_name,location,carrier,line_type'

    banner()
    phone_number = input(bcolors.WARNING+"[*]Phone-Finder >> ")
    json_data =check_connection(phone_number)
    par = parametros.split(",")

    
    




