# Talk2YourComputer


The code in this repository gives you opportunity to communicate by talking and with simple mouse clicks without interacting with the keyboard too much

```
pip install -r requirements.txt (note inside the python env you can use pip not pip3)

python talkintocomputer.py
```


0) Choose the text area

1) Takes the picture

2) Reads to you

3) Takes your input (your voice)

4) Generates text 

5) Choose the input location

6) Inputs the text and presses ENTER for you

This project is build on python3.11.1 and Ubuntu 20.04 (I recomment you to use virtualenv)
it uses pygame and tkinter in order to install the tkinter code below can be used


```pip install pygame --pre```

``` sudo apt-get install python3-tk python3-dev```

specifically

```sudo apt-get install python3.11-tk python3-dev``` 

### other libraries I have downloaded 

```sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn```

#when I was trying to download the pyaudio
```
sudo apt-get install portaudio19-dev

sudo apt-get install libjack-jackd2-dev portaudio19-dev

sudo apt-get install libportaudio2
```

## Make a virtualenv
```
sudo apt-get install python3-pip

sudo pip3 install virtualenv 

python3.11 -m venv EnvName

source EnvName/bin/activate
```
if you had a problem while building the environment it can be related to python3.11 libraries, 
search and download necessary ones then it will fine


## Future TODOS
make a loop for not changing locations

show chosen area in gray pictures

design a UI

then maybe change the voice 

add eye tracking to completely avoid mouse and clickings


