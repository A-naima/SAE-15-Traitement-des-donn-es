import pickle

# Sauvegarde de données binaires
def save_binary_data(data, filename):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

# Chargement de données binaires
def load_binary_data(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
