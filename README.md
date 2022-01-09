# Election_Analysis
Module 3 - Election Analysis using Python

## Overview of Project
A fictional Colorado Board of Elections employee has asked to audit the results for a US congressional precinct in Colorado. The audit takes a .csv file containing all the tabulated votes and uses python to report on the following items of the election:
1. The total number of votes cast
1. A list of candidates who received votes
1. The total number of votes each candidate received
1. The percentage of votes each candidate received
1. The winner of the election based on the popular vote
1. A list of counties in the precinct
1. The total number of votes cast in each county
1. The percentage of votes cast in each county
1. The county with the highest turnout

## Election Audit Results
The analysis of the election show that:
* There were 369,711 votes cast.
* The county results were:
  * Arapahoe County: 24, 801 votes, 6.7%
  * Denver County: 306,055 votes, 82.8% 
  * Jefferson County:  38,855 votes,  10.5% 
* Denver County had the largest turnout.
* The candidate results were:
  * Diana DeGette received 73.8% of the votes and 272,892 number of votes.
  * Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
  * Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
* The **winner of the election** was:
  * **Diana DeGette** who received **73.8%** of the vote and **272,892** votes.

## Election Audits Summary
The code used to generate the election audit results can easily be repurposed to automate other types of elections, such as senatorial or local elections. The results are saved to a .txt file which can be sent to an election commission. If additional voting information is also saved to a .csv, the code could be extended to report on votes by voting method (ballot, mail-in), for example. 

There are a few ways to improve upon this election audit.  The code could be modified to check that all ballot ids are unique. Additionally, the report could show the percentage of votes that each candidate received per county. If the total number of registered voters is known, the results could include percentage of voter turnout.



