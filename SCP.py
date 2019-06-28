
#Rita
import random
class SCP:
      def __init__(self,sizeOfUniversal,countOfSubsets):
          self.sizeOfUniversal = sizeOfUniversal
          self.countOfSubsets = countOfSubsets
          universal = set()
          set_notCovered = set()
          list_subsets = list()
          for i in range(sizeOfUniversal):
              universal.add(i+1)
          unionOfsubsets = self.Init_Subsets(sizeOfUniversal,countOfSubsets,list_subsets)
          set_notCovered = universal - unionOfsubsets
          if(set_notCovered.__len__() != 0):
             self.listOfSubsets = self.Prepare_Subsets(set_notCovered,list_subsets)
          

      def Init_Subsets(self,sizeOfUniversal,countOfSubsets,list_subsets):
          unionSbset = set()
          for i in range(countOfSubsets):
              subset = set()
              sizeOfSubset = random.randrange(1,sizeOfUniversal)
              for j in range(sizeOfSubset):
                  subset.add(random.randrange(1,sizeOfUniversal))
              list_subsets.append(subset)
              unionSbset = unionSbset|subset
          return unionSbset    

      def Prepare_Subsets(self,set_notCovered,list_subsets):
          for i in set_notCovered:
              countOfSomeSets = random.randrange(1,list_subsets.__len__())
              for j in range(countOfSomeSets):
                  chooseIndex = random.randrange(0,list_subsets.__len__()-1)
                  miniSet = list_subsets[chooseIndex]
                  list_subsets.remove(miniSet)
                  miniSet.add(i)
                  list_subsets.insert(chooseIndex,miniSet)
          return list_subsets


      
                
            
        
    

                
                 
           
             
     
    
     
    
   

