FROM debian:10 

RUN apt-get update && apt-get install -y apt-utils
RUN apt-get install -y openssh-server vim 
RUN mkdir /var/run/sshd
RUN apt-get install adduser
RUN echo 'root:rock' | chpasswd
RUN echo "alias ll='ls -la'" >> /root/.bashrc
RUN echo "alias cl='clear'" >> /root/.bashrc
RUN adduser --quiet --disabled-password --shell /bin/bash --home /home/rock --gecos "User" rock
RUN echo "rock:rock" | chpasswd 
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN echo "alias ll='ls -la'" >> /home/rock/.bashrc
RUN echo "alias cl='clear'" >> /home/rock/.bashrc
# SSH login fix. Otherwise user is kicked off after login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install colorlog 
ENV NOTVISIBLE="in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
