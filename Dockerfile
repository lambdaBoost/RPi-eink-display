FROM python:3.9

WORKDIR /code

COPY images/ /code/images

COPY inky_display /code/inky_display

COPY ./cycle_images.py /code/

COPY ./requirements.txt /code/requirements.txt 

RUN apt-get update

RUN apt-get install  samba-common smbclient samba-common-bin smbclient  cifs-utils

RUN pip install --upgrade -r /code/requirements.txt

RUN mkdir /mnt/pi_smb

RUN mount -t cifs //192.168.1.24/public /mnt/pi_smb
