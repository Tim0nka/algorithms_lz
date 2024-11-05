import random
#создаем список через рандом
list1 = []
for i in range(10):
    list1.append(random.randint(0,1000000))          

def max(list1):
    answer = list1.sort()
    list1.pop()

    return max  
#выводим наш полученный список



#копируем список для второй сортировки
list2 = list1.copy()


#сортировка пузырьком
def bubble_sort(list1):
    #длина сортируемого списка
    n=len(list1)
    #создаем счетчик сравнений
    x = 0
    #бесконечный цикл 
    while(True): 
         #вывод до                         
        for i in range(n):                     
             print(list1[i],end=' ')
        #количество перестановок
        c=0
        #главный цикл сравнения                                    
        for i in range(n-1):
            #если i-й и (i+1)-й стоят в неправильном порядке            
            if list1[i+1]>list1[i]:
                x +=1
                #меняем их местами                
                list1[i+1],list1[i]=list1[i],list1[i+1]
                #увеличиваем счетчик перестановок 
                c+=1  
        #вывод после                       
        for i in range(n):                     
             print(list1[i],end=' ')
        #если перестановок не было, то массив будет готов
        if c==0:
            print(x)                                
            break

list1 = bubble_sort(list1)


#сортировка выбором
def elect_sort(list2):
    #создаем счетчик сравнений
    y = 0
    # длина списка 
    n=len(list2)                                    
    # главный цикл
    for i in range(n):         
        print("До    :",list2)   
        # ищем минимум на отрезке [i,n-1]
        mi=list2[i] 
        ii=i
        for j in range(i,n): 
            if list2[j]<mi:
                y +=1
                # минимум
                mi=list2[j]       
                # его позиция
                ii=j                 
                # меняем i-й с минимумом 
        list2[i],list2[ii]=list2[ii],list2[i]       
        print("После :",list2)
        print()

list2 = elect_sort(list2)