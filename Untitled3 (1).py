#!/usr/bin/env python
# coding: utf-8

# In[1]:


#soal 1
number = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
a=0
while a < len(number):
    if number[a] % 2 == 1:
        print(number[a])
    if number[a] == 553:
        break
    a+=1


# In[3]:


#soal 2 output
count = 0
for i in range(1,20,2):
    count+=1
print(count)


# In[4]:


#soal 3
for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()


# In[3]:


nama="Muhammad Raffi Arjuna"
print(nama)
nim="0110123192"
print(nim)
rombel="SI05"
print(rombel)


# In[ ]:




