# -*- coding: utf-8 -*-
"""
This is an attempt at writing a program to solve 
Words with Friends.

J. Butler, 12/26/2017
"""

#%%
#Library Imports
import random as rn
import matplotlib.pyplot as plt
import numpy as np
#%%
# Playing Board
board = np.zeros([11,11])

# Letter/Word Bonus Matrix
bonus=np.matrix([['TL',1,'TW',1,1,1,1,1,'TW',1,'TL'],
                [1,'DW',1,1,1,'DW',1,1,1,'DW',1],
                ['TW',1,'TL',1,'DL',1,'DL',1,'TL',1,'TW'],
                [1,1,1,'TL',1,1,1,'TL',1,1,1],
                [1,1,'DL',1,1,1,1,1,'DL',1,1],
                [1,'DW',1,1,1,1,1,1,1,'DW',1],
                [1,1,'DL',1,1,1,1,1,'DL',1,1],
                [1,1,1,'TL',1,1,1,'TL',1,1,1],
                ['TW',1,'TL',1,'DL',1,'DL',1,'TL',1,'TW'],
                [1,'DW',1,1,1,'DW',1,1,1,'DW',1],
                ['TL',1,'TW',1,1,1,1,1,'TW',1,'TL']])
#%%
# Dictionary
words = [line.rstrip('\n') for line in open('C:/Users/Jimmy/OneDrive/Cluster/Python Scripts/source.txt')]
for x in range(len(words)):
    words[x]=words[x]+"$"
words[1:5]

#%%
tiles="KJXQZBBCCMMPPFFHHVVWWYYGGGDDDDLLLLSSSSUUUUNNNNNNRRRRRRTTTTTTOOOOOOOOAAAAAAAAAIIIIIIIIIEEEEEEEEEEEE"
master=[]
handVals=[]

#Random Hand 



solns=[]
inp=input("Enter Letters Here: ")
hand=list(inp.upper())
'''
hand=[]
for x in range(0,7):
    hand.append(rn.choice(tiles))
'''
length=len(hand)

#Gives a list of words using current hand!
for x in range(0,length):
    var=hand[x]
    wtemp=[]
    for x in words:
        if x.startswith(var):
            wtemp.append(x)
    
    htemp=[]
    for num in range(0,len(hand)):
        htemp.append(hand[num])
    htemp.remove(var)

    for y in range(0,len(htemp)):
        vtemp=var+htemp[y]
        if (vtemp+"$") in wtemp:
            solns.append(vtemp)
            
        x2=htemp[y]    
        temp2=[]
        for num in range(0,len(htemp)):
            temp2.append(htemp[num])
        temp2.remove(x2)
        
        for z in range(0,len(temp2)):
            ztemp=vtemp+temp2[z]
            if (ztemp+"$") in wtemp:
                solns.append(ztemp)
            
            x3=temp2[z]
            temp3=[]
            for num in range(0,len(temp2)):
                temp3.append(temp2[num])
            temp3.remove(x3)
            
            for q in range(0,len(temp3)):
                qtemp=ztemp+temp3[q]
                if (qtemp+"$") in wtemp:
                    solns.append(qtemp)
                
                x4=temp3[q]
                temp4=[]
                for num in range(0,len(temp3)):
                    temp4.append(temp3[num])
                temp4.remove(x4)
                
                for t in range(0,len(temp4)):
                    ttemp=qtemp+temp4[t]
                    if (ttemp + "$") in wtemp:
                        solns.append(ttemp)
                    
                    x5=temp4[t]
                    temp5=[]
                    for num in range(0,len(temp4)):
                        temp5.append(temp4[num])
                    temp5.remove(x5)
                    
                    for b in range(0,len(temp5)):
                        btemp=ttemp+temp5[b]
                        if (btemp + "$") in wtemp:
                            solns.append(btemp)
                        
                        x6=temp5[b]
                        temp6=[]
                        for num in range(0,len(temp5)):
                            temp6.append(temp5[num])
                        temp6.remove(x6)
                        
                        for p in range(0,len(temp6)):
                            ptemp=btemp+temp6[p]
                            if (ptemp + "$") in wtemp:
                                solns.append(ptemp)
                            '''
                            x7=temp6[p]
                            temp7=[]
                            for num in range(0,len(temp6)):
                                temp7.append(temp6[num])
                            temp7.remove(x7)
                            
                            for i in range(0,len(temp7)):
                                itemp=ptemp+temp7[i]
                                if (itemp + "$") in wtemp:
                                    solns.append(itemp)
                            '''

sol=set(solns)
sol=list(sol)
handVals.append(len(sol))

for i in range(0,len(sol)):
    master.append(sol[i])


# Split words into length groups
s2=[];s3=[];s4=[];s5=[];s6=[];s7=[];#s8=[]
for word in master:
    if len(word)==2:
        s2.append(word)
    elif len(word)==3:
        s3.append(word)
    elif len(word)==4:
        s4.append(word)
    elif len(word)==5:
        s5.append(word)
    elif len(word)==6:
        s6.append(word)
    elif len(word)==7:
        s7.append(word)
    #elif len(word)==8:
    #   s8.append(word)
        


# Master list, associated point values, and statistics

pt1=['A','E','I','O','U','N','R','T','S','L']
pt2=['D','G']
pt3=['B','C','M','P']
pt4=['F','H','V','W','Y']
pt5=['K']
pt8=['J','X']
pt10=['Q','Z']

numbers_list=[]
s2_list=[]
s3_list=[]
s4_list=[]
s5_list=[]
s6_list=[]
s7_list=[]
words_list=[master,s2,s3,s4,s5,s6,s7]
master_list=[numbers_list,s2_list,s3_list,s4_list,s5_list,s6_list,s7_list]
for x in range(0,len(words_list)):
    for word in words_list[x]:
        numbers=[]
        for lett in word:
            if lett in pt1:
                numbers.append(1)
            elif lett in pt2:
                numbers.append(2)
            elif lett in pt3:
                numbers.append(3)
            elif lett in pt4:
                numbers.append(4)
            elif lett in pt5:
                numbers.append(5)
            elif lett in pt8:
                numbers.append(8)
            elif lett in pt10:
                numbers.append(10)
        master_list[x].append(sum(numbers))

if len(s2_list) >= 1:
    ind2=np.argmax(s2_list)
    print('Best 2 Letter Word is : ',s2[ind2], ': ', s2_list[ind2], 'Points' )
    
if len(s3_list) >= 1:
    ind3=np.argmax(s3_list)
    print('Best 3 Letter Word is : ',s3[ind3], ': ', s3_list[ind3], 'Points' )
    
if len(s4_list) >= 1:
    ind4=np.argmax(s4_list)
    print('Best 4 Letter Word is : ',s4[ind4], ': ', s4_list[ind4], 'Points' )

if len(s5_list) >= 1:
    ind5=np.argmax(s5_list)
    print('Best 5 Letter Word is : ',s5[ind5], ': ', s5_list[ind5], 'Points' )

if len(s6_list) >= 1:
    ind6=np.argmax(s6_list)
    print('Best 6 Letter Word is : ',s6[ind6], ': ', s6_list[ind6], 'Points' )

if len(s7_list) >= 1:
    ind7=np.argmax(s7_list)
    print('Best 7 Letter Word is : ',s7[ind7], ': ', s7_list[ind7], 'Points' )




#%%
print(' Max Value is:  ', max(numbers_list),'\n',
      'Mean Value is: ',np.mean(numbers_list),'\n',
      'Variance is:   ',np.var(numbers_list),'\n',
      'Median is:     ',np.median(numbers_list))


#%% 
# Points

plt.figure(figsize=(8,5),dpi=200)
plt.hist(numbers_list,alpha=0.7,color='red',rwidth=0.8,bins=25)
plt.ylabel('Frequency')
plt.xlabel('Point Values')
plt.title('Distribution of Point Values')
plt.text(20,3500,'E(x)=5.09')
plt.text(20,3200,'V(x)=5.67')
#%%
# Plot of the PMF
        

total=len(master)
lens=[len(s2)/total,len(s3)/total,len(s4)/total,len(s5)/total,len(s6)/total,len(s7)/total]

objects=('2','3','4','5','6','7')
y_pos=np.arange(len(objects))
plt.figure(figsize=(8,5),dpi=200)
plt.bar(y_pos, lens,align='center', alpha=0.7,color="#3CE74C")

plt.xticks(y_pos,objects)
plt.ylabel("Frequency")
plt.xlabel("Number of Letters in Word")
plt.title("Distribution of Word Lengths")
plt.show()


#%%
#Unique Hands
plt.figure(figsize=(8,5),dpi=200)
plt.hist(handVals,alpha=0.7,color='blue',rwidth=0.8,bins=40)
plt.ylabel('Frequency')
plt.xlabel('Number of Unique Words')
plt.title('Unique Words in a Scrabble Hand')
plt.text(200,100,'E(x)=45.87')
plt.text(200,90,'V(x)=1104.2')
plt.show()
print(np.mean(handVals),np.var(handVals))


#%%
np.std(handVals)










