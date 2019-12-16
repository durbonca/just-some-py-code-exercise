def run():
    counter=0
    with open ('file.txt') as f:
        data = f.read()
        words = data.split()    
        print(words)
        num_words = len(words)

        print("el numero de palabras del CV son {} y el precio a calcular seria: $ {}".format(num_words, num_words*20))



if __name__ == "__main__":
    run()