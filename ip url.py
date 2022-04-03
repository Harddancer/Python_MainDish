# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 :57:08 2021

@author: mvandron
"""
# Resolve DNS with user_choice host
import pandas as p
import dns
import dns.resolver
df = p.read_excel('URL.xlsx', sheet_name='url')
h = df['url'].values.tolist()
#print(h)
main_list = []

for i in h:
    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = ['8.8.8.8'] # your DNS  host choice
    r = dns.resolver.resolve(i, 'a')
    host = [a.to_text() for a in r]
    #print(i,host)
    main_list.append([i,host])

df = p.DataFrame(main_list,columns=['url','host'])
print (df)
df.to_excel('./NEWHOST.xlsx')   
    

