# Problem list

## From [Harvard's CS50 course](https://computersciencewiki.org/index.php/Problem_Sets)

### Min and max

Write a program that takes a list of numbers as its input. Then return the highest and lowest numbers that were given.

### Bill calculator

Write a program that calculates the total cost of a restaurant bill. It should act like the example below. For invalid items, let the user know it is not valid and don’t include it in the total:

```
$ python3 bill.py
Choose from the following menu to order. Press enter when done.
Burger: $9.50
Vegan Burger: $11.00
Hot Dog: $5.00
Cheese Dog: $7.00
Fries: $5.00
Cheese Fries: $6.00
Cold Pressed Juice: $7.00
Cold Brew: $3.00
Water: $2.00
Soda: $2.00

Enter a food item: burger
Enter a food item: fries
Enter a food item: ice cream
Sorry, “ice cream” is not a valid option
Enter a food item: soda
Enter a food item:

Your total cost is: $16.50
```

### Hours worked

Write a program that prompts users for the number of weeks that they worked. Then prompt them for how many hours they worked each week. Then prompt them for whether they’d like the total number of hours worked or the average of the number of hours per week and return the result asked for.

Example 1:

```
$ python3 hours.py
Number of weeks to track: 3
Week 0 HW Hours: 3
Week 1 HW Hours: 7
Week 2 HW Hours: 10
Enter T for total hours, A for average hours per week: A
6.7 hours
```

Example 2:

```
$ python3 hours.py
Number of weeks taking CS50: 2
Week 0 HW Hours: 2
Week 1 HW Hours: 8
Enter T for total hours, A for average hours per week: T
10.0 hours
```

### 1337SP36K

Write a program that replaces all of the following vowels with the corresponding listed numbers: `a` becomes `6`, `e` becomes `3`, `i` becomes `1`, `o` becomes `0` and `u` does not change.

### Password validator

Write a program to check whether the provided string has at least one lower case letter, one upper case letter, one number and one symbol. It should let the user know what they are missing if they are missing something and let them know if it’s valid if it’s valid.

### Rotation cypher

Write a program that encrypts a given message using a rotation cypher, rotating by the amount given (N). A rotation cypher is a character based cypher where each character receives a “shift” / “rotation” by a given N letters in an alphabet. In other words, any single letter is replaced by a different single letter that is located further (exactly N letters further) in the alphabet, wrapping from the beginning to the start.

Example 1:

```
$ python3 cypher.py 1 hello
ifmmp
```

Example 2:

```
$ python3 cypher.py 2 Hello
Jgnnq
```

### Change calculator

Write a program that takes a positive number as an input and returns a list of the minimum number of dollars (up to $20 bills) and coins to make up that amount.

Example 1:

```
$ python3 change.py 0.41
1 quarter
1 dime
1 nickel
1 penny
```

Example 2:

```
$ python3 change.py 22.50
1 $20 bill
2 $1 bills
2 quarters
```

### (challenge) Substitution cypher

Write a program that encrypts a given message using a substitution cypher, where a letter is replaced by another letter using the key-value pair given. The user should input their substitution by providing a list of all 26 letters as a single string, followed by the string they’d like to encrypt. Make sure to check to make sure the substitution is valid, letting the user know what letters were used multiple times or were missing if their substitution was invalid.

Example 1:

```
$ python3 substitution.py YTNSHKVEFXRBAUQZCLWDMIPGJO HELLO
EHBBQ
```

## Basic data parsing and handling

TODO: The purpose of these questions is to make sure you're comfortable reading and writing data to files from Python, in addition to parsing data of different formats and using different data formats intelligently to create better solutions.

## Loop practice

TODO: these are on my other computer, will add once I get access to it

## Advanced topics

### Pathfinding Algorithms

Write a Python program to implement a pathfinding algorithm to find the shortest path between two points in a 2D grid. You can use the A\* algorithm or any other pathfinding algorithm of your choice. The program should take as input the start and end points, as well as the obstacles in the grid.

### Image Processing

Write a Python program to process an image and extract certain features from it. For example, you could write a program to detect edges in an image, or to identify objects in an image using machine learning techniques.

### Web Scraping

Write a Python program to scrape data from a website and save it to a CSV file. You can use a library like Beautiful Soup or Scrapy to extract the data. The program should be able to handle multiple pages of data and should be robust enough to handle errors and exceptions that may arise during the scraping process.
