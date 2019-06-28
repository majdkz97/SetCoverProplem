import Population
import SCP
import random
class GA:
      numOfUnivers = 1000
      countOfChromosomes = 200
      countOfSubSets = 10
      list_subSetCost = list()
      list_validChromosomes = list()


      for i in range(countOfSubSets):
          list_subsetCost = input()
          list_subSetCost.append(list_subsetCost)

      def __init__(self,numOfUni,numOfChromosomes,numOfSubSets,list_subSetCost,):
          self.numOfUnivers = numOfUni 
          self.countOfChromosomes =numOfChromosomes
          self.countOfSubSets = numOfSubSets
          list_validChromosomes = list()
          self.population = Population.Population(numOfUni,numOfChromosomes,numOfSubSets,list_validChromosomes)
        

      def FitnessFunction(self,numOfChromosomes,list_validChromosomes,list_subSetCost):
          list_chromosomeCost = list()
          list_chromosomeSize = list()
          for i in range(numOfChromosomes):
              totalCost = 0
              totalSize = 0
              list_sortedFitnessResault = list()
              for j in range(self.list_subSetCost.__len__()):
                  if (list_validChromosomes[i][j] == 1):
                      totalCost = totalCost + list_subSetCost[j]
                      totalSize += 1
              list_chromosomeCost.append(totalCost)
              list_chromosomeSize.append(totalSize)
          fitnessResult = list()
          for i in range(numOfChromosomes):
              fitnessResult[i] = 1/(8*list_chromosomeCost[i] + 2*list_chromosomeSize[i])
          list_sotredFitness = fitnessResult
          list_sotredFitness.sort()
          list_sortedFitnessResault.reverse()
          for index in range(list_sotredFitness.__len__()):
              for j in range(fitnessResult.__len__()):
                  if(list_sotredFitness[index] == fitnessResult[j]):
                      list_sortedFitnessResault.append(list_validChromosomes[j])
                      fitnessValSorted = fitnessResult[j]
                      chromosomeSorted = list_validChromosomes[j]
                      fitnessResult.remove(fitnessValSorted)
                      list_validChromosomes.remove(chromosomeSorted)


      
      def RoulleteWheelSelection(self,list_sortedFitnessValue,list_roulletWheel,rand):
          totalEvaluation = 0
          for i in list_sortedFitnessValue:
              totalEvaluation += i
          for j in range(list_sortedFitnessValue.__len__()):
              if(j==0): 
                  list_roulletWheel.append(list_sortedFitnessValue[j]/totalEvaluation) 
              else:
                  list_roulletWheel.append(list_roulletWheel[j-1] + list_sortedFitnessValue[j]/totalEvaluation)
          for r in range(list_roulletWheel.__len__()):
              if (rand <= list_roulletWheel[r]):
                  return r
 
      def SinglePointCrossover(self,firstParent,secondParent):
          newFirstChild = firstParent
          newSecondChild = secondParent
          cxPoint = int(random.randrange(0,firstParent.__len__()))
          temp = newFirstChild[cxPoint:]
          newFirstChild[cxPoint:] = newSecondChild[cxPoint:]
          newSecondChild[cxPoint:] = temp
          return newFirstChild,newSecondChild
          
