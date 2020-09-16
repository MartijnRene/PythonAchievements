import math

trees = 333
shadedTrees = (trees / 3) * 2
sunnyTrees = trees / 3

shadeOutputModifier = 0.8

sunnyTreeOutput = 146
shadedTreeOutput = sunnyTreeOutput * shadeOutputModifier

sunnyOutput = sunnyTrees * sunnyTreeOutput
shadedOutput = shadedTrees * shadedTreeOutput
totalOutput = sunnyOutput + shadedOutput

owners = 3

eatCount = totalOutput % 3
sellableOutput = totalOutput - eatCount
cut = sellableOutput / owners

print(cut)