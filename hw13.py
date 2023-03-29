
import tkinter as tk
import random

#==========================================
# Purpose: SnakeGUI is a graphical user interface that initializes other class objects into a game 
# Instance variables: self.win: tkinter window, self.canvas: a tkinter object with specific dimensions,
# self.board: the game board boundaries, self.snake: a Snake class object that is user controlled,
# self.enemy: an Enemy class object which competes against the player's self.snake,
# self.pellet: a Pellet class object that the snake and enemy compete for
# Methods: eat_food: creates a new segment for whichever snake or enemy gets it, find_food: tells the enemy snake where to go,
# enemy_collision: checks for the enemy snake hitting the player controlled snake and vice versa,
# gameloop: calls itself and all the method functions every 100ms, restart: creates a new game when user presses 'r'
#==========================================
class SnakeGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.canvas = tk.Canvas(width = 660, height = 660)
        self.canvas.pack()
        self.board = self.canvas.create_rectangle(30, 30, 630, 630)
        self.snake = Snake(330,330,'Green',self.canvas)
        self.enemy = Enemy(180,180,'Purple',self.canvas)
        self.pellet = Pellet(self.canvas, 'Brown')
        self.super = SuperPellet(self.canvas, 'Gold')
        self.win.bind('<Down>',self.snake.go_down)
        self.win.bind('<Up>',self.snake.go_up)
        self.win.bind('<Right>',self.snake.go_right)
        self.win.bind('<Left>',self.snake.go_left)
        self.win.bind('r',self.restart)
        self.new_game = False
        self.gameloop()

    def end_screen(self):
        length = len(self.snake.segments)
        text_str = 'Game over, score = {}\n Number of Specail Pellets consumed = {}'.format(length, self.super.num_eat)
        end = self.canvas.create_text(330, 330, text= text_str )
        
    def eat_food(self):
        colors = ['Red', 'Orange', 'Yellow', 'Blue', 'Pink', 'Silver']
        numbers = [1,2,3,4]
        if self.snake.x == self.pellet.fx and self.snake.y == self.pellet.fy:
            self.pellet.new_pellet()
            new = self.canvas.create_rectangle(self.snake.x, self.snake.y, self.snake.x+30, self.snake.y+30, fill = self.snake.color)
            new_lst = [self.snake.x, self.snake.y, self.snake.x+30, self.snake.y+30]
            self.snake.segments.append(new)
            self.snake.segment_pos.append(new_lst)
            self.super.new_pellet()
        elif self.enemy.x == self.pellet.fx and self.enemy.y == self.pellet.fy:
            self.pellet.new_pellet()
            new_enemy = self.canvas.create_rectangle(self.enemy.x, self.enemy.y, self.enemy.x+30, self.enemy.y+30, fill = self.enemy.color)
            enemy_lst = [self.enemy.x, self.enemy.y, self.enemy.x+30, self.enemy.y+30]
            self.enemy.segments.append(new_enemy)
            self.enemy.segment_pos.append(enemy_lst)
            self.super.new_pellet()
        if self.snake.x == self.super.fx and self.snake.y == self.super.fy: #extra credit part VIII. - my own idea to create a new food that changes a snake's color
            idx = random.randint(0,5)
            self.snake.color = colors[idx]
            self.super.new_pellet()
            self.super.num_eat += 1
        elif self.enemy.x == self.super.fx and self.enemy.y == self.super.fy:
            idx = random.randint(0,5)
            self.enemy.color = colors[idx]
            self.super.new_pellet()

    def find_food(self):
            if self.enemy.x < self.pellet.fx and self.enemy.vx != 30: #implemented extra credit part V. - enemy cannot reverse directions
                self.enemy.vx = 30
                self.enemy.vy = 0
                self.enemy.turn_lst.append('r')
            elif self.enemy.x == self.pellet.fx: #y direction movement
                if self.enemy.y < self.pellet.fy and self.enemy.vy != 30:
                    self.enemy.vy = 30
                    self.enemy.vx = 0
                    self.enemy.turn_lst.append('d')
                elif self.enemy.y > self.pellet.fy and self.enemy.vy != -30:
                    self.enemy.vy = -30
                    self.enemy.vx = 0
                    self.enemy.turn_lst.append('u')
            elif self.enemy.x > self.pellet.fx and self.enemy.vx != -30:
                self.enemy.vx = -30
                self.enemy.vy = 0
                self.enemy.turn_lst.append('l')

    def enemy_collision(self):
        if self.enemy.pos_lst in self.snake.segment_pos:
            self.enemy.vx = 0
            self.enemy.vy = 0
            self.snake.vx = 0
            self.snake.vy = 0
            self.end_screen()
            self.new_game = True
            return False
        elif self.snake.pos_lst in self.enemy.segment_pos:
            self.enemy.vx = 0
            self.enemy.vy = 0
            self.snake.vx = 0
            self.snake.vy = 0
            self.end_screen()
            self.new_game = True
            return False
        
    def gameloop(self):
        if Snake.move(self.snake) != False and self.enemy_collision() != False:
            self.eat_food()
            self.find_food()
            self.enemy_collision()
            Enemy.move(self.enemy)
            self.enemy_collision() #checking for a collision after user moves and after enemy moves
            self.canvas.after(200, self.gameloop)
        else:
            self.end_screen()
            self.new_game = True
        

    def restart(self,event):
        if self.new_game == True:
            self.canvas.delete(tk.ALL)
            self.board = self.canvas.create_rectangle(30, 30, 630, 630)
            self.snake = Snake(330,330,'Green',self.canvas)
            self.enemy = Enemy(180,180,'Purple',self.canvas)
            self.pellet = Pellet(self.canvas, 'Brown')
            self.super = SuperPellet(self.canvas, 'Gold')
            self.win.bind('<Down>',self.snake.go_down)
            self.win.bind('<Up>',self.snake.go_up)
            self.win.bind('<Right>',self.snake.go_right)
            self.win.bind('<Left>',self.snake.go_left)
            self.win.bind('r',self.restart)
            self.new_game = False
            self.gameloop()
            
