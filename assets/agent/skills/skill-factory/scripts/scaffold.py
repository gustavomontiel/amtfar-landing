import os

def create_skill_structure(name):
    base_path = f"agent/skills/{name}"
    folders = ["recursos", "scripts", "ejemplos"]
    
    os.makedirs(base_path, exist_ok=True)
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    
    print(f"Estructura para {name} creada con éxito.")