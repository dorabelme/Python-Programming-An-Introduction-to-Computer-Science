# print a (new) intro
# get probA, probB, n from user
# calculate the average number of wins for the better player over 10 rounds of n games
# calculate the maximum deviation
# print the data

import volleyball_mod
import volleyball_rally_mod

def main():
	printIntro()
	probA, probB, n = getInputs()
	avg_wins, max_dev = avg0fK(probA, probB, n, 10)
	winsA_rally, winsB_rally = \
		volleyball_rally_mod.getStats(probA, probB, 10 * n)
	wins_rally = max(winsA_rally, winsB_rally)
	printStats(avg_wins, max_dev, wins_rally, n ,10)

def printIntro():
	print("This program analyzes the results of games of volleyball")
	print('between two players called "A" and "B" under regular rules')
	print("and rally rules. The abilities of each player is indicated")
	print("by a probablitiy (a number between 0 and 1) that the")
	print("player wins the point when serving. Player A always")
	print("has the first serve.")

def getInputs():
	# Returns the three simulation parameters probA, probB and n
	a = float(input("What is the prob. player A wins a serve? "))
	b = float(input("What is the prob. player B wins a serve? "))
	n = int(input("How many games to simulate? "))
	return a, b, n

def avg0fK(probA, probB, n, k):
	winsA_list = []
	winsB_list = []
	for i in range(k):
		winsA, winsB = volleyball_mod.getStats(probA, probB, n)
		winsA_list.append(winsA)
		winsB_list.append(winsB)

	avg_winsA = sum(winsA_list) / len(winsA_list)
	avg_winsB = sum(winsB_list) / len(winsB_list)
	if avg_winsA > avg_winsB:
		avg_wins = avg_winsA
		max_dev = max(max(winsA_list)-avg_wins, avg_wins - min(winsB_list))
	else:
		avg_wins = avg_winsB
		max_dev = max(max(winsB_list)-avg_wins, avg_wins - min(winsB_list))
	return avg_wins, max_dev

def printStats(avg_wins, max_dev, wins_rally, n, k):
	print("\nStats for Better Team")
	print("Average number of wins per", n, "games: " +
		"{0:0.0f} ± {1:0.0f}".format(avg_wins, max_dev))
	print("Average number of wins with rally scoring: " +
		"{0:0.0f}".format(wins_rally / k))
	if wins_rally / k < avg_wins - max_dev:
		print("It appears that rally scoring reduces the advantage of the " +
			"better team.")
	elif wins_rally / k > avg_wins + max_dev:
		print("It appears that rally scoring increases the advantage of the " +
			"better team.")
	else:
		print("There does not seem to be a statistical change in the relative " +
			"advantage of the better team using rally scoring.")

main()
