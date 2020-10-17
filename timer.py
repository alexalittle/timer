import tkinter as tk

class App:
	def __init__(self, master):
		frame = tk.Frame(master)
		frame.pack()

		# set attributes for start time, current time
		self.start_time = 0
		self.current_time = 0

		# set up labels
		self.title = tk.Label(frame, text = "Timer")
		self.timer_display = tk.Label(frame, text = "0:00")

		# create start, stop, reset buttons
		self.start_btn = tk.Button(frame, text="Start", command = self.start_timer)
		self.stop_btn = tk.Button(frame, text="Stop", command = self.stop_timer)
		self.reset_btn = tk.Button(frame, text="Reset", command = self.reset_timer)

		# create section for adding minutes
		self.minutes_label = tk.Label(frame, text = "Add Minutes")
		self.minutes_plus_btn = tk.Button(frame, text = "+", command = lambda: self.change_time(60))
		self.minutes_minus_btn = tk.Button(frame, text = "-", command = lambda: self.change_time(-60))

		#create section for adding seconds
		self.seconds_label = tk.Label(frame, text = "Add Seconds")
		self.seconds_plus_btn = tk.Button(frame, text = "+", command = lambda: self.change_time(1))
		self.seconds_minus_btn = tk.Button(frame, text = "-", command = lambda: self.change_time(-1))

		# pack elements into the frame
		self.title.pack()
		self.timer_display.pack()

		self.start_btn.pack()
		self.stop_btn.pack()
		self.reset_btn.pack()

		self.minutes_label.pack()
		self.minutes_plus_btn.pack()
		self.minutes_minus_btn.pack()

		self.seconds_label.pack()
		self.seconds_plus_btn.pack()
		self.seconds_minus_btn.pack()

	def start_timer(self):
		"""timer1 = Timer(timer_display["text"])
		return run_timer(timer1)"""
		pass

	def run_timer(my_timer):
		"""
		timer_display["text"] = Timer.sec_to_min(my_timer.current_len)
		if my_timer.current_len > 0:
			my_timer.current_len -= 1
			my_timer.running = window.after(1000, lambda: run_timer(my_timer))
		else:
			timer_display["text"] = "DONE"
			window.bell()
		"""
		pass

	def stop_timer(self):
		pass

	def reset_timer(self):
		self.current_time = self.start_time
		self.timer_display["text"] = self.sec_to_min(self.start_time)

	def change_time(self, num):
		self.current_time += num
		if self.current_time < 0:
			self.current_time = 0
		self.timer_display["text"] = self.sec_to_min(self.current_time)

	def sec_to_min(self, seconds):
		""" given input in seconds, returns equivalent value in minutes (0:00 string) """
		calculation = divmod(seconds, 60)
		if calculation[1] < 10:
			output = "0" + str(calculation[1])
		else:
			output = str(calculation[1])
		return str(calculation[0]) + ":" + output

	def min_to_sec(self, minutes):
		""" given input in 0:00 format, returns equivalent value in seconds """
		vals = minutes.split(":")
		return (int(vals[0]) * 60) + int(vals[1])		

root = tk.Tk()
app = App(root)

root.mainloop()