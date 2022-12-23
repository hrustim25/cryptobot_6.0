FROM python:3-onbuild

RUN mkdir -p /usr/src/cryptobot_6_0
WORKDIR /usr/src/cryptobot_6_0

COPY . /usr/src/cryptobot_6_0/

RUN pip install -r requirements.txt

CMD ["python3", "cryptobot_6_0.py"]
# CMD ["./launch.sh"]
# CMD ["./setup.sh"]