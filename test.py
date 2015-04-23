import pysave

test = {
		"textProperty":"pear", 
		"number":5.3, 
		"int":7
		}

pysave.save(test, 'data')