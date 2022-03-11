#!/usr/bin/env python
# coding: utf-8

# In[14]:


months = ["January", "February", "March", "April", "May", "June", 
"July", "August", "September", "October", "November", "December"]


def date_passed(todays_date, scheduled_date):
    
    dateA, monthA = todays_date.split(" ")
    dateB, monthB = scheduled_date.split(" ")
    
    dateA = int(dateA[:-2])
    dateB = int(dateB[:-2])
    
    monthA = months.index(monthA) + 1
    monthB = months.index(monthB) + 1
    
    if monthA > monthB:
        return True
    if monthA < monthB:
        return False
    
    if dateA > dateB:
        return True
    else:
        return False
    
    
print(date_passed("11th March", "26th March"))


# In[16]:


def unique_letters(word):
    ans = []
    word = list(set(word))
    
    for i in word:
        if i.isalpha():
            i = i.upper()
            if i not in ans:
                ans.append(i)
    
    return ans, len(ans)

print(unique_letters("charming"))


# In[ ]:




