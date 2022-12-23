# Cryptobot_6.0
Simple telegram bot with jokes about crypto

# Launch
Bot requires file 'config.py' containing field TOKEN with your bot token. If you don't have one, it can be acquired via @BotFather bot.

## Launch in Python VM
To start application first time write
```
source setup.sh
```
Next times you can use
```
source launch.sh
```
## Launch in Docker
Preparations:
```
sudo apt-get install docker, docker-compose
```
Login into your Docker account. Next inside the working directory:
```
docker-compose build
docker run -d <your-username>/first-telegram-bot
```
