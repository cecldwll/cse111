import requests
import tkinter as tk
from tkinter import ttk

def get_exchange_rates():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return data.get("rates", {})
    except requests.exceptions.RequestException as e:
        print("Error fetching exchange rates:", e)
        return None

def convert_currency(from_currency, to_currency, amount, exchange_rates):
    if from_currency == to_currency:
        return amount

    rate_to_usd = exchange_rates.get(from_currency)
    if rate_to_usd is None:
        print(f"Unsupported currency: {from_currency}")
        return None
    
    amount_in_usd = amount / rate_to_usd

    rate_from_usd = exchange_rates.get(to_currency)
    if rate_from_usd is None:
        print(f"Unsupported currency: {to_currency}")
        return None

    converted_amount = amount_in_usd * rate_from_usd
    return converted_amount

def on_convert_button_click():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_entry.get())
    converted_amount = convert_currency(from_currency, to_currency, amount, exchange_rates)
    if converted_amount is not None:
        result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    else:
        result_label.config(text="Unable to perform the currency conversion.")

exchange_rates = get_exchange_rates()

if exchange_rates is None:
    exit()

root = tk.Tk()
root.title("Currency Converter")

from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()

from_currency_label = ttk.Label(root, text="From Currency:")
from_currency_label.grid(row=0, column=0, padx=5, pady=5)
from_currency_combobox = ttk.Combobox(root, textvariable=from_currency_var, values=list(exchange_rates.keys()))
from_currency_combobox.grid(row=0, column=1, padx=5, pady=5)
from_currency_combobox.current(0)

to_currency_label = ttk.Label(root, text="To Currency:")
to_currency_label.grid(row=1, column=0, padx=5, pady=5)
to_currency_combobox = ttk.Combobox(root, textvariable=to_currency_var, values=list(exchange_rates.keys()))
to_currency_combobox.grid(row=1, column=1, padx=5, pady=5)
to_currency_combobox.current(0)

amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0, padx=5, pady=5)
amount_entry = ttk.Entry(root)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

convert_button = ttk.Button(root, text="Convert", command=on_convert_button_click)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
