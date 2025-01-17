#!/usr/bin/python3
if __name__ == "__main__":
    import inspect
    import hidden_4
    members = inspect.getmembers(hidden_4, inspect.isfunction)
    function_names = sorted([name for name, _ in members])
    for name in function_names:
        if nom[0] != '_':
            print(nom)
