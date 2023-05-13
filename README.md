<h1 align="center">
    <a href="https://github.com/Untouchable17/Meta-DataWipe">
        <img src="https://i.ibb.co/4pTBvX8/zxvvzxzvx.png" width="700">
    </a>
</h1>

<p align="center">
<a href="https://github.com/Untouchable17/Meta-DataWipe"><img src="https://img.shields.io/static/v1?label=version&message=4.0.0&color=green"></a>
<a href="https://github.com/Untouchable17/Meta-DataWipe/issues?q=is:issue+is:closed"><img src="https://img.shields.io/github/issues-closed/Untouchable17/Meta-DataWipe?color=orange"></a>
</p>

<h1 align="center">Meta DataWipe</h1>

<b>DataWipe </b>- Python library that allows you to safely read and remove metadata from various file types, including images, videos, audio, and documents. Metadata such as EXIF data, GPS coordinates, creation, copyright and others, an organization providing confidential information whose user does not want to be disclosed. DataWipe allows you to prevent the removal of metadata from files in order to ensure the possibility of leakage of confidential information and user privacy. MetaCleaner has a clean and simple interface that makes it quick and easy to use in your Python projects.

<h2 align="center">Installation</h2>

<p align="center">Installing and using program process:</p>

<p align="center">Execute all commands on behalf of the superuser</p>

Downloading or cloning this GitHub repository.
```
git clone https://github.com/Untouchable17/Meta-DataWipe
```
<b>Windows</b>: You need to install ffmpeg and exiftool programs
```
- https://exiftool.org/install.html
- https://ffmpeg.org/download.html
```
Create and activate python virtual env
```
python3 -m venv venv
source venv/bin/activate
```
Install all requirements
```
pip3 install -r requirements.txt
```
```
chmod +x DataWiper.py
```
<br>You can add the correct path to global like this: `export PATH="$PATH:$(pwd)"` and then you can run the program by just entering their name

<h2 align="center">How to use</h2>

```
usage: DataWiper.py [-h] [-r READ] [-d DELETE] [-t {media,document,image}]

Get metadata for a file

optional arguments:
  -h, --help            show this help message and exit
  -r READ, --read READ  Option to read metadata
  -d DELETE, --delete DELETE
                        Option to remove metadata
  -t {media,document,image}, --type {media,document,image}
                        Option to specify file type
```


<h2 align="center">Contact Developer</h2>


    Telegram:           @secdet17
    Group:              t.me/secdet_team
    Email:              tylerblackout17@gmail.com

