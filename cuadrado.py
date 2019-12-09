import turtle

def main():
        window = turtle.Screen()
        david = turtle.Turtle()
        draw(david)

def draw(david):
        lengh = int(input('ingresar largo: '))
        for i in range (0,4):
            line(david, lengh)

def line(david, lengh):
        david.forward(lengh)
        david.left(90)

if __name__ == '__main__':
    main()
    turtle.mainloop()