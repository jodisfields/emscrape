<h1 align="center"><u>Emscrape</u></h1>

<p align ="center"><b>Web scraping utility designed for max scrape, min hassle</b></p>

## Getting Started

There are a number of ways you can install Python on your machine, the below is my personal preference but feel free to install Python on your machine in any manner you prefer.

### Windows

Use the keyboard shortcut `WIN` + `X` followed by `I` to open powershell and run the following commands.

> Note: You may need to close and reopen your terminal after installing miniconda.

```sh
cd ~/Downloads/
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe --output miniconda.exe
./miniconda.exe
conda create -n emscrape python=3.9.7
conda activate emscrape
git clone https://github.com/jodisfields/emscrape.git
cd emscrape
pip install -r requirements.txt
```

### Mac

I havent tested this on an actual Mac, but it should work the same as a Linux machine as they are both Unix based. So if you're on a Mac, open the terminal application and run the following commands.

> Note: When the installer asks if you wish to initialize Miniconda3 **select yes**.

```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
conda create -n emscrape python=3.9.7
conda activate emscrape
git clone https://github.com/jodisfields/emscrape.git
cd emscrape
pip install -r requirements.txt
```

## Usage

```sh
conda activate emscrape
python emscrape.py
```

https://user-images.githubusercontent.com/46502355/201368804-85b69446-f18e-4590-a688-2fc5c323cec4.mp4
