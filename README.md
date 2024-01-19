# Selenium-Python-Example

This repository contains the base setup of an UI testing project,
using Python, Selenium Webdriver and Page Object Model pattern.

A simple search in DuckDuckGo to check that results are displayed is used as example

# Requirements

* Python 3.12.X (najlepiej zainstalowany globalni, dla wszystkich uzytkownikow, i zaznaczyć dodanie py.exe )
* pip and setuptools   
  - python.exe -m pip install --upgrade pip setuptools
  - pip install --upgrade pip setuptools
  
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Instalation

1. Download or clone the repository: https://github.com/slawomirslowik/selenium-python-example
2. Go to the project root directory "/selenium-python-example/".
3. Open a terminal
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal on project root directory 
2. Run: `pytest -v --html=results/TWOJA_NAZWA_RAPORTU.html`

# Configuration

/data/config.yaml 

# Results

'/results/TWOJA_NAZWA_RAPORTU.html'

# Links
   
   [Selenium - Python Documentation](<https://selenium-python.readthedocs.io/>)
   
   [Webdriver Manager for Python](<https://github.com/SergeyPirogov/webdriver_manager>)
   
   