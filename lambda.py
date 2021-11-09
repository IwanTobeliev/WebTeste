capivara = [
    {"nome": "cap", "casa": "capivara"},
    {"nome": "capy", "casa": "capivaras"},
    {"nome": "capybara", "casa": "capivarinhas"},
    {"nome": "capa", "casa": "capivara"},
]


capivara.sort(key=lambda capivara: capivara["nome"])
print(capivara)