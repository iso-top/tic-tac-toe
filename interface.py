from tkinter import *
from tkinter import ttk 

start_play = False
# Глобальная переменная для отслеживания количества ходов
move_count = 0
flug_move_1 = True

# Флаги для каждой клетки (True - клетка пуста, False - клетка занята)
flags = {
	"cell_1": True,  # Левая верхняя клетка
	"cell_2": True,  # Средняя верхняя клетка
	"cell_3": True,  # Правая верхняя клетка
	"cell_4": True,  # Левая средняя клетка
	"cell_5": True,  # Центральная клетка
	"cell_6": True,  # Правая средняя клетка
	"cell_7": True,  # Левая нижняя клетка
	"cell_8": True,  # Средняя нижняя клетка
	"cell_9": True   # Правая нижняя клетка
}

def click_events(event):
	global move_count  # Используем глобальный счетчик ходов
	x, y = event.x, event.y

	# Проверяем, чей ход (крестики или нолики)
	flug_move = move_count % 2 == 0  # True для крестиков, False для ноликов

	# Левая верхняя клетка
	if (x >= 100 and x <= 390) and (y >= 100 and y <= 390):
		if flags["cell_1"]:  # Если клетка пуста
			if flug_move:
				# Крестик
				canvas.create_line(110, 110, 370, 370, width=6, fill='red')
				canvas.create_line(110, 370, 370, 110, width=6, fill='red')
			else:
				# Нолик
				canvas.create_oval(110, 110, 370, 370, width=6, outline='blue')
			flags["cell_1"] = False  # Занимаем клетку
			move_count += 1  # Увеличиваем счетчик ходов

	# Средняя верхняя клетка
	elif (x >= 390 and x <= 640) and (y >= 100 and y <= 390):
		if flags["cell_2"]:
			if flug_move:
				canvas.create_line(400, 110, 630, 370, width=6, fill='red')
				canvas.create_line(400, 370, 630, 110, width=6, fill='red')
			else:
				canvas.create_oval(400, 110, 630, 370, width=6, outline='blue')
			flags["cell_2"] = False
			move_count += 1

	# Правая верхняя клетка
	elif (x >= 640 and x <= 900) and (y >= 100 and y <= 390):
		if flags["cell_3"]:
			if flug_move:
				canvas.create_line(650, 110, 890, 370, width=6, fill='red')
				canvas.create_line(650, 370, 890, 110, width=6, fill='red')
			else:
				canvas.create_oval(650, 110, 890, 370, width=6, outline='blue')
			flags["cell_3"] = False
			move_count += 1

	# Левая средняя клетка
	elif (x >= 100 and x <= 390) and (y >= 390 and y <= 640):
		if flags["cell_4"]:
			if flug_move:
				canvas.create_line(110, 400, 370, 630, width=6, fill='red')
				canvas.create_line(110, 630, 370, 400, width=6, fill='red')
			else:
				canvas.create_oval(110, 400, 370, 630, width=6, outline='blue')
			flags["cell_4"] = False
			move_count += 1

	# Центральная клетка
	elif (x >= 390 and x <= 640) and (y >= 390 and y <= 640):
		if flags["cell_5"]:
			if flug_move:
				canvas.create_line(400, 400, 630, 630, width=6, fill='red')
				canvas.create_line(400, 630, 630, 400, width=6, fill='red')
			else:
				canvas.create_oval(400, 400, 630, 630, width=6, outline='blue')
			flags["cell_5"] = False
			move_count += 1

	# Правая средняя клетка
	elif (x >= 640 and x <= 900) and (y >= 390 and y <= 640):
		if flags["cell_6"]:
			if flug_move:
				canvas.create_line(650, 400, 890, 630, width=6, fill='red')
				canvas.create_line(650, 630, 890, 400, width=6, fill='red')
			else:
				canvas.create_oval(650, 400, 890, 630, width=6, outline='blue')
			flags["cell_6"] = False
			move_count += 1

	# Левая нижняя клетка
	elif (x >= 100 and x <= 390) and (y >= 640 and y <= 900):
		if flags["cell_7"]:
			if flug_move:
				canvas.create_line(110, 650, 370, 890, width=6, fill='red')
				canvas.create_line(110, 890, 370, 650, width=6, fill='red')
			else:
				canvas.create_oval(110, 650, 370, 890, width=6, outline='blue')
			flags["cell_7"] = False
			move_count += 1

	# Средняя нижняя клетка
	elif (x >= 390 and x <= 640) and (y >= 640 and y <= 900):
		if flags["cell_8"]:
			if flug_move:
				canvas.create_line(400, 650, 630, 890, width=6, fill='red')
				canvas.create_line(400, 890, 630, 650, width=6, fill='red')
			else:
				canvas.create_oval(400, 650, 630, 890, width=6, outline='blue')
			flags["cell_8"] = False
			move_count += 1

	# Правая нижняя клетка
	elif (x >= 640 and x <= 900) and (y >= 640 and y <= 900):
		if flags["cell_9"]:
			if flug_move:
				canvas.create_line(650, 650, 890, 890, width=6, fill='red')
				canvas.create_line(650, 890, 890, 650, width=6, fill='red')
			else:
				canvas.create_oval(650, 650, 890, 890, width=6, outline='blue')
			flags["cell_9"] = False
			move_count += 1


def create_bord():
	global canvas
	# Создаем фрейм с границей
	frame = Frame(root, bg="black", bd=8)
	frame.pack(anchor=CENTER, expand=1, padx=10, pady=10)# Устанавливаем отстg
	# Создаем Canvas внутри фрейма
	canvas = Canvas(frame, bg="#4d2046", width=1000, height=1000,highlightthickness=0)
	canvas.pack()
	canvas.create_line(390, 100, 390, 900, width=6)
	canvas.create_line(640, 100, 640, 900, width=6)
	canvas.create_line(100, 390, 900, 390, width=6)
	canvas.create_line(100, 640, 900, 640, width=6)

	# Привязываем событие клика левой кнопкой мыши к функции draw_shape
	canvas.bind("<Button-1>", click_events)

def click_play():
	play_btn.config(state=DISABLED)
	create_bord()

root = Tk()
#задний фон
root['bg'] = "#4d2046"
#Имя окна
root.title("Tic Tac Toe")

#Добавление иконки игры в окне
root.iconbitmap(default="images/Cage.ico")
#Окно в режиме fullscreen
root.attributes("-fullscreen", True)

#создание кнопки и добавление ее отображение
play_btn = ttk.Button(text="Play",width=100,command = click_play)
play_btn.pack()

#Бесконечная работа tkinter окон
root.mainloop()