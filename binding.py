import tkinter as tk

class App:

	def __init__(self, master):
		frame = tk.Frame(master)
		frame.pack()

		self.up_btn = tk.Button(frame, text = "+", command = self.increase_count)
		self.count = tk.Label(frame, text = "0")
		self.down_btn = tk.Button(frame, text = "-", command = self.decrease_count)

		self.up_btn.pack()
		self.count.pack()
		self.down_btn.pack()

	def increase_count(self):
		self.count["text"] = str(int(self.count["text"]) + 1)

	def decrease_count(self):
		self.count["text"] = str(int(self.count["text"]) - 1)

root = tk.Tk()
app = App(root)
root.mainloop()