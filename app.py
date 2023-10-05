import requests, json

# def delete():

def update(): 
    

def read():
    rid = input('Please enter the record ID you want to read: ')
    r = requests.get('http://127.0.0.1:5000/read')
    if r.status_code == 200:
        data = r.json()
        for x in data:
            if x.get('id')==rid:
                print(f"ID: {x.get('id')}")
                print(f"Title: {x.get('title')}")
                print(f"Description: {x.get('Description')}")


def create():
    rid = input('Please enter the record ID: ')
    rtitle = input('Please enter the record title: ')
    rdesc = input('Please enter the record description: ')

    data = {'id': rid, 'title': rtitle, 'desc': rdesc}

    r = requests.post('http://127.0.0.1:5000/create', json = data)

    if(r.status_code==200):
        print("Object created successfully")
    else:
        print("Creation failed, please try again")

    # print(r.content)

def main():
    # user = int(input("Hello what would you like to do\n(1) Create record\n(2) Read record\n(3) Update record\n(4) Delete record\n"))
    # using python 3.9 so unfortunately no switch or case statements
    state=0
    while(state==0):
        user = int(input("Hello what would you like to do\n(1) Create record\n(2) Read record\n(3) Update record\n(4) Delete record\n(5) Exit\n"))
        if(user == 1):
            create()
            # print('1')
        elif(user==2):
            read()
            # print('2')
        elif(user==3):
            print('3')
        elif(user==4):
            print('4')
        elif(user==5):
            print('Thanks for using the syster')
            state=1
        else:
            print('Please select a valid input')

if __name__ == "__main__":
    main()