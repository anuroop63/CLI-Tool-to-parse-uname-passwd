# Password Parsing
The project aims to parse the UNIX "/etc/passwd" and "/etc/group" files and combine the data into a single json output.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Python 3.x

## Running the test case
To run a test case using provided sample input files, run below command in project directory.
	"python3 passwd-parser.py -p ./passwd -g ./group"		(Output printed on terminal)

## Deployment
To deploy the code manually, use below commands in project directory:
1. Using custom test files: (Output stored in out.log)
	"./script.sh /absolute/path/to/passwd /absolute/path/to/group"
2. To run project on default Unix system files, simply run below:
	"./script.sh"

To configure cronjobs for the code, add below commands to cronjobs list with the correct file paths to files: (Output stored in out.log)
1. Using custom test files:
	"*/60 * * * * /Users/Desktop/code/script.sh /absolute/path/to/passwd /absolute/path/to/group"		(Runs every 60 minutes)
2. To run project on default Unix system files, simply run below:
	"*/60 * * * * /Users/Desktop/code/script.sh"						(Runs every 60 minutes)


## File Descriptions
1. script.sh - Execution file to run the project and use for cronjob also.
2. passwd-parser.py - File containing the complete python code for the project.
3. group - Sample test file, similar to /etc/group file of Unix system.
4. passwd - Sample test file, similar to /etc/passwd file of Unix system.

## Note
Keep the 'script.sh' and 'passwd-parser.py' in the same directory.

## Authors
* **Anuroop Katiyar**

## Acknowledgments
* Some default code snippets referred from stackoverflow.com
* https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/
* https://www.cyberciti.biz/faq/understanding-etcgroup-file/