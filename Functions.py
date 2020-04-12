import random

#تابع توليد الكروموسوم العشوائي
def build_Chromosome_Randomly(universe_Input):
    list_Random_Sets = []
    for j in range(1,universe_Input.set_Count+1):
        temp = random.uniform(0.000,1.000)
        if temp < 0.500:
            list_Random_Sets.append(0)
        else:
            list_Random_Sets.append(1)
    return list_Random_Sets

# لمعرفة إذا الحل صحيح
def check_If_Valid(set_Temp,universe_Input):
    x = len(set_Temp)
    y = len(universe_Input.list_Universe_Items)
    if x==y:
        return True
    else:
        return False

    #لتقدير مدى الحطأ
def check_Chromosome_Error_Rate(universe_Input,temp_set):
    x = universe_Input.universe_Size
    y = len(temp_set)
    if (x-y)<=(x/2):
        return True
    else:
        return False

    #تابع تعاودي لإيجاد كروموسوم صحيح
def fixing_Chromosome_Randomly(universe_Input):
    chromosome = build_Chromosome_Randomly(universe_Input)
    status = chromosom_Is_Correct(chromosome,universe_Input)
    if status == True:
        return chromosome
    else:
       chromosome = fixing_Chromosome_Randomly(universe_Input)

    return chromosome

        #تابع الإصلاح خطياً
def fixing_Chromosome_Linear(chromosome,universe_Input):
    gene_Index = 0
    for gene in chromosome:
        if gene ==0:
            chromosome[gene_Index]=1
            status = chromosom_Is_Correct(chromosome,universe_Input)
            if status == True:
                break        
        gene_Index+=1

    return chromosome

#تابع التحقق من صحة الكروموسوم
def chromosom_Is_Correct(chromosome,universe_Input):
    set_Temp = chromosome_Get_Sets(chromosome,universe_Input)
    status = check_If_Valid(set_Temp,universe_Input)
    return status

#تابع الحصول على مجموعة من كروموسوم
def chromosome_Get_Sets(chromosome,universe_Input):
    index = 0
    set_Temp = set()
    for gene in chromosome:
        if gene==1:
           set_Temp.update(universe_Input.list_Sets[index].list_set)
        index+=1
    return set_Temp

#تابع حساب التكلفة وعدد الواحدات
def calculate_Costs_And_ActiveBits(universe_Input,chromosome):
    index = 0
    sum_Costs=0.0
    active_Bits=0
    for gene in chromosome.List_Genes:
        if gene==1:
           sum_Costs += universe_Input.list_Sets[index].set_Cost
           active_Bits+=1
        index+=1
    chromosome.Count_Active_Bits = active_Bits
    chromosome.sum_Costs = sum_Costs

#تابع حساب الفيتنس
def calculate_Fitness(universe_Input,chromosome):
    a = 0.8
    b = 0.2
    x = chromosome.sum_Costs
    y = chromosome.Count_Active_Bits
    chromosome.Fitness = (1.0/(a*x + b*y))



#تابع حساب الاحتمال التراكمي
def pdf_Cdf_Functions(list_Chromosome):
    sum_Fitness = 0.0
    for x in list_Chromosome:
        sum_Fitness+=x.Fitness
    list_Pdf = []
    for x in list_Chromosome:
        list_Pdf.append(x.Fitness/sum_Fitness)
    list_Cdf = []
    temp=0
    for x in list_Pdf:
        temp += x
        list_Cdf.append(temp)
    return list_Cdf

#تابع الرولت وييل
def roulette_Wheel_Function(list_Cdf):
    random_Value = random.uniform(0.000,1.000)
    index =0
    for x in list_Cdf:
        if(random_Value<=x):
            break;
        index+=1
    return index

#تابع سينجل بوينت
def single_Point_Crossover(universe_Input,first,second):

    random_Point = random.randint(0,universe_Input.set_Count-1)
    new_First = first.copy()
    new_Second = second.copy()
    for i in range(random_Point,len(first)):
        new_First[i] = second[i]
    for i in range(random_Point,len(second)):
        new_Second[i] = first[i]
    return new_First,new_Second


#تابع تو بوينت
def two_Point_Crossover(universe_Input,first,second):

    random_Point1 = random.randint(0,universe_Input.set_Count-1)
    random_Point2 = random.randint(0,universe_Input.set_Count-1)
    if(random_Point1>=random_Point2):
        start = random_Point2
        end = random_Point1
    else:
        start = random_Point1
        end = random_Point2
    new_First = first.copy()
    new_Second = second.copy()
    for i in range(start,end):
        new_First[i] = second[i]
    for i in range(start,end):
        new_Second[i] = first[i]
    return new_First,new_Second


#تابع الطفران
def mutation_Random_Bit(universe_Input,chromosome):
    random_Value = random.randint(0,universe_Input.set_Count-1)
    gene_Randomly = chromosome.List_Genes[random_Value]
    if gene_Randomly == 1:
        chromosome.List_Genes[random_Value] = 0
    else:
        chromosome.List_Genes[random_Value] = 1

