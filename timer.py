import tkinter as tk

class App:
	def __init__(self, master):
		frame = tk.Frame(master)
		frame.pack()

		# set attributes for start time, current time
		self.start_time = 0
		self.current_time = 0

		# create variable to be used by start & stop timer functions
		# stores the current call to tkinter's "after" module
		self.callback = None

		# set up labels
		self.title = tk.Label(frame, text = "Timer")
		self.timer_display = tk.Label(frame, text = "0:00")

		# create start, stop, reset buttons
		self.start_btn = tk.Button(frame, text="Start", command = self.start_timer)
		self.stop_btn = tk.Button(frame, text="Stop", command = self.stop_timer)
		self.reset_btn = tk.Button(frame, text="Reset", command = self.reset_timer)
		self.clear_btn = tk.Button(frame, text="Clear", command = self.clear_timer)

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
		self.clear_btn.pack()

		self.minutes_label.pack()
		self.minutes_plus_btn.pack()
		self.minutes_minus_btn.pack()

		self.seconds_label.pack()
		self.seconds_plus_btn.pack()
		self.seconds_minus_btn.pack()

	def update_display(self):
		""" Updates the timer on the app display."""
		self.timer_display["text"] = self.sec_to_min(self.current_time)

	def start_timer(self):
		""" Starts the timer."""
		self.current_time -= 1
		self.update_display()
		if self.current_time > 0:
			self.callback = root.after(1000, lambda: self.start_timer())
		else:
			root.bell()

	def stop_timer(self):
		""" Stops the timer."""
		if self.callback:
			root.after_cancel(self.callback)

	def reset_timer(self):
		""" Stops the timer if running and resets it to the start time value."""
		self.stop_timer()
		self.current_time = self.start_time
		self.update_display()

	def clear_timer(self):
		""" Stops the timer if running and resets all time values to 0."""
		self.stop_timer()
		self.current_time = 0
		self.start_time = 0
		self.update_display()

	def change_time(self, num):
		""" Given an input in seconds, adds that value to the current time. Current time cannot be < 0."""
		self.current_time += num
		self.start_time += num
		if self.current_time < 0:
			self.current_time = 0
		self.update_display()

	def sec_to_min(self, seconds):
		""" Given input in seconds, returns equivalent value in minutes (0:00 string)."""
		calculation = divmod(seconds, 60)
		if calculation[1] < 10:
			output = "0" + str(calculation[1])
		else:
			output = str(calculation[1])
		return str(calculation[0]) + ":" + output

root = tk.Tk()
app = App(root)

root.mainloop()