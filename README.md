<h1 align="center">Emscrape</h1>

<p align ="center"><b>Web scraping utility designed for max scrape, min hassle!</b></p>

---

## Getting Started

The only prerequisite is a working installation of Python so feel free to skip the below steps if you already have Python installed on your system. There are a number of ways you can install Python, the below is my personal preference but of course feel free to install Python on your machine in any manner you prefer.

## Windows

Use the keyboard shortcut `WIN` + `X` followed by `I` to open powershell then copy and paste the following commands to get up and running.

> Note: You may need to close and reopen your terminal after installing miniconda.<br>Note: When the installer asks if you wish to initialize Miniconda3 **select yes**.

```sh
cd ~/Downloads/
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe --output miniconda.exe
./miniconda.exe
conda create -n emscrape python=3.9.7
conda activate emscrape
git clone https://github.com/jodisfields/emscrape.git
cd emscrape
pip install -r requirements.txt
python emscrape.py
```

## Mac / Linux

I have NOT personally tested this on a Mac however as it is a Unix based operating system at its core I dont expect any issues. So if you're on a Mac press `Command` + `Space Bar`, type in `Terminal` and then open the application. Once you have the terminal open, copy and paste the following commands to get up and running.

> Note: You may need to close and reopen your terminal after installing miniconda.<br>Note: When the installer asks if you wish to initialize Miniconda3 **select yes**.

```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
conda create -n emscrape python=3.9.7
conda activate emscrape
git clone https://github.com/jodisfields/emscrape.git
cd emscrape
pip install -r requirements.txt
python emscrape.py
```

## Usage

https://user-images.githubusercontent.com/46502355/201368804-85b69446-f18e-4590-a688-2fc5c323cec4.mp4
