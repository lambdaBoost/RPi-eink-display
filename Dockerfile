FROM python:3.9 

WORKDIR /code

COPY images/ /code/images

COPY inky_display /code/inky_display

COPY ./cycle_images.py /code/

COPY ./requirements.txt /code/requirements.txt

# RUN apt-get install ca-certificates

# RUN wget https://packages.ntop.org/apt-stable/bullseye/all/apt-ntop-stable.deb

# RUN apt install ./apt-ntop-stable.deb

RUN apt -y upgrade

RUN apt -y update

RUN apt install -y --no-install-recommends samba-common-bin samba

RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/*

#RUN apt install -y python3-pip

RUN pip install --upgrade -r /code/requirements.txt

RUN mkdir /mnt/pi_smb

RUN mount -t cifs //192.168.1.24/public /mnt/pi_smb
