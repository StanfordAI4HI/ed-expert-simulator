# A prompt for the high-variability/practice group group in simulated expert evaluations replicating the Variability Effect. Note that problems with even numbers are different than problems with odd numbers in both formats and values.
PROMPT = '''
Here is an 8th-grade student with the following skill levels (each skill is rated on a scale from 1 to 5):
    1. Being able to set up systems of equations given a word problem: {level1}
    2. Being able to solve systems of equations: {level2}

Here's the instruction that the student receives. The student is asked to work on the following problems on their own: 
1. A brownie recipe is asking for 350 grams of sugar, and a pound cake recipe requires 270 more grams of sugar than a brownie recipe. How many grams of sugar are needed for the pound cake? 
2. The size of a compressed file is 1.74 MiB, while the size of the original uncompressed file is 5.5 times greater. What is the size of the uncompressed file, in MiB?
3. Devon is 26 years older than his son Cooper. The sum of their ages is 50. Find Devon's age.
4. When Jenna spent 10 minutes on the elliptical trainer and then did circuit training for 20 minutes, her fitness app says she burned 278 calories. When she spent 20 minutes on the elliptical trainer and 30 minutes circuit training she burned 473 calories. How many calories does she burn for each minute on the elliptical trainer?
5. Last month Jim and Debbie earned $7,200. Debbie earned $1,600 more than Jim earned. How much did Debbie earn?
6. Lynn paid a total of $2,780 for 261 tickets to the theater. Student tickets cost $10 and adult tickets cost $15. How many student tickets did Lynn buy?

Now the student is asked to work on the following problem on a test: {problem} Given the student's initial skill levels and the instruction the student has received, what's the probability that the student can solve the problem correctly? Explain your reasoning and give a single number between 0 and 100 in square brackets.
'''