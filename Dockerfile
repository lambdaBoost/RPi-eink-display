FROM python:3.9 

WORKDIR /code

COPY images/ /code/images

COPY inky_display /code/inky_display

COPY ./cycle_images.py /code/

COPY ./requirements.txt /code/requirements.txt

RUN apt -y upgrade

RUN apt -y update

RUN apt install -y --no-install-recommends samba-common-bin samba

RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/*

RUN pip3 install --upgrade -r /code/requirements.txt

CMD ["python3", "cycle_images.py"]
