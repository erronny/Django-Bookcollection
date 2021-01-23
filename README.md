# Django-BookCollection

A Library Management System In Django runs Django Framework in back-end and HTML, CSS in front-end. The project contains all the features of a library management like login, interactive UI, issue books, Manage books, Add books to the library.

## Requirements
  ```
  alabaster==0.7.8
anyascii==0.1.7
appdirs==1.4.4
apturl==0.5.2
asgiref==3.3.1
autopep8==1.5.4
Babel==2.8.0
bcrypt==3.1.7
beautifulsoup4==4.8.2
blinker==1.4
Brlapi==0.7.0
certifi==2020.4.5.1
chardet==3.0.4
click==7.1.2
colorama==0.4.3
command-not-found==0.3
coverage==3.6
cryptography==3.0
cupshelpers==1.0
dbus-python==1.2.16
defer==1.0.6
distlib==0.3.1
distro==1.5.0
distro-info===0.23ubuntu1
dj-database-url==0.5.0
Django==3.1.5
django-ckeditor==6.0.0
django-cors-headers==3.6.0
django-filter==2.4.0
django-js-asset==1.2.2
django-modelcluster==5.1
django-taggit==1.3.0
django-treebeard==4.4
djangocms-installer==2.0.0
djangorestframework==3.12.2
docopt==0.6.2
docutils==0.16
draftjs-exporter==2.1.7
duplicity==0.8.12.0
et-xmlfile==1.0.1
fasteners==0.14.1
feedparser==5.2.1
filelock==3.0.12
future==0.18.2
gitsome==0.8.0
gTTS==2.2.1
gunicorn==20.0.4
gyp==0.1
html5lib==1.1
httplib2==0.18.1
idna==2.10
imagesize==1.2.0
importlib-metadata==1.6.0
jdcal==1.4.1
jeepney==0.4.3
Jinja2==2.11.2
joblib==1.0.0
keyring==21.3.0
l18n==2020.6.1
language-selector==0.1
launchpadlib==1.10.13
lazr.restfulclient==0.14.2
lazr.uri==1.0.5
lockfile==0.12.2
louis==3.14.0
macaroonbakery==1.3.1
Mako==1.1.2
MarkupSafe==1.1.1
monotonic==1.5
more-itertools==4.2.0
netifaces==0.10.4
nodeenv==0.13.4
numpy==1.19.4
numpydoc==1.1.0
oauthlib==3.1.0
olefile==0.46
openpyxl==3.0.6
packaging==20.4
paramiko==2.7.1
pexpect==4.6.0
Pillow==7.2.0
pipenv==11.9.0
playsound==1.2.2
ply==3.11
prompt-toolkit==3.0.6
protobuf==3.12.3
psycopg2-binary==2.8.6
PyAudio==0.2.11
pycairo==1.16.2
pycodestyle==2.6.0
pycups==2.0.1
Pygments==2.3.1
PyGObject==3.38.0
PyJWT==1.7.1
pymacaroons==0.13.0
PyNaCl==1.4.0
pyparsing==2.4.7
pyRFC3339==1.1
pyspeech==0.0.0
python-apt==2.1.3+ubuntu1.3
python-dateutil==2.8.1
python-debian==0.1.37
python-decouple==3.4
pyttsx3==2.90
pytz==2020.1
pyxdg==0.26
PyYAML==5.3.1
reportlab==3.5.47
requests==2.23.0
requests-unixsocket==0.2.0
roman==2.0.0
scikit-learn==0.24.0
scipy==1.6.0
SecretStorage==3.1.2
setproctitle==1.1.10
simplejson==3.17.0
six==1.15.0
soupsieve==2.1
SpeechRecognition==3.8.1
Sphinx==3.2.1
sqlparse==0.4.1
systemd-python==234
tablib==3.0.0
threadpoolctl==2.1.0
toml==0.10.2
tzlocal==2.1
ubuntu-advantage-tools==24.4
ubuntu-drivers-common==0.0.0
ufw==0.36
unattended-upgrades==0.1
Unidecode==1.1.2
Unipath==1.1
urllib3==1.25.9
usb-creator==0.3.7
virtualenv==20.2.2
virtualenv-clone==0.3.0
wadllib==1.3.4
wagtail==2.11.3
wcwidth==0.1.9
webencodings==0.5.1
whitenoise==5.2.0
wikipedia==1.4.0
Willow==1.4
xkit==0.0.0
xlrd==2.0.1
XlsxWriter==1.3.7
xlwt==1.3.0
xonsh==0.9.19
zipp==1.0.0

  ```

## Python Version
  Python2 and Its Supported Package PIP, Developed on python2 and Reconfigured on Python3
## Features
- Manage Books – In this feature the user can manage all the information of the books including, “add new book” , “update or modify book” and “delete book“.
- Manage Users – In this feature the admin can manage all the information of users including, “add new user” , “update or modify user” and “delete user“.
- Manage Students – In this feature the user can manage the list of the students.
- Login/Logout System – In this feature where the user can login and logout to the system.

## Operating System
Linux(Ubuntu).

## Method:
- library management – This method is the main method of the system project.
- management – In this method which is the management of the library system..
- media – This method you can found the uploading media like “photos” or other media file.
- template – This method id for the template design of the system including, “HTML“, “CSS” and etc.


## Installation
  #### Step1:- 
    Clone it.
  
  #### Step2:- 
  ```
  pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3) 
  ```
  
  #### Step3:- 
  ```
  Python3 manage.py makemigrations 
  ```
  
  #### Step4:- 
  ```
  Pyhon3 manage.py migrate 
  ```
  #### Step5:- 
  ```
  Python3 manage.py createsuperuser 
  ```
  #### Step6:- 
  ``` 
  Python3 manage.py runserver 
  ```
  ## Contributing
   Pull requests are not elligble before discuss. For major changes, please open an issue first to discuss what you would like to change.

  Please make sure to update tests as appropriate.

## License
[MIT](https://)
