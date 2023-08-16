FROM debian:11

RUN apt update
RUN apt-get install python3.6
RUN apt install python3-pip -y
RUN pip install jupyter -U 
RUN pip install jupyterlab 

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]