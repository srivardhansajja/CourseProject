# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.
 
# Project Setup Instructions

Clone repository on your local machine and enter the project directory:

	    git clone https://github.com/srivardhansajja/CourseProject.git
	    cd CourseProject/


Setup a virtual environment. Executing the following two lines in a terminal will set up an environment using `venv` within the project directory.

		python3 -m venv venv
		source venv/bin/activate

We have used `Python3` for running and testing the project. Install all required packages by executing:

		python3 -m pip install -r requirements.txt
	
Change line 11 in `crawler/crawler_handler.py` to the python version that you are using. For example, `python3.8`, `python3`, `python3.6` or `py`
The project is now set up for you to use and test. Execute

		python3 main.py

from the primary project directory and access the locally hosted flask website by visiting http://127.0.0.1:3000/ from a browser window. You can enter university domain names and the appropriate faculty directory urls will be shown to you along with the crawling statistics.

<hr>

The program by default uses our pre-generated model. If you wish to update the parameters or tweak the model, go to `model_train/trainer.py`, make your required changes, and run

		python3 model_train/model_train.py

This will output your testing statistics, including `accuracy`, `precision`, `recall` and `F1 score`, and generate `model_testing.json`. Once you are satisfied with your changes, if you wish to use your model in the crawling process instead, replace `model_testing.json` in line 50 of `model_train/model_train.py` with `model.json` and rerun the above statement in your terminal. Be careful as this will replace our original model, and re-cloning the project is the only way to revert it, unless you make a backup of it