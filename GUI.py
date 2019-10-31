import tkinter
import constant
import cpu
import random

State = [[None for _ in range(constant.grid)] for _ in range(constant.grid)]
root = tkinter.Tk()
main_canvas = tkinter.Canvas(root, height = 800, width = 800)

def create_grid():
    for i in range(constant.grid+1):
        main_canvas.create_line(constant.start+i*constant.grid_size, constant.start, constant.start+i*constant.grid_size, constant.start+constant.grid_size*constant.grid)
        main_canvas.create_line(constant.start, constant.start+i*constant.grid_size, constant.start+constant.grid_size*constant.grid ,constant.start+i*constant.grid_size)
rect = [[0 for _ in range(constant.grid)] for _ in range(constant.grid)]

def create_rect_touch():
    for i in range(constant.grid):
        for j in range(constant.grid):
            rect[i][j] = main_canvas.create_rectangle(constant.start+j*constant.grid_size+constant.rect_diff, constant.start+i*constant.grid_size+constant.rect_diff, constant.start+j*constant.grid_size+constant.grid_size-constant.rect_diff, constant.start+i*constant.grid_size+constant.grid_size-constant.rect_diff,fill = 'red')

create_grid()
create_rect_touch()

def insert_block(event):
    X = event.x
    Y = event.y
    y_val = (X-constant.start)//constant.grid_size
    x_val = (Y-constant.start)//constant.grid_size
    constant.state_change(y_val, State, main_canvas, 'u')
    cpu.cpu_turn(State, main_canvas)
    # print(State)

for i in range(constant.grid):
    for j in range(constant.grid):
        main_canvas.tag_bind(rect[i][j], '<Button-1>', insert_block)
# cpu.cpu_turn(State, main_canvas)
constant.state_change(random.randint(0, 4), State, main_canvas, 'p')
main_canvas.pack()
root.mainloop()
