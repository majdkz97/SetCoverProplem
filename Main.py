import random
import Chromosome
import Functions
import Universe
import Set
import Generation

def Main_Solve(universe_Input,list_Genereations,Crossover_Type):
    #توليد الكروموسومات العشوائية لأول مرة
    list_Chromosome = []
    for i in range(1,universe_Input.chromosome_Count+1):
        list_Random_Sets = Functions.build_Chromosome_Randomly(universe_Input)
        object_Chromosome = Chromosome.Chromosome()
        object_Chromosome.List_Genes = list_Random_Sets
        list_Chromosome.append(object_Chromosome)
    
    
    #طباعة الكروموسومات العشوائية
    #print('The Randoms Chromosomes')
  #  for i in list_Chromosome:
        #print(i.List_Genes)
    
    
    #حلقة الأجيال
    for i in range(1,universe_Input.generations_Count+1):
        index=0
        #التحقق من الكروموسومات الصحيحة والخاطئة يتم تصحيحها
        for chromosome in list_Chromosome:
            status = Functions.chromosom_Is_Correct(chromosome.List_Genes,universe_Input)
            
            if status == True:
                status = status
                
            else:
                set_Temp = Functions.chromosome_Get_Sets(chromosome.List_Genes,universe_Input)
                error_Status = Functions.check_Chromosome_Error_Rate(universe_Input,set_Temp)
                if error_Status == True:
                    Functions.fixing_Chromosome_Linear(chromosome.List_Genes,universe_Input)
                    #print('*********Linear************')
                else:
                    new_Chromosome = Functions.fixing_Chromosome_Randomly(universe_Input)
                    #print('*********Randomly************')
                    object_New_Chromosomoe = Chromosome.Chromosome()
                    object_New_Chromosomoe.List_Genes = new_Chromosome.copy() 
                    list_Chromosome[index] = object_New_Chromosomoe
            
            #حساب التكلفة وعدد الواحدات
            Functions.calculate_Costs_And_ActiveBits(universe_Input,list_Chromosome[index])
            #حساب الصلاحية
            Functions.calculate_Fitness(universe_Input,list_Chromosome[index])
        
            index+=1
        
            
        #ترتيب الكروموسومات حسب الأفضل
        newlist_Sorted = sorted(list_Chromosome, key=lambda x: x.Fitness, reverse=True).copy()
        #print('New List Sorted After Fixing')
      #  for x in newlist_Sorted:
            #print(x.List_Genes)
            #print(x.Fitness)
        
        #اضافة افضل كروموسون وليستة الكروموسومات للجيل الحالي
        generation = Generation.Genereation()
        generation.best_Chromosome = newlist_Sorted[0]
        #print('*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/')
        #print(generation.best_Chromosome.List_Genes)
        #print(generation.best_Chromosome.Fitness)

        #print('*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/')
        generation.sorted_Chromosomes = newlist_Sorted.copy()
        list_Genereations.append(generation)
        #انتهت مرحلة الجيل الحالي
        

        if(i==universe_Input.generations_Count):
            continue

        #التجهيز للإنتقال للجيل التالي
        #طباعة الكروموسومات النهائية بعد التصحيح
        #print('Final Chromosomes In This Generation')
       # for x in list_Chromosome:
        #    s = Functions.chromosom_Is_Correct(x.List_Genes,universe_Input)
            #print (s)
            #print(x.List_Genes)
            #print(x.sum_Costs)
            #print(x.Count_Active_Bits)
            #print(x.Fitness)
        

        #تابع تهيئة الاحتمال التراكمي
        list_Cdf=Functions.pdf_Cdf_Functions(list_Chromosome)
        #print('*******List CDF*******')
        #print(list_Cdf)
        
        #عمل كروس أوفر بتطبيق روليت رول
        list_Chromosome_After_Crossover=[]
        for i in range(1,int(universe_Input.chromosome_Count/2) + 1):
            x1 = Functions.roulette_Wheel_Function(list_Cdf)
            x2 = Functions.roulette_Wheel_Function(list_Cdf)
            random_Value_Crossover = random.uniform(0.000,1.000)
            ch1 = Chromosome.Chromosome()
            ch2 = Chromosome.Chromosome()
            if(random_Value_Crossover<=universe_Input.crossover_Rate):
                if Crossover_Type == 'one point':
                    ch1.List_Genes,ch2.List_Genes =  Functions.single_Point_Crossover(universe_Input,list_Chromosome[x1].List_Genes,list_Chromosome[x2].List_Genes)
                    
                else:
                    ch1.List_Genes,ch2.List_Genes =  Functions.two_Point_Crossover(universe_Input,list_Chromosome[x1].List_Genes,list_Chromosome[x2].List_Genes)
                    
            else:
                ch1.List_Genes = list_Chromosome[x1].List_Genes
                ch2.List_Genes = list_Chromosome[x2].List_Genes
            list_Chromosome_After_Crossover.append(ch1)
            list_Chromosome_After_Crossover.append(ch2)
        #print('List Chromosomes After Crossover')
      #  for x in list_Chromosome_After_Crossover:
            #print(x.List_Genes)
        
               
        #عمل الطفران
        list_Chromosome_After_Mutation = []
        for x in list_Chromosome_After_Crossover:
            random_Value_Mutation = random.uniform(0.000,1.000)
            if(random_Value_Mutation<=universe_Input.mutation_Rate):
                Functions.mutation_Random_Bit(universe_Input,x)

            list_Chromosome_After_Mutation.append(x)
               
        
        #print('List Chromosomes After Mutation')
       # for x in list_Chromosome_After_Mutation:
            #print(x.List_Genes)
    
        list_Chromosome = list_Chromosome_After_Mutation.copy()
    
    
    
        
        
        
       
    
    


    
    
    #print('Sorted Generations')
  #  for x in sorted_Genereation:
        #print(x.best_Chromosome.Fitness)
        #print(x.best_Chromosome.List_Genes)
    

    #print('Best Solution')
    #print(sorted_Genereation[0].best_Chromosome.List_Genes)
    #print(sorted_Genereation[0].best_Chromosome.Fitness)


    #print('////////////////////////////////////////////')
    #print('////////////////////////////////////////////')
    #print('////////////////////////////////////////////')
    #print('************************ DONE ************************')
    #print('////////////////////////////////////////////')
    #print('////////////////////////////////////////////')
    #print('////////////////////////////////////////////')
    
    
    