import requests
import re
import tkinter as tk
from tkinter import ttk


# Class to handle real-time currency conversion
class RealTimeCurrencyConverter:
    def __init__(self, url):
        # Fetch currency data from the API
        self.data = requests.get(url).json()
        self.currencies = self.data["rates"]

    def convert(self, from_currency, to_currency, amount):
        # Convert the amount to USD first if it's not in USD
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]

        # Convert the amount to the target currency and round to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


# Main application class for the currency converter GUI
class CurrencyConverterApp(tk.Tk):
    def __init__(self, converter):
        super().__init__()
        self.title("Egyptian Currency Converter")
        self.currency_converter = converter
        self.geometry("500x250")
        self.configure(bg="#f0e68c")  # Set background color to a sandy yellow

        # Label for the title
        self.intro_label = tk.Label(
            self,
            text="Welcome to the Egyptian Currency Converter",
            fg="#8b4513",
            bg="#f0e68c",
            relief=tk.RAISED,
            borderwidth=3,
        )
        self.intro_label.config(font=("Courier", 15, "bold"))
        self.intro_label.place(x=10, y=5)

        # Label to display the current exchange rate and date
        self.date_label = tk.Label(
            self,
            text=f"1 EGP equals = {self.currency_converter.convert('EGP', 'USD', 1)} USD \n Date: {self.currency_converter.data['date']}",
            relief=tk.GROOVE,
            borderwidth=5,
            bg="#f0e68c",
        )
        self.date_label.place(x=150, y=50)

        # Entry box for the amount to convert
        self.amount_field = tk.Entry(
            self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate="key"
        )
        self.amount_field.config(
            validatecommand=(self.register(self.restrict_number_only), "%d", "%P")
        )
        self.amount_field.place(x=36, y=150)

        # Label to display the converted amount
        self.converted_amount_field_label = tk.Label(
            self,
            text="",
            fg="black",
            bg="white",
            relief=tk.RIDGE,
            justify=tk.CENTER,
            width=17,
            borderwidth=3,
        )
        self.converted_amount_field_label.place(x=346, y=150)

        # Dropdown for selecting the 'from' currency
        self.from_currency_variable = tk.StringVar(self)
        self.from_currency_variable.set("EGP")  # Default value is Egyptian Pound
        self.from_currency_dropdown = ttk.Combobox(
            self,
            textvariable=self.from_currency_variable,
            values=list(self.currency_converter.currencies.keys()),
            font=("Courier", 12, "bold"),
            state="readonly",
            width=12,
            justify=tk.CENTER,
        )
        self.from_currency_dropdown.place(x=30, y=120)

        # Dropdown for selecting the 'to' currency
        self.to_currency_variable = tk.StringVar(self)
        self.to_currency_variable.set("USD")  # Default value is US Dollar
        self.to_currency_dropdown = ttk.Combobox(
            self,
            textvariable=self.to_currency_variable,
            values=list(self.currency_converter.currencies.keys()),
            font=("Courier", 12, "bold"),
            state="readonly",
            width=12,
            justify=tk.CENTER,
        )
        self.to_currency_dropdown.place(x=340, y=120)

        # Button to perform the conversion
        self.convert_button = tk.Button(
            self,
            text="Convert",
            fg="#8b4513",
            bg="#f0e68c",
            command=self.perform_conversion,
        )
        self.convert_button.config(font=("Courier", 10, "bold"))
        self.convert_button.place(x=225, y=200)

    # Function to perform the conversion and update the converted amount label
    def perform_conversion(self):
        try:
            amount = float(self.amount_field.get())
            from_curr = self.from_currency_variable.get()
            to_curr = self.to_currency_variable.get()

            converted_amount = self.currency_converter.convert(
                from_curr, to_curr, amount
            )
            converted_amount = round(converted_amount, 2)

            self.converted_amount_field_label.config(text=str(converted_amount))
        except ValueError:
            self.converted_amount_field_label.config(text="Invalid input")

    # Function to restrict the input to numbers only
    def restrict_number_only(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string == "" or (string.count(".") <= 1 and result is not None)


# Main function to run the application
if __name__ == "__main__":
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    converter = RealTimeCurrencyConverter(url)

    app = CurrencyConverterApp(converter)
    app.mainloop()

# Copyrights to Aya Nabil
