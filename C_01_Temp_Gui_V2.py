from tkinter import *


class Converter():
    """

    Temperature conversion tool (°C, °F, °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """
        # gets title heading
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)
        # gets instructions and shows them in correct format
        instructions = ("Please enter a temperature below and then press "
                        "one of the buttons to convert it from centigrade "
                        "to Fahrenheit.")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)
        # entry widget
        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text=error,
                                fg="#9C0000")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
           ["To Celsius", "#02C39A", "", 0, 0],
           ["To Fahrenheit", "#028090", "", 0, 1],
           ["Help / Info", "#019E95", "", 1, 0],
           ["History / Export", "#05668D", "", 0, 1]
        ]

        # List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
