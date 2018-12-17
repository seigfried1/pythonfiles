# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:58:29 2018

@author: RAHUL MISHRA
"""

#names = ['rahul', 'magic', 'curator', 'pixel', 'lagoon', 'nancy', 'jazz',\
#'luhar', 'rohit', 'tiger', 'roxy']
# print(names)
names2 = "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia\
croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus\
heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred\
lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir\
poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking\
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko\
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"

#names2 = "audino bagon etihad baltoy banette bidoof braviary owl love"
names2_list = names2.split(' ')
# print(names2_list)


final_list = []
for i in names2_list:
    sub_list = []
    sub_list.append(i)
    count = 0
    while count < len(names2_list):
        if sub_list[-1][-1] == names2_list[count][0]:
            if names2_list[count] not in sub_list:
                sub_list.append(names2_list[count])
                count = 0
                #print(len(sub_list))
            count += 1
        else:
            count += 1
    final_list.append(sub_list)

a = sorted(final_list, key=len)
print(a[-1])









# final_list = []
# for i in names2_list:
# 	sub_list = []
# 	sub_list.append(i)
# 	should_restart = True
# 	while should_restart:
# 		should_restart = False
# 		for j in names2_list:
# 			if sub_list[-1][-1] == j[0]:
# 				sub_list.append(j)
# 				should_restart = True
# 				break
# 		final_list.append(sub_list)
# print(final_list)
