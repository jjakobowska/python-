# getting familiar with local and global 

def First():
    print('First one')
    def spam():
        eggs = 99
        bacon =()
        print(eggs)
    def bacon():
        eggs = 0
        ham = 101
    spam() #output : 99

def Second():
    print('Second one')
    def spam():
        eggs = 99
        def bacon():
           eggs = 0
           print(eggs)
        print(eggs)
        bacon()
    spam() #output : 99 \ 0

def Third():
    print('Third one')
    def spam():
        eggs = 1
        print(eggs)
        bacon()
    def bacon():
        eggs = 0
        print(eggs)
    bacon()
    spam() #output : 0 \ 1 \ 0

def Fourh():
    print('Fourth one')
    def spam():
        print(eggs)
    eggs = 42
    spam()
    print(eggs) #output : 42 \ 42

First()
Second()
Third()
Fourh()