#==========================================
# Purpose: Pellet objects represents a food pellet that Snake and Enemy classes interact with to grow longer
# Instance variables: canvas: the game board canvas, fx: x position of pellet, fy: y position of pellet,
# pellet: a tkinter oval object, foods: a list holding the current self.pellet informaiton
# Methods: new_pellet: creates a new pellet at a random position
#==========================================
class Pellet:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.fx = random.randrange(30,630,30) #food pellet cords
        self.fy = random.randrange(30,630,30)
        self.color = color
        self.pellet = self.canvas.create_oval(self.fx, self.fy, self.fx+30, self.fy+30, fill = self.color)
        self.foods = [self.pellet]

    def new_pellet(self): #places new food pellet
        self.fx = random.randrange(30,630,30) 
        self.fy = random.randrange(30,630,30)
        self.pellet = self.canvas.create_oval(self.fx, self.fy, self.fx+30, self.fy+30, fill = self.color)
        self.foods.insert(0, self.pellet)
        f = self.foods.pop()
        self.canvas.delete(f)
        
#==========================================
# Purpose: SuperPellet objects are derived from pellet class
# Instance variables: canvas: the game board canvas, fx: x position of pellet, fy: y position of pellet,
# pellet: a tkinter oval object, foods: a list holding the current self.pellet informaiton, self.num_eat: a counter of pellets consumed by player controlled snake
# Methods: new_pellet: creates a new pellet at a random position
#==========================================
class SuperPellet(Pellet):
    def __init__(self, canvas, color):
        self.canvas = canvas
        super().__init__(canvas, color)
        self.num_eat = 0

    def new_pellet(self):
        Pellet.new_pellet(self)

                
#==========================================
# Purpose: Snake is a user controlled object of square links representing a snake
# Instance variables: x: x posittion, y: y position, color: snake color, canvas: a tkinter canvas for the game,
# vx: x velocity, vy: y velocity, snake: a tkinter rectangle object, segments: list of tkinter rectangles that the snake is made of,
# turn_lst: a list to track which direction the snake is moving, segment_pos: a list that stores the position of each snake rectangle position,
# pos_lst: a list of the rectangle coordinates which is updated into the segment_pos list
# Methods: move: illustrates the moving snake and updates its velocity and tracks its positon,
# end_screen: a string that gives information to the user at end of game, go____: functions that are called with user key presses and change snake velocity
#==========================================
class Snake:
    def __init__(self, x, y, color, canvas):
        self.x = x
        self.y = y
        self.color = color
        self.canvas = canvas
        self.vx = 30
        self.vy = 0
        self.snake = self.canvas.create_rectangle(x, y, x+30, y+30, fill = color)
        self.segments = [self.snake]
        self.turn_lst = ['r']
        self.segment_pos = []
        self.pos_lst = [self.x, self.y, self.x+30, self.y+30]
                   
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.snake = self.canvas.create_rectangle(self.x, self.y, self.x+30, self.y+30, fill = self.color)
        self.segments.insert(0, self.snake)
        z = self.segments.pop()
        self.canvas.delete(z)
        self.pos_lst = [self.x, self.y, self.x+30, self.y+30]
        self.segment_pos.append(self.pos_lst)
        self.segment_pos.pop(0)
        if self.pos_lst in self.segment_pos[:-1]:
            return False
        if self.x > 600 or self.x < 30: #Snake dies when it goes out of bounds
            self.vx = 0
            self.vy = 0
            return False
        if self.y > 600 or self.y < 30:
            self.vx = 0
            self.vy = 0
            return False

    def go_down(self,event):
        if self.turn_lst[-1] != 'u' and self.turn_lst[-1] != 'd': # implemented extra credit part I. - snake cannot reverse directions
            self.vx = 0
            self.vy = 30
            self.turn_lst.append('d')
        
    def go_up(self,event):
        if self.turn_lst[-1] != 'd' and self.turn_lst[-1] != 'u':
            self.vx = 0
            self.vy = -30
            self.turn_lst.append('u')
               
    def go_left(self,event):
        if self.turn_lst[-1] != 'r' and self.turn_lst[-1] != 'l':
            self.vx = -30
            self.vy = 0
            self.turn_lst.append('l')       
        
    def go_right(self,event):
        if self.turn_lst[-1] != 'l' and self.turn_lst[-1] != 'r':
            self.vx = 30
            self.vy = 0
            self.turn_lst.append('r')
            
#==========================================
# Purpose: An Enemy class object is similar to a Snake class but is not user controlled and has different movement rules
# Instance variables: same instance variables as Snake class object 
# Methods: move: illustrates the computer controlled snake and updates its velocity and tracks its positon
#==========================================
class Enemy:
    def __init__(self, x, y, color, canvas):
        self.x = x #tried doing an inherited class and using super().__init__() but for some reason this was causing the enemy snake animation to not work properlly 
        self.y = y
        self.color = color
        self.canvas = canvas
        self.vx = 30
        self.vy = 0
        self.snake = self.canvas.create_rectangle(x, y, x+30, y+30, fill = color)
        self.segments = [self.snake]
        self.segment_pos = []
        self.pos_lst = [self.x, self.y, self.x+30, self.y+30]
        self.turn_lst = ['r']

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.snake = self.canvas.create_rectangle(self.x, self.y, self.x+30, self.y+30, fill = self.color)
        self.segments.insert(0, self.snake)
        w = self.segments.pop()
        self.canvas.delete(w)
        self.pos_lst = [self.x, self.y, self.x+30, self.y+30]
        self.segment_pos.append(self.pos_lst)
        self.segment_pos.pop(0)

        


SnakeGUI()
tk.mainloop()
