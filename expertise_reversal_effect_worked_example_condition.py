# A prompt for the worked-example group in simulated expert evaluations replicating the Expertise Reversal Effect. The first, third, fifth, and seventh problems have step-by-step solutions, while the other problems do not.
PROMPT = '''
Here is an 8th-grade student with the following skill levels (each skill is rated on a scale from 1 to 5):
    1. Being able to set up systems of equations given a word problem: {level1}
    2. Being able to solve systems of equations: {level2}

Here's the instruction that the student receives. The student is asked to study a problem and its solution. Here's the problem: 
A brownie recipe is asking for 350 grams of sugar, and a pound cake recipe requires 270 more grams of sugar than a brownie recipe. How many grams of sugar are needed for the pound cake? Here's its solution:
Step 1: Identify the amount of sugar needed for the brownie recipe, which is 350 grams.\nStep 2: Understand that the pound cake recipe requires 270 more grams of sugar than the brownie recipe.\nStep 3: Add the additional 270 grams of sugar to the 350 grams required for the brownie recipe.\nStep 4: The total amount of sugar needed for the pound cake recipe is 350 grams + 270 grams = 620 grams.
The student is then asked to work on the following problem on their own:
The size of a compressed file is 1.74 MiB, while the size of the original uncompressed file is 5.5 times greater. What is the size of the uncompressed file, in MiB?
The student is then asked to study another problem and its solution. Here's the problem: 
Devon is 26 years older than his son Cooper. The sum of their ages is 50. Find Devon's age. Here's its solution:
Step 1: Let's denote Devon's age as D and Cooper's age as C.\nStep 2: According to the problem, we have two equations. The first one is D = C + 26 (since Devon is 26 years older than Cooper). The second one is D + C = 50 (since the sum of their ages is 50).\nStep 3: We can substitute the first equation into the second one. So, instead of D in the second equation, we can put C + 26. We get C + 26 + C = 50.\nStep 4: Simplify the equation. Combine like terms to get 2C + 26 = 50.\nStep 5: Subtract 26 from both sides of the equation to get 2C = 24.\nStep 6: Divide both sides of the equation by 2 to get C = 12. So, Cooper is 12 years old.\nStep 7: Substitute C = 12 into the first equation (D = C + 26) to get D = 12 + 26 = 38.\nSo, Devon is 38 years old.
The student is then asked to work on the following problem on their own:
When Jenna spent 10 minutes on the elliptical trainer and then did circuit training for 20 minutes, her fitness app says she burned 278 calories. When she spent 20 minutes on the elliptical trainer and 30 minutes circuit training she burned 473 calories. How many calories does she burn for each minute on the elliptical trainer?
The student is then asked to study another problem and its solution. Here's the problem: 
Last month Jim and Debbie earned $7,200. Debbie earned $1,600 more than Jim earned. How much did Debbie earn? Here's its solution:
Step 1: Let's denote the amount Jim earned as J. \nStep 2: According to the problem, Debbie earned $1,600 more than Jim, so we can denote the amount Debbie earned as J + $1,600.\nStep 3: We know that the total amount they earned together is $7,200. So, we can set up the following equation: J + (J + $1,600) = $7,200.\nStep 4: Simplify the equation by combining like terms: 2J + $1,600 = $7,200.\nStep 5: To solve for J, subtract $1,600 from both sides of the equation: 2J = $7,200 - $1,600 = $5,600.\nStep 6: Divide both sides of the equation by 2 to solve for J: J = $5,600 / 2 = $2,800.\nStep 7: Substitute J = $2,800 back into the equation from Step 2 to find out how much Debbie earned: Debbie earned J + $1,600 = $2,800 + $1,600 = $4,400. \nSo, Debbie earned $4,400 last month.
The student is then asked to work on the following problem on their own:
Pam is 3 years older than her sister, Jan. The sum of their ages is 99. Find Pam's age.
The student is then asked to study another problem and its solution. Here's the problem: 
Lynn paid a total of $2,780 for 261 tickets to the theater. Student tickets cost $10 and adult tickets cost $15. How many student tickets did Lynn buy? Here's its solution:
Step 1: Let's denote the number of student tickets as S and the number of adult tickets as A.\nStep 2: We know that the total number of tickets is 261, so we can write the equation: S + A = 261.\nStep 3: We also know that the total cost of the tickets is $2,780, with student tickets costing $10 and adult tickets costing $15. This gives us the equation: 10S + 15A = 2780.\nStep 4: To solve these two equations, we can first multiply the first equation by 10 to make the coefficients of S the same in both equations: 10S + 10A = 2610.\nStep 5: Now, subtract the new first equation from the second equation: 10S + 15A - (10S + 10A) = 2780 - 2610. This simplifies to 5A = 170.\nStep 6: Divide both sides of the equation by 5 to solve for A: A = 170 / 5 = 34.\nStep 7: Substitute A = 34 into the first equation: S + 34 = 261. Solve for S: S = 261 - 34 = 227.\nSo, Lynn bought 227 student tickets.
The student is then asked to work on the following problem on their own:
Yumi wants to make 12 cups of party mix using candies and nuts. Her budget requires the party mix to cost her $1.29 per cup. The candies are $2.49 per cup and the nuts are $0.69 per cup. How many cups of candies should she use?

Now the student is asked to work on the following problem on a test: {problem} Given the student's initial skill levels and the instruction the student has received, what's the probability that the student can solve the problem correctly? Explain your reasoning and give a single number between 0 and 100 in square brackets.
'''