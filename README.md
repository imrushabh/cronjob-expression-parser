**cronjob-expression-parser**

**Problem statement:-**

command line application which parses a cron string and expands each field
to show the times at which it will run.

**Input/output:-**

This repo parse the give corn expression and return the result as below.

Input:- 
```
*/15 0 1,15 * 1-5 /usr/bin/find
```

output:-
```
minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find
```
**Setting up local development:-**

1. Install python 3
ex:- On Mac(for brew user) 
```
brew install python3
```

2. Create virtual environment
commands:-
```
pip3 install virtualenv
virtualenv -p python3 <desired-path>
source <desired-path>/bin/activate
```
3. Install the requirements.txt file
```
pip3 install -r requirements.txt
```

4. Change directory to generator and run below command
```
python3 main.py "0 22 * * 5-5 /usr/bin/find"
```

5. To run the test, change directory to test and run below command
```
python3 Test_ExpressionParser.py
```

For more info related to Cron expression please refer below links:-
https://crontab.guru/
https://docs.oracle.com/cd/E12058_01/doc/doc.1014/e12030/cron_expressions.htm

Note:-
This parser doesn't have all the functionality coverved. All the functionality will be extended in the future releases.

Thanks
Rushabh Gaherwar
Author
