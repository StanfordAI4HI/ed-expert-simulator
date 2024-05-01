# The optimization prompt for generating a new instruction (e.g., a worksheet) based on prior instructions and post-test scores for a given student
PROMPT = '''
Here is an 8th-grade student with the following skill levels (each skill is rated on a scale from 1 to 5, where higher numbers indicate more proficiency):
    1. Being able to set up systems of equations given a word problem: 1
    2. Being able to solve systems of equations: 1

I have some worksheets along with the student's test scores after receiving the worksheets. The worksheets are arranged in ascending order based on their scores, where higher scores indicate better quality.

Worksheet: 
You need to study a problem and its solution. Here's the problem: 
A brownie recipe is asking for 350 grams of sugar, and a pound cake recipe requires 270 more grams of sugar than a brownie recipe. How many grams of sugar are needed for the pound cake? Here's its solution:
Step 1: Identify the amount of sugar needed for the brownie recipe, which is 350 grams.\nStep 2: Understand that the pound cake recipe requires 270 more grams of sugar than the brownie recipe.\nStep 3: Add the additional 270 grams of sugar to the 350 grams required for the brownie recipe.\nStep 4: The total amount of sugar needed for the pound cake recipe is 350 grams + 270 grams = 620 grams.
Test score: 
20

Generate a new worksheet to further increase the test score of the student. You will be evaluated based on this score function:
```python
{utility_string}
```
The new worksheet should begin with <WORKSHEET> and end with </WORKSHEET>.
'''