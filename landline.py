#!/usr/bin/env python
# coding: utf-8

# # Metro Manila landline converter
# 

# #### Source: https://mb.com.ph/2019/10/04/migration-to-8-digit-landline-number-starts-october-6/
# The following are the 3-digit prefix for Globe and Innove which will require the assigned PTE identifier “7” at the beginning of the prefix: 210-219, 225, 238-239, 261, 263-266, 349, 358, 368-369, 473, 482, 500-509, 576-577, 585-587, 610-619, 621-625, 717-720, 728-730, 738-739, 744-748, 750-759, 791-799,900-910, 914-919, 933-934, 940, 943-946, 949-950, 954-960, 964, 966, 968, 970-976, 978, 980, 987, 989.
# 
# The following are the 3-digit prefix for Bayan which will require the assigned PTE identifier ”3” at the beginning of the prefix: 220-224, 226-228, 262, 377-394, 406-419, 427-428, 430-440, 443-450, 453-456, 466-469, 474, 480-481, 483-499.

# In[ ]:


def parse_list(raw):
    list = []
    tmp = raw.split(',')
    for entry in tmp:
        try: 
            n = [str(int(entry))]
        except ValueError:
            a, z = entry.split('-')
            n = [str(i) for i in range(int(a), int(z)+1)]
        list += n
    return list


# In[ ]:


def convert_landline(landline, masterlist):
    if landline == None:
        return None 
    try:
        if len(landline) != 13 and len(landline) != 14:
            return landline

        if landline[0:6] != '+63 02':
            return landline
        else:
            if len(landline) == 14:
                return '(02) ' + landline[6:10] + ' ' + landline[10:]
            else:
                mykey = 'pldt'
                tag = landline[6:9]
                keys = masterlist['entries'].keys()
                for key in keys:
                    if tag in masterlist['entries'][key]:
                        mykey = key 
                return '(02) ' + masterlist['prefix'][mykey] + landline[6:9] + ' ' + landline[9:] 
    except TypeError: 
        return landline
# In[ ]:


def make_masterlist():
    raw = {}
    raw['globe'] = '210-219, 225, 238-239, 261, 263-266, 349, 358, 368-369, 473, 482, 500-509, 576-577, 585-587, 610-619, 621-625, 717-720, 728-730, 738-739, 744-748, 750-759, 791-799,900-910, 914-919, 933-934, 940, 943-946, 949-950, 954-960, 964, 966, 968, 970-976, 978, 980, 987, 989'
    raw['bayantel'] = '220-224, 226-228, 262, 377-394, 406-419, 427-428, 430-440, 443-450, 453-456, 466-469, 474, 480-481, 483-499'
    prefix = {'globe': '7', 'bayantel': '3', 'pldt': '8'}
    masterlist = {'prefix': prefix, 'entries': {}}
    keys = raw.keys()
    for key in keys:
        masterlist['entries'][key] = parse_list(raw[key])
    return masterlist


# In[ ]:


masterlist = make_masterlist()


# In[ ]:




