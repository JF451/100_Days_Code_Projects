import tkinter as tk
import random

Text = ["A cat ran over the hill", "Some random text"]



root = tk.Tk()
root.geometry("250x170")

def retrieve_input(text):
    inputValue = textBox.get("1.0","end-1c")

    count = 0
    for i, c in enumerate(text.get("1.0", "end-1c").split()):
        try:
            if inputValue[i] == c:
                count += 1
        except:
            pass

    print(count)
    print(inputValue)


# Create text widget and specify size.
T = tk.Text(root, height=5, width=52)

textBox = tk.Text(root, height=2, width=10)
textBox.pack()
buttonCommit=tk.Button(root, height=1, width=10, text="Commit",
                    command=lambda: retrieve_input(T))

buttonCommit.pack()

# Create label
l = tk.Label(root, text="Speed Typing")
l.config(font=("Courier", 14))

# Create button for next text.
b1 = tk.Button(root, text="Next", )

# Create an Exit button.
b2 = tk.Button(root, text="Exit",
            command=root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, random.choice(Text))




tk.mainloop()

# text = "The cat ran over the hill"
#
# count = 0
# for i, c in enumerate(text.split()):
#     try:
#         if input() == c:
#             count += 1
#     except:
#         pass
#
# print(count)
