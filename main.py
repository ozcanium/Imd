import tkinter as tk
import requests

url_search_by_name = "https://api.collectapi.com/imdb/imdbSearchByName"
api_key = "apikey 5sqJdApDBJLCSV9iquWXs9:7FBKHx8n7O1iEMMI8GLErm"

def movie_details_by_name():
    film_name = film_name_entry.get()

    if not film_name:
        result_label.config(text="Enter a Film Name")
        return

    headers = {'content-type': "application/json", 'authorization': api_key}
    params = {"query": film_name}

    try:
        response = requests.get(url_search_by_name, headers=headers, params=params)
        data = response.json()

        result_label.config(text=str(data))
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")


window = tk.Tk()
window.title("IMDb Movie Details Search by Name ")
window.config(padx=200, pady=200)

canvas = tk.Canvas(height=175, width=180)
logo = tk.PhotoImage(file="imdb3.png")
canvas.create_image(100, 100, image=logo)
canvas.pack()

film_name_label = tk.Label(text="Enter Film Name Please: ", pady=30, padx=30)
film_name_label.pack()

film_name_entry = tk.Entry(width=40)
film_name_entry.pack()

search_by_name_button = tk.Button(text="Search by Name", command=movie_details_by_name)
search_by_name_button.pack()


result_label = tk.Label()
result_label.pack()


window.mainloop()




