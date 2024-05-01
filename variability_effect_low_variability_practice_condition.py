# A prompt for the low-variability/practice group in simulated expert evaluations replicating the Variability Effect. Note that problems with even numbers have the same format as problems with odd numbers.
PROMPT = '''
Here is an 8th-grade student with the following skill levels (each skill is rated on a scale from 1 to 5):
    1. Being able to set up systems of equations given a word problem: {level1}
    2. Being able to solve systems of equations: {level2}

Here's the instruction that the student receives. The student is asked to work on the following problems on their own: 
1. A brownie recipe is asking for 350 grams of sugar, and a pound cake recipe requires 270 more grams of sugar than a brownie recipe. How many grams of sugar are needed for the pound cake? 
2. A cookie recipe is asking for 400 grams of sugar, and a brownie recipe requires 70 more grams of sugar than a cookie recipe. How many grams of sugar are needed for the brownie? 
3. Devon is 26 years older than his son Cooper. The sum of their ages is 50. Find Devon's age.
4. Pam is 3 years older than her sister, Jan. The sum of their ages is 99. Find Pam's age.
5. Last month Jim and Debbie earned $7,200. Debbie earned $1,600 more than Jim earned. How much did Debbie earn?
6. A married couple together earn $75,000. The husband earns $15,000 more than five times what his wife earns. What does the wife earn?

Now the student is asked to work on the following problem on a test: {problem} Given the student's initial skill levels and the instruction the student has received, what's the probability that the student can solve the problem correctly? Explain your reasoning and give a single number between 0 and 100 in square brackets.
'''