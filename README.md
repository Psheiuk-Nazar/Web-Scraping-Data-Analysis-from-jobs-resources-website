# Web Scraping & Data Analysis from jobs resources website

## Overview

This Python program is designed to perform word frequency analysis on serialized dictionaries, and then visualize the top 25 most frequent words using a bar chart. 
The program uses popular libraries, including `ast`, `pandas`, and `matplotlib`, to accomplish this task.
The program was created to analyze the Djinni site, namely the Python development section. At the end of the program, you will receive a bar with the most popular technologies

## Prerequisites

Before running the program, make sure you have the following dependencies installed:

- Python 3.x
- `ast` library (no additional installation required, it's part of the Python standard library)
- `pandas`: You can install it using `pip install pandas`.
- `matplotlib`: You can install it using `pip install matplotlib`.

## Structure

1. jobwebsite - folder - Inside of this folder is a program for scraping Djinni website. In fields words we take a serializer dict with count of words in description uses function _select_words
2. jobs.csv - file with table which have main information about python vacancies
3. jobs_analysis.ipynb - This file analysis main words in vacancies description and build bar chart with main technology 
4. bad_words.py - This file has a class with words which not use in analysis

## Usage

1. Clone or download this repository to your local machine.

2. Make sure you have your data (in this case, serialized dictionaries) ready or modify the program to read data from a source.

3. Open a terminal or command prompt and navigate to the project directory.

4. pip install requirements.txt 

5. Run the Python script:

   ```bash
   scrapy crawl python_jobs -O jobs.csv

6. Open jobs_analysis.ipynb file

7. Run all 


![25 main technologies in python.png](25%20main%20technologies%20in%20python.png)
