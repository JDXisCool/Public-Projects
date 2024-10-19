import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk
import webbrowser

# Sample data for cities
cities_info = {
    "Bangalore": {
        "map": "maps/bangalore_map.png",
        "tourist_hotspots": "Lalbagh, Cubbon Park, Vidhana Soudha",
        "cafes": "Coffee Day (MG Road), Third Wave Coffee (Indiranagar)",
        "hotels": "Taj Hotel (MG Road), ITC Gardenia (Residency Road)",
        "travel_options": "Metro, Buses, Cabs"
    },
    "Mysore": {
        "map": "maps/mysore_map.png",
        "tourist_hotspots": "Mysore Palace, Chamundi Hill",
        "cafes": "Cafe Agrahara (Ashoka Road), Infinitive (Lalitha Mahal Road)",
        "hotels": "Radisson Blu (Jayalakshmipuram), Fortune JP Palace (Dattagalli)",
        "travel_options": "Buses, Autos"
    },
    "Hubli": {
        "map": "maps/hubli_map.png",
        "tourist_hotspots": "Unkal Lake, Nrupatunga Hill",
        "cafes": "Cafe Coffee Day (Gokul Road), Fresh Bake (Keshwapur)",
        "hotels": "Royal Orchid (Bangalore Road), Divya Sagar (Keshwapur)",
        "travel_options": "Buses, Taxis"
    },
    "Dharwad": {
        "map": "maps/dharwad_map.png",
        "tourist_hotspots": "Indira Gandhi Glass House, Nrupatunga Hill",
        "cafes": "Cafe Coffee Day (Nehru Nagar), Chaat Gali (Nehru Nagar)",
        "hotels": "Hotel Ashok (Bangalore Road), Hotel Swagat (Gadag Road)",
        "travel_options": "Buses, Autos"
    },
    "Mangalore": {
        "map": "maps/mangalore_map.png",
        "tourist_hotspots": "Panambur Beach, Kadri Manjunath Temple",
        "cafes": "Bistro (Balmatta), Cafe Alva's (Kuntikana)",
        "hotels": "Taj Gateway (Mangalore), The Gateway Hotel (Bajpe)",
        "travel_options": "Buses, Taxis"
    },
    "Belgaum": {
        "map": "maps/belgaum_map.png",
        "tourist_hotspots": "Belgaum Fort, Kamal Basti",
        "cafes": "Cafe Coffee Day (Club Road), The Garden Cafe (Gadadkelkar)",
        "hotels": "Hotel Sankam Residency (College Road), Hotel Eefa (Khanapur Road)",
        "travel_options": "Buses, Autos"
    },
    "Chikmagalur": {
        "map": "maps/chikmagalur_map.png",
        "tourist_hotspots": "Mullayanagiri, Baba Budangiri",
        "cafes": "The Coffee Shop (Main Road), Town Canteen (MG Road)",
        "hotels": "The Serai (Chikmagalur), Planters Court (MG Road)",
        "travel_options": "Buses, Cabs"
    },
    "Coorg": {
        "map": "maps/coorg_map.png",
        "tourist_hotspots": "Abbey Falls, Talacauvery",
        "cafes": "Coorg Coffee Shop (Madikeri), The Fort Mercara (Madikeri)",
        "hotels": "Club Mahindra (Kakkabe), Evolve Back (Gonicoppa)",
        "travel_options": "Buses, Taxis"
    },
    "Hampi": {
        "map": "maps/hampi_map.png",
        "tourist_hotspots": "Virupaksha Temple, Hampi Bazaar",
        "cafes": "Mango Tree (Hampi), The German Bakery (Hampi)",
        "hotels": "Hampi's Boulders (Hampi), Hotel Hilltop (Hampi)",
        "travel_options": "Buses, Autos"
    },
    "Gadag": {
        "map": "maps/gadag_map.png",
        "tourist_hotspots": "Dodda Basappa Temple, Archaeological Museum",
        "cafes": "Cafe Jivan (Gadag), The Corner House (Gadag)",
        "hotels": "Hotel Ashok (Gadag), Hotel Anand (Gadag)",
        "travel_options": "Buses, Autos"
    },
}

class CityInfoApp:
    def __init__(self, master):
        self.master = master
        master.title("Karnataka City Info")

        self.city_var = tk.StringVar(value="Select a city")
        self.city_menu = tk.OptionMenu(master, self.city_var, *cities_info.keys())
        self.city_menu.pack(pady=20)

        self.info_button = tk.Button(master, text="Show Info", command=self.show_info)
        self.info_button.pack(pady=10)

    def show_info(self):
        selected_city = self.city_var.get()
        if selected_city in cities_info:
            self.open_info_window(selected_city)
        else:
            messagebox.showerror("Error", "Please select a valid city.")

    def open_info_window(self, city):
        info_window = Toplevel(self.master)
        info_window.title(f"{city} Info")

        for key in cities_info[city].keys():
            button = tk.Button(info_window, text=key.capitalize(), command=lambda k=key: self.display_info(city, k))
            button.pack(pady=5)

    def display_info(self, city, info_type):
        if info_type == "map":
            self.show_map(city)
        else:
            info_message = cities_info[city][info_type]
            messagebox.showinfo(f"{info_type.capitalize()} in {city}", info_message)

    def show_map(self, city):
        city_urls = {
            "Bangalore": "https://www.google.com/maps/place/Bangalore",
            "Mysore": "https://www.google.com/maps/place/Mysore",
            "Hubli": "https://www.google.com/maps/place/Hubli",
            "Dharwad": "https://www.google.com/maps/place/Dharwad",
            "Mangalore": "https://www.google.com/maps/place/Mangalore",
            "Belgaum": "https://www.google.com/maps/place/Belgaum",
            "Chikmagalur": "https://www.google.com/maps/place/Chikmagalur",
            "Coorg": "https://www.google.com/maps/place/Coorg",
            "Hampi": "https://www.google.com/maps/place/Hampi",
            "Gadag": "https://www.google.com/maps/place/Gadag",
        }
        
        url = city_urls.get(city)
        webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    app = CityInfoApp(root)
    root.mainloop()
