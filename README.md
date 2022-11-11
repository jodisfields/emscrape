<center>

# Emscrape

**Web scraping utility designed for max scrape, min hassle**

</center>

## Getting Started

There are a number of ways you can install Python on your machine, the below is my personal preference so feel free to install Python on your machine in any manner you prefer. Open a terminal and type in the following commands to install Python on your machine.

> Note: You may need to close and reopen your terminal after installing miniconda to ensure that the conda command is available.

### Windows

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

> Note: The installer prompts “Do you wish the installer to initialize Miniconda3 by running conda init?” Make sure you select **yes**.

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
python emscrape.py
```
