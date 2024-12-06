import pickle

# Try to load the models from the pickle file
with open('models.pkl', 'rb') as file:
    models = pickle.load(file)

# Print the type and contents of the loaded models to understand what is inside
print(f"Type of models: {type(models)}")
print(f"Contents of models (first model if it's a list): {models[0] if isinstance(models, list) else models}")
