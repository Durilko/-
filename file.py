links1 = open("Ссылки1.txt")
links2 = open("Ссылки2.txt")


links1 = links1.read().splitlines()
links2 = links2.read().splitlines()


same_links = [] # ссылки которые повторы 
different_links = [] # ссылки которые НЕ повторы


for link in links1 :
    if link in links2:
        same_links.append(link)
    else :
        different_links.append(link)

for link in links2 :
    if link in links1:
        same_links.append(link)
    else :
        different_links.append(link)

        
same_links = set(same_links) # удаляем повторяющиеся в повторах
different_links = set(different_links) # удаляем повторяющиеся в не повторах




