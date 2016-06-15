with open("3.txt") as files:
    lines = files.readlines()
    lines = [l for l in lines ]
    lines_seen = set()
    with open("stockinfo.txt", "w+") as myfile:
        for item in lines:
            if item not in lines_seen:
                if 'Stock Quote' in item :
                    myfile.writelines(item.replace('Stock Quote',' '))
                    myfile.write(item.replace(item,'http://www.marketwatch.com/investing/Stock/',1))
                    myfile.writelines(item.splitlines())
                    myfile.writelines(item.decode())
                    lines_seen.add(item)
                    stock= list(lines_seen)
                    stock.sort()
                

                   
myfile.close()
     
##.split('Stock Quote')
