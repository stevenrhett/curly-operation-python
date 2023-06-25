# Problem list

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

The purpose of these questions is to make sure you're comfortable reading and writing data to files from Python, in addition to parsing data of different formats and using different data formats intelligently to create better solutions.

### Housing data

Write a program to ingest the `home_data.csv` file and list the 10 least expensive houses along with their ZIP codes, condition, and living square feet.

### Olympics

Write a program to ingest the `olympics.csv` file and list the top 3 countries who have won the most summer olympic medals and the top 3 countries who have won the most winter olypmic medals.

### Movies data

Write a program to ingest the `movies.csv` file and list top rated movie in each genre.

### Narcos - show info

Write a program to ingest the `narcos.json` file and list the TV show name, the genres that it fits under, and the average show rating.

### Narcos - episode info

Write a program to ingest the `narcos.json` file and list each episodes' name, season, and rating, sorted by the highest to lowest rating.

### User creation

The point of this exercise is to practice storing and changing user information. Your program should parse JSON data (from a file for now), allowing the following fields to be set via that JSON: `username`, `first-name`, `last-name`, `email`, `password`, `following`, `followers`. These are all strings except `following` and `followers`, which are bost lists of strings.

In `/data` you will find a file called `new_user.json`. Create a new user from this data and store it however you'd like (JSON or CSV probably makes sense). You can store this file in `/data` if you'd like.

Your program should also be able to show a list of all existing users, showing their username.

> Question: Is there anything else you think we might want to save for each user?

### (challenge) Editing an existing user

Using the set up from the previous problem, allow a user's list of `following` and `followers` to be updated via JSON.

In `/data` you will find a file named `add_follower.json` to do this with. You should update the appropriate list for both uses.

Make sure that the user being followed exists before adding it to the list! Your program should print the new list at the end.


## Loop practice

### Multiplication

Write a function to find the product (multiplication) of two given numbers only using addition. For example, `multiple(2, 5)` should result in 10.

### Modulo

Write a function tthat calculates the modulo (remainder - usually `%`) of a number divided by another number.. For example, `mod(137, 10)` should result in 7.

### Sum

Write a program to calculate the sum of digits in a number using a loop.

### Divisibility

Write a program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

(challenge) Make this program generic to handle any two numbers passed in.

### Powers

Write a program to find the value of a given number raised to the power of a second given number using a loop. For example, `power(5, 2)` should result in 25.

### Factorials

Write a function to find the factorial value of any number using a loop. For example, given `4` return 24, given `5` return `120`.

### Find the number of 0s

Write a program to find the number of zeros in 2D matrix. For example: `const arr = [[0,1,1],[0,1,0],[1,0,0]];`.

(challenge) Allow any number of nesting of arrays to be used.

### Find the most repeated number

Given a two dimensional array of numbers, find the number that is repeated the most times using for loops.

### Pattern creation

Write a program to construct the following pattern using loops.

```
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```

### Minesweeper

Given a 2D array of strings with equal rows and columns, output a 2D array that has either an "X" if there was an "X" in the cell originally or the count of all adjacent Xs to that cell.

For example, given:

```
[
  [" ", " ", "X", " "],
  [" ", "X", " ", " "],
  [" ", " ", "X", "X"],
  ["X", " ", " ", " "],
]
```

The result should be:

```
[
  [  1,   2, "X",   1],
  [  1, "X",   4,   3],
  [  2,   3, "X", "X"],
  ["X",   1,   2,   2],
]
```

### Sum of adjacent cells

Given a 2D array of numbers with equal rows and columns, output a 2D array that has the sum of all 9 adjacent cells, including itself.

For example, given:

```
[
  [0, 0, 1, 0],
  [0, 1, 2, 0],
  [3, 0, 0, 1],
  [0, 0, 1, 0],
]
```

The result should be:

```
[
  [1, 4, 4, 3],
  [4, 7, 5, 4],
  [4, 7, 5, 4],
  [3, 4, 2, 2],
]
```

## (optional) Advanced topics, in order of perceived helpfulness

### Sorting algorithms

It's handy to know one fast sorting algorithm from memory. It's also handy to know when other sorting algorithms may be beneficial, even if you don't know how to write them from memory.

### Data structures practice

There are a lot of different data structures (binary trees, linked lists, etc.). Get some practice with them to perhaps be able to recognize when a problem would be benefited from using them.

### Pathfinding algorithms

Write a Python program to implement a pathfinding algorithm to find the shortest path between two points in a 2D grid. You can use the A\* algorithm or any other pathfinding algorithm of your choice. The program should take as input the start and end points, as well as the obstacles in the grid.

### Sockets (responding to live data)

There are a lot of instances where you might want to listen for traffic at a particular address and handle the flow of data. Common use cases for this sort of thing includes traffic hitting an endpoint and users posting new content.

### Web scraping

Write a Python program to scrape data from a website and save it to a CSV file. You can use a library like Beautiful Soup or Scrapy to extract the data. The program should be able to handle multiple pages of data and should be robust enough to handle errors and exceptions that may arise during the scraping process.

You might want to also investigate how to use online web scraping tools.

### Image processing effects

Write a Python program to process an image and extract certain features from it. For example, you could write a program to detect edges in an image, or to identify objects in an image using machine learning techniques.
