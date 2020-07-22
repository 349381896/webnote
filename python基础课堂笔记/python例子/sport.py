#体育竞技分析
from random import random
def printIntro():
    print("这是程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行时需要A和B的能力值（以0到1之间的小数表示）")

def getInputs():
    a,b,n = eval(input("请依次输入选手A、选手B能力值，以及模拟比赛场数（用逗号分隔）："))
    return a,b,n
def printSummary(winsA,winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))

def gamOver(scoreA,scoreB):
    return scoreA == 15 or scoreB == 15

def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = "A"
    while not gamOver(scoreA,scoreB):
        if serving =="A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
        return scoreA,scoreB

def simNGames(n,probA,probB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB

def main():
    printIntro()
    probA,probB,n = getInputs()
    winsA,winsB = simNGames(n,probA,probB)
    printSummary(winsA,winsB)
if __name__ == "__main__":
    main()