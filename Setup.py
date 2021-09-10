import setuptools

with open('README.md','r') as File:
	long_description=File.read()



setuptools.setup(

	name='Preprocess_text_file_Pranav',
	author='Pranav Kashyap',
	version='0.0.1',
	description='This is for PreProcessing of text data for NLP',
	author_email='pranavkshp9@gmail.com',
	packages=setuptools.find_packages(),
	classifiers=[
		'Programming Language::Python ::3',
		'License:: OSI Approved :: MIT License',
		'Operating System:: OS Independent'],
		python_requires='=>3.6'

	)