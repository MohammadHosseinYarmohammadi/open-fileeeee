def main():
    with open("f.txt","w") as f:
        for i in range(1, 6):
            print(f'person{i}: ')
            name = input("please enter your name: ")
            password = input("please enter your password: ")
            id = input("please enter your id: ")
            f.write(f'name: {name},   pass: {password},   id: {id}')
            f.write('\n')

main()