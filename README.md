# Log_Parser

A log management system must first parse the files to extract meaningful information from logs. Log parsing translates structured or unstructured log files so your log management system can read, index, and store their data. This way, you can easily filter, analyze, and manipulate the key-value information.

One of the most commonly used structured data formats is JSON. It’s the first choice for many application developers because its Unicode encoding makes it universally accessible and readable by humans and machines alike. The snippet below shows a simple JSON document with key-value pairs as elements.

## How Does a Log Parser Work?
Usually, log parsers are built into the log management software’s engine. This means each log manager will have its proprietary method for parsing logs.

Most log management solutions have built-in parsers for common data types like Windows Event Logs, JSON, CSV, or W3C. Parsers are configured to recognize these log types based on the source data structure and file extensions.

Once a log file is ingested, the parser applies its built-in rules to extract useful field names and their values. Sometimes, a parser can store the extracted data in a hierarchical structure. With this approach, the user can search on any field and drill down through the returned result set to fine-tune the query.

For non-standard log types, users can provide custom log parsing rules. Typically this is done using regular expressions or the logging solution’s proprietary language. Some log management solutions make it even easier by letting users build the parsing rule from a graphical interface. Users can highlight the field names they are interested in; meanwhile, behind the scenes, the log management solution builds the parsing rule.

Once logs are parsed, the logging system will ingest the data so users can query, analyze, and visualize it.

## What Log Parsing Features to Look For

Log parsing features should be one of the key areas to consider when you are assessing a log management solution. It’s important to get your logs ingested and parsed as quickly and easily as possible so you can spend more of your time analyzing them.

### Automation: 
Make sure the tool you choose comes with automatic parsers for the most common log formats. For custom logs, you should be able to perform a full-text search on the raw data before writing custom parsing rules.

### Customization:
Logs come in so many formats that it would be impossible for any log management system to support them all by default. That’s why creating your parsing configuration must be easy and intuitive. Some logging tools provide a GUI to create custom parsing configurations. Others provide an editor writing custom parsing rules.

### Visualization:
An incorrect parsing configuration can show wrong data values and lead to inaccurate analysis. A good log management solution should allow you to perform a “dry-run” of the parsing rule by previewing the key-value pairs from a sample data set before saving it. It should also offer visual aids for creating and updating the parsing configuration. This can include color-coding and highlighting non-matching fields or errors.

## Tools/Packages used in this are:
numpy -> https://numpy.org/doc/
pandas	-> https://pandas.pydata.org/docs/
pip	-> https://pip.pypa.io/en/stable/
pprint (pretty print) ->	https://docs.python.org/3/library/pprint.html
pretty-html-table	->	https://pypi.org/project/pretty-html-table/
python-dateutil	->	https://dateutil.readthedocs.io
pytz	->	https://pythonhosted.org/pytz/
setuptools	->	https://setuptools.pypa.io/en/latest/
six	->	https://six.readthedocs.io/
tzdata ->	https://tzdata.readthedocs.io/en/latest/
wheel	->	https://wheel.readthedocs.io/en/stable/

## How does this log parser works?
1. Clone the repository or download the contents of the repository as a Zip file.
2. Set up PyCharm Community Edition (https://www.jetbrains.com/pycharm/download/?section=windows) on your computer.
3. Import the project into PyCharm.
4. Import all the packages (You can watch a video on YouTube to learn how to do this).
5. Run the log_parser.py file by clicking on the run button.
6. After that, the software will execute the remaining tasks, which include scanning the serverlogs.logs file and providing the parsed logs in the output.csv file.
7. Now to get the output.csv file to your provided email address
8. Adjust the required settings by viewing the comments.

## Future Updates

1. I'll try to make the parser more dynamic so that it can offer far more comprehensive solutions.
2. In the near future, I'll try to add more features to it.
