def print_models(unprinted_designs, completed_models):
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
        # VERSION 2

# La primera funcion se ocupara de la impresion de los diseños y la 
# segunda resumira las impresiones que se hay hecho

def impresion(modelos_para_imprimir, modelos_impresos):
    """Mueve y muestra los modelos que estan siendo impresos"""
    while modelos_para_imprimir:
        modelo_actual = modelos_para_imprimir.pop()
        print(f"Imprimiendo {modelo_actual}... Aguarde por favor")
        print(f"{modelo_actual.capitalize()} impreso!\n")
        modelos_impresos.append(modelo_actual)

def muestra_terminados(modelos_impresos):
    print("\nLos siguientes modelos fueron ya impresos: ")
    for actual in modelos_impresos:
        print(actual.capitalize())    
        