
# University Faculty Directory Page Crawler

This is the course project for CS 410 Text Information Systems course at the University of Illinois at Urbana Champaign. Usage tutorial: [https://youtu.be/tN551flUyks](https://youtu.be/tN551flUyks)
  
## Overview

We were able to augment the ExpertSearch system by adding functionality which makes the system automatically crawl through faculty webpages given the primary university link/URL (illinois.edu, berkeley.edu, etc.), instead of having to explicitly identify them. Our project has two main components. First, we implemented our own classifier, which given any URL uses text classification techniques mentioned in this course to judge whether the given URL is that of a faculty directory page. Second, given a primary university link we find all directory pages associated with that primary URL. We used the classifier built in part 1 for implementing part 2.

## Team

- Srivardhan Sajja
- Navyaa Sanan

## Project Setup Instructions

Clone repository on your local machine and enter the project directory:

		git clone https://github.com/srivardhansajja/CourseProject.git
		cd CourseProject/
	
Setup a virtual environment. Executing the following two lines in a terminal will set up an environment using `venv` within the project directory.

		python3 -m venv venv
		source venv/bin/activate

We have used `Python3` for running and testing the project. Install all required packages by executing:

		python3 -m pip install -r requirements.txt

Change line 11 in `crawler/crawler_handler.py` to the python version that you are using. For example, `python`, `python3.8`, `python3`, `python3.6` or `py`

The project is now set up for you to use and test. Execute

		python3 main.py

from the primary project directory and access the locally hosted flask website by visiting http://127.0.0.1:3000/ from a browser window. You can enter university domain names and the appropriate faculty directory urls will be shown to you along with the crawling statistics.

<hr>

The program by default uses our pre-generated model. If you wish to update the parameters or tweak the model, go to `model_train/trainer.py`, make your required changes, and run

		python3 model_train/model_train.py

This will output your testing statistics, including `accuracy`, `precision`, `recall` and `F1 score`, and generate `model_testing.json`. Once you are satisfied with your changes, if you wish to use your model in the crawling process instead, replace `model_testing.json` in line 50 of `model_train/model_train.py` with `model.json` and rerun the above statement in your terminal. Be careful as this will replace our original model, and re-cloning the project is the only way to revert it, unless you make a backup of it

## Project Structure

 - Source Code:
	 - Crawler
		 - /crawler/crawler.py
		 - /crawler/crawler_handler.py
	 - Model Training
		 - /model_train/trainer.py
		 - /model_train/model_train.py
		 - /model_train/train_data.txt
		 - /model_train/dev_data.txt
	 - Model Deployment
		 - /model_deploy/model_dep.py
		 - /model_deploy/model.json
	 - Flask App
		 - /main.py
		 - /templates/
		 - /static/
 - Documentation: 
	 - ProjectProposal.pdf
	 - ProjectProgressReport.pdf
	 - ProjectDocumentation.pdf
 - README .md
	 - /

## Demo and Tutorial

We made a tutorial for ease of use of the software, and is hosted at https://youtu.be/tN551flUyks

## Model Statistics

These are the statistics of our generated model, based on training and testing data sets with 800 URLs each.

		Accuracy: 0.83875
		F1-Score: 0.8268456375838926
		Precision: 0.8927536231884058
		Recall: 0.77