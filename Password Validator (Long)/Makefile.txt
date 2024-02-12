test:
	python3 testwe1.py
	python3 passwordvalidate.py

push:
	git commit -a
	git push

validate:
	python3 submission_validator.py

clean:
# For MacOS
	-rm .DS_Store
	-rm -r __pycache__
