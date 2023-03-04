# Deutschlander-Machine-Company-Problem-with-Linear-Programming

Deutchlander Machine Company (DMC) makes two types of printing presses: a four-color litho and a two-color litho. Demand for both products is booming and exceeds DMC's ability to satisfy it. Most raw materials are plentiful, but production is limited by three factors: a shortage of steel rollers, gear cutting capacity, and roller polishing capacity. Each four-color press requires 16 rollers, and each two-color press requires 8 rollers. The four-color presses require 30 hours of gear cutting and 8 hours of polishing time, and the two-color presses require 12 hours of gear cutting and 3 hours of polishing time. DMC is able to buy 100 rollers per week, and it has 160 hours of gear cutting time and 40 hours of polishing time available per week. 
To avoid harming long-term sales, DMC does not want to raise prices. At current prices DMC will earn a profit of DM24,000 on each four-color press made and DM10,000 on each two-color press made. So as not to abandon either product market, DMC also wants to produce at least two units of each press each week. 

a. Solution in primal variant 
b. Solution in dual variant

a.1. Formulatation of DMC's problem as a linear program to maximize its profit:

Maximize: 24000x + 10000y
Subject to:
16x + 8y <= 100 (rollers constraint)
30x + 12y <= 160 (gear cutting constraint)
8x + 3y <= 40 (polishing constraint)
x >= 2 (minimum four-color presses constraint)
y >= 2 (minimum two-color presses constraint)
x, y >= 0 (non-negativity constraint)
where x is the number of four-color presses produced and y is the number of two-color presses produced.

a.2. Simplex method: To solve this problem using the simplex method, we can follow these steps:

First, we convert the constraints into the standard form by introducing slack variables:
Maximize: 24000x + 10000y
Subject to:
16x + 8y + s1 = 100 (rollers constraint)
30x + 12y + s2 = 160 (gear cutting constraint)
8x + 3y + s3 = 40 (polishing constraint)
x >= 2 (minimum four-color presses constraint)
y >= 2 (minimum two-color presses constraint)
x, y, s1, s2, s3 >= 0 (non-negativity constraint)

b. Dual variant:

Minimize: 100s1 + 160s2 + 40s3 (s1, s2, s3 are the slack variables)
Subject to:
16s1 + 30s2 + 8s3 >= 24000 (profit constraint)
8s1 + 12s2 + 3s3 >= 10000 (profit constraint)
s1, s2, s3 >= 0 (non-negativity constraint)
