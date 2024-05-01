# A prompt for the low-variability/worked-example group in simulated expert evaluations replicating the Variability Effect. Note that problems with even numbers have the same format as problems with odd numbers. All problems are presented with their step-by-step solutions.
PROMPT = '''
Here is an 8th-grade student with the following skill levels (each skill is rated on a scale from 1 to 5):
    1. Being able to set up systems of equations given a word problem: {level1}
    2. Being able to solve systems of equations: {level2}

Here's the instruction that the student receives. The student is asked to study a problem and its solution. Here's the problem: 
A brownie recipe is asking for 350 grams of sugar, and a pound cake recipe requires 270 more grams of sugar than a brownie recipe. How many grams of sugar are needed for the pound cake? Here's its solution:
Step 1: Identify the amount of sugar needed for the brownie recipe, which is 350 grams.\nStep 2: Understand that the pound cake recipe requires 270 more grams of sugar than the brownie recipe.\nStep 3: Add the additional 270 grams of sugar to the 350 grams required for the brownie recipe.\nStep 4: The total amount of sugar needed for the pound cake recipe is 350 grams + 270 grams = 620 grams.

The student is then asked to study another problem and its solution. Here's the problem: 
A cookie recipe is asking for 400 grams of sugar, and a brownie recipe requires 70 more grams of sugar than a cookie recipe. How many grams of sugar are needed for the brownie? Here's its solution:
Step 1: Identify the amount of sugar needed for the cookie recipe, which is 400 grams.\nStep 2: Understand that the brownie recipe needs 70 grams more sugar than the cookie recipe.\nStep 3: Add the extra 70 grams of sugar to the 400 grams needed for the cookie recipe.\nStep 4: The total amount of sugar needed for the brownie recipe is 400 grams + 70 grams = 470 grams.

The student is then asked to study another problem and its solution. Here's the problem: 
Devon is 26 years older than his son Cooper. The sum of their ages is 50. Find Devon's age. Here's its solution:
Step 1: Let's denote Devon's age as D and Cooper's age as C.\nStep 2: According to the problem, we have two equations. The first one is D = C + 26 (since Devon is 26 years older than Cooper). The second one is D + C = 50 (since the sum of their ages is 50).\nStep 3: We can substitute the first equation into the second one. So, instead of D in the second equation, we can put C + 26. We get C + 26 + C = 50.\nStep 4: Simplify the equation. Combine like terms to get 2C + 26 = 50.\nStep 5: Subtract 26 from both sides of the equation to get 2C = 24.\nStep 6: Divide both sides of the equation by 2 to get C = 12. So, Cooper is 12 years old.\nStep 7: Substitute C = 12 into the first equation (D = C + 26) to get D = 12 + 26 = 38.\nSo, Devon is 38 years old.

The student is then asked to study another problem and its solution. Here's the problem: 
Pam is 3 years older than her sister, Jan. The sum of their ages is 99. Find Pam's age. Here's its solution:
Step 1: Let's denote Jan's age as x.\nStep 2: Since Pam is 3 years older than Jan, we can denote Pam's age as x + 3.\nStep 3: According to the problem, the sum of their ages is 99. So, we can write the equation: x + (x + 3) = 99.\nStep 4: Simplify the equation by combining like terms: 2x + 3 = 99.\nStep 5: Subtract 3 from both sides of the equation to isolate the term with x: 2x = 99 - 3, which simplifies to 2x = 96.\nStep 6: Divide both sides of the equation by 2 to solve for x: x = 96 / 2, which simplifies to x = 48.\nSo, Jan is 48 years old.\nStep 7: To find Pam's age, add 3 to Jan's age: 48 + 3 = 51.\nSo, Pam is 51 years old.

The student is then asked to study another problem and its solution. Here's the problem: 
Last month Jim and Debbie earned $7,200. Debbie earned $1,600 more than Jim earned. How much did Debbie earn? Here's its solution:
Step 1: Let's denote the amount Jim earned as J. \nStep 2: According to the problem, Debbie earned $1,600 more than Jim, so we can denote the amount Debbie earned as J + $1,600.\nStep 3: We know that the total amount they earned together is $7,200. So, we can set up the following equation: J + (J + $1,600) = $7,200.\nStep 4: Simplify the equation by combining like terms: 2J + $1,600 = $7,200.\nStep 5: To solve for J, subtract $1,600 from both sides of the equation: 2J = $7,200 - $1,600 = $5,600.\nStep 6: Divide both sides of the equation by 2 to solve for J: J = $5,600 / 2 = $2,800.\nStep 7: Substitute J = $2,800 back into the equation from Step 2 to find out how much Debbie earned: Debbie earned J + $1,600 = $2,800 + $1,600 = $4,400. \nSo, Debbie earned $4,400 last month.

The student is then asked to study another problem and its solution. Here's the problem: 
A married couple together earn $75,000. The husband earns $15,000 more than five times what his wife earns. What does the wife earn? Here's its solution:
Step 1: Let's denote the wife's earnings as W.\nStep 2: According to the problem, the husband earns $15,000 more than five times what his wife earns. So, we can express the husband's earnings as 5W + $15,000.\nStep 3: The problem also states that the couple together earn $75,000. So, we can set up the following equation to represent the total earnings of the couple: W + (5W + $15,000) = $75,000.\nStep 4: Simplify the equation by combining like terms: 6W + $15,000 = $75,000.\nStep 5: Subtract $15,000 from both sides of the equation to isolate the term with W: 6W = $60,000.\nStep 6: Divide both sides of the equation by 6 to solve for W: W = $10,000.\nSo, the wife earns $10,000.

Now the student is asked to work on the following problem on a test: {problem} Given the student's initial skill levels and the instruction the student has received, what's the probability that the student can solve the problem correctly? Explain your reasoning and give a single number between 0 and 100 in square brackets.
'''