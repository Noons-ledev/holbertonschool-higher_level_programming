#!/usr/bin/python3
if __name__ == "__main__":
    import inspect
    import hidden_4
    membres = inspect.getmembers(hidden_4, inspect.isfunction)
    function_names = sorted([nom for nom, _ in membres])
    for nom in function_names:
        if nom[0] != '_':
            print(nom)
