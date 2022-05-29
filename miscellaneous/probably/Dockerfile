FROM python:3


# Install other dependencies
RUN apt-get update && apt-get upgrade && apt-get install -y \
  xinetd \
  && rm -rf /var/lib/apt/lists/*

# Configure xinetd
RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf


# Create user
RUN useradd -M -d /ctf ctf
USER ctf
WORKDIR /ctf


# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy files
COPY ./src /ctf/


ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 40000