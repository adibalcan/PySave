PySave
=========

Python module for easy save in SQLite3

Requirements
=========
	sqlite3

Installation
=========
ATENTION: First install pip and git

	pip install git+git://github.com/adibalcan/PySave.git@master


Usage
=========
	import pysave

	test = {
			"textProperty":"pear", 
			"number":5.3, 
			"int":7
			}

	pysave.save(test, 'data')