# Trumpers [![python](https://img.shields.io/badge/Python-3.0-green.svg?style=style=flat-square)](https://www.python.org/downloads/) ![version](https://img.shields.io/badge/Build-Final-blue.svg) ![license](https://img.shields.io/badge/License-MIT-orange.svg?style=style=flat-square)

Python script that unfollows anyone you're following if they follow @realDonaldTrump

<a href="https://asciinema.org/a/4QPO3MADJcx0Tf655BccSjS8E" target="_blank"><img src="https://asciinema.org/a/4QPO3MADJcx0Tf655BccSjS8E.png" /></a>

Made with ![heart](https://cloud.githubusercontent.com/assets/4301109/16754758/82e3a63c-4813-11e6-9430-6015d98aeaab.png) by <a href=https://rgllm.com>rgllm</a>

## Features
- Gets Twitter User IDs from people you're following
- Sees if they follow @realDonaldTrump
- Unfollow them if True

## Usage
Trumpers should work on all Linux distros running Python > 2.7
First, clone it by entering the following command in the terminal
``` bash
git clone https://github.com/rgllm/Trumpers.git
```
Now navigate to Trumpers directory
``` bash
cd Trumpers
```
Now install the requirements with the following command
``` bash
pip install -r requirements.txt
```
Edit Trumpers.py and put your Twitter app keys
``` bash
APP_KEY ='XxXxXxxXXXxxxxXXXxXX'
APP_SECRET ='XxXxXxxXXXxxxxXXXxXX'
OAUTH_TOKEN='XxXxXxxXXXxxxxXXXxXX'
OAUTH_TOKEN_SECRET='XxXxXxxXXXxxxxXXXxXX'
YOUR_ACCOUNT_NAME = 'XxXx'
```
Now you can run Trumpers
``` bash
python Trumpers.py
```