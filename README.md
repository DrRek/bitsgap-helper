INSTALL:

make sure you've installed geckdriver
Pacman:
	sudo pacman -S geckodriver

git clone git@github.com:DrRek/bitsgap-helper.git
cd bitsgap-helper
pip install -r requirements.txt

you could also to this inside a virtualenv


RUN:

./src/main.py

do not use Firefox insted of Chrome, the login process will most likely fail
