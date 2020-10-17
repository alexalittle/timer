import tkinter as tk

class Timer:

	def __init__(self, start_len):
		self.start_len = Timer.min_to_sec(start_len)
		self.current_len = Timer.min_to_sec(start_len)
		self.running = None

	def __repr__(self):
		minutes = Timer.sec_to_min(self.start_len)
		return f"A {minutes} timer"

	def reset(self):
		self.current_len = self.start_len

	@classmethod
	def sec_to_min(cls, seconds):
		""" given input in seconds, returns equivalent value in minutes (0:00 string) """
		calculation = divmod(seconds, 60)
		if calculation[1] < 10:
			output = "0" + str(calculation[1])
		else:
			output = str(calculation[1])
		return str(calculation[0]) + ":" + output

	@classmethod
	def min_to_sec(cls, minutes):
		""" given input in 0:00 format, returns equivalent value in seconds """
		vals = minutes.split(":")
		return (int(vals[0]) * 60) + int(vals[1])
		

window = tk.Tk()

my_timer = Timer("0:00")

title = tk.Label( text = "Timer")
title.pack()

timer_display = tk.Label(text = Timer.sec_to_min(my_timer.current_len))
timer_display.pack()

minutes_label = tk.Label(text = "Add Minutes")
minutes_plus_btn = tk.Button(text = "+")
minutes_minus_btn = tk.Button(text = "-")

minutes_label.pack()
minutes_plus_btn.pack()
minutes_minus_btn.pack()

timer_start_btn = tk.Button(text = "Start")

def start_timer(event):
	timer1 = Timer(timer_display["text"])
	return run_timer(timer1)

def run_timer(my_timer):
	timer_display["text"] = Timer.sec_to_min(my_timer.current_len)
	if my_timer.current_len > 0:
		my_timer.current_len -= 1
		my_timer.running = window.after(1000, lambda: run_timer(my_timer))
	else:
		timer_display["text"] = "DONE"
		window.bell()

timer_start_btn.pack()
timer_start_btn.bind("<Button-1>", start_timer)

def stop_timer(event):
	pass

timer_stop = tk.Button(
	text = "Stop",
	foreground = "black")

timer_stop.pack()
timer_stop.bind("<Button-1>", stop_timer)

window.mainloop()