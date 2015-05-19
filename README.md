# Amaru [![Build Status](https://travis-ci.org/centaurialpha/amaru.svg?branch=master)](https://travis-ci.org/centaurialpha/amaru)

**Amaru** is a modern code editor for programmers, built with *Python* and *Qt*, it is designed to be as customizable as possible.

## Screenshot

![screenshot](https://github.com/centaurialpha/edis/blob/gh-pages/img/amaru-screenshot.png)

## Platforms
- GNU/Linux
- Windows
- Mac OS X

## Running

### Requirements
* [Python 3.x](https://www.python.org/downloads/release/)
* [PyQt5](http://www.riverbankcomputing.co.uk/software/pyqt/download5)
* [Qscintilla](http://www.riverbankcomputing.com/software/qscintilla/download)

#### Debian/Ubuntu
```bash
sudo apt-get install python3-pyqt5 python3-pyqt5.qsci
```
#### Arch/Manjaro
```bash
sudo pacman -S python-pyqt5 python-qscintilla-qt5
```

Clone the repository and running:
```bash
git clone https://github.com/centaurialpha/amaru.git
cd amaru
python bin/amaru
```