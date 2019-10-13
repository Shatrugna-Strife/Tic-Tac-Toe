import tkinter

rect_diff = 10
start = 50
grid_size = 50
grid = 4
State = [[0 for _ in range(grid)] for _ in range(grid)]
root = tkinter.Tk()
main_canvas = tkinter.Canvas(root, height = 800, width = 800)
def create_grid():
    for i in range(grid+1):
        main_canvas.create_line(start+i*grid_size, start, start+i*grid_size, start+grid_size*grid)
        main_canvas.create_line(start, start+i*grid_size, start+grid_size*grid ,start+i*grid_size)
rect = [[0 for _ in range(grid)] for _ in range(grid)]
def create_rect_touch():
    for i in range(grid):
        for j in range(grid):
            rect[i][j] = main_canvas.create_rectangle(start+j*grid_size+rect_diff, start+i*grid_size+rect_diff, start+j*grid_size+grid_size-rect_diff, start+i*grid_size+grid_size-rect_diff,fill = 'red')
create_grid()
create_rect_touch()

def state_change(x, y):
    for _ range
    if State[][y]
    State[x][y] = 1
    main_canvas.create_oval(start+y*grid_size, start+x*grid_size, start+(y+1)*grid_size, start+(x+1)*grid_size, fill = 'green')

def insert_block(event):
    X = event.x
    Y = event.y
    y_val = (X-start)//grid_size
    x_val = (Y-start)//grid_size
    state_change(x_val, y_val)
    print(x_val, y_val)

for i in range(grid):
    for j in range(grid):
        main_canvas.tag_bind(rect[i][j], '<Button-1>', insert_block)

main_canvas.pack()
root.mainloop()
