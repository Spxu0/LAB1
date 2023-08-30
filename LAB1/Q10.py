while 1 :
    num1 = int(input('Enter start number:'))
    if num1 ==00:
        print('good bye')
        break
    num2 = int(input('Enter end number:'))
    
    sum=0
    for n in range(num1,num2+1,1):
        sum+=n
    print(sum)    