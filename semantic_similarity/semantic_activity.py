import os
import chromadb
from chromadb.config import Settings

def load_sentences(path):
    """
    Carga oraciones desde un archivo .txt
    """
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def print_results(query, results):
    """
    Imprime resultados de una consulta
    """
    print("\n======================================")
    print(f"QUERY: {query}")
    print("Top results:")
    for doc in results["documents"][0]:
        print(f" - {doc}")
    print("======================================\n")


def load_base_dataset(collection, sentences):
    """
    1) Insertar dataset base en la colección

    TODO:
    - Generar IDs únicos (ej. id_0, id_1, ...)
    - Insertar documentos usando collection.add()

    HINT:
    - Los IDs NO se pueden repetir

    IMPORTANTE:
    - Después agregarás más documentos
    - Los IDs deben poder continuar (id_50, id_51...)

    Ejemplo:
    ids = [f"id_{i}" for i in range(len(sentences))]

    HINT:
    - Usar collection.add()
    - documents=sentences
    - ids=ids
    """

    print(f"Se insertarán {len(sentences)} oraciones base.")

    # TODO: generar ids
    ids = None

    # TODO: insertar en la colección
    

    print("Dataset base insertado correctamente.\n")


def run_required_queries(collection):
    """
    2) Ejecutar queries requeridas

    TODO:
    - Definir las queries dadas
    - Ejecutarlas con collection.query()
    - n_results = 3
    - Mostrar resultados con print_results() 
    """
    pass


def insert_student_documents(collection, sentences):
    """
    3) Insertar al menos 50 documentos con metadata

    TODO:
    - Cargar new_sentences.txt
    - Generar IDs nuevos (sin repetir)
    - Crear metadata para cada documento
    - Insertar en la colección

    IMPORTANTE:
    - Usa collection.count() para continuar IDs
    - Elegir UN solo tema

    Ejemplo:
    start_index = collection.count()
    ids = [f"id_{i}" for i in range(start_index, start_index + len(sentences))]

    Ejemplo metadata:
    metadatas = [{"topic": "technology"} for _ in sentences]

    HINT:
    - Usar collection.add()
    - documents=sentences
    - ids=ids
    - agregar metadatas=metadatas
    """

    print(f"Se insertarán {len(sentences)} oraciones nuevas.")

    # TODO: generar ids nuevos
    ids = None

    # TODO: insertar en la colección con metadatos

    print("Dataset nuevo insertado correctamente.\n")
    pass


def search_documents(collection):
    """
    4) Búsqueda libre (interfaz básica)

    El usuario escribe una consulta y el sistema devuelve resultados similares.

    TODO:
    - Pedir input al usuario
    - Ejecutar query con n_results=4
    - Mostrar resultados
    - Usar collection.query()

    IMPORTANTE:
    - La búsqueda es SEMÁNTICA (no usar palabras exactas)
    """
    user_query = input("Enter your query: ")

    #TODO: agregar ejecución de query
    pass


def update_document(collection):
    """
    5) Actualizar documento

    TODO:
    - Pedir ID
    - Pedir nuevo texto
    - Usar collection.update()
    """
    pass


def delete_documents(collection):
    """
    6) Eliminar documento por ID

    TODO:
    - Pedir ID
    - Eliminar con collection.delete()
    """
    pass


def reset_collection(collection):
    """
    7) Eliminar toda la colección

    TODO:
    - Usar collection.delete()
    """
    pass



# Main
def main():

    print("\n=== Actividad: Búsqueda Semántica con ChromaDB ===\n")

    DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(DIR, "data")

    # Cliente y colección
    # TODO: Crear cliente persistente
    client = None

    # TODO: Crear colección con tu nombre
    collection = None


    # Load Dataset
    sentences_path = os.path.join(DIR, "sentences.txt")
    new_sentences_path = os.path.join(DIR, "new_sentences.txt")
    base_sentences = load_sentences(sentences_path)
    new_sentences = load_sentences(new_sentences_path)

    print(f"Se cargaron {len(base_sentences)} oraciones base.")

    # Menú

    while True:

        print("\nSelecciona una opción:")
        print("1) Cargar dataset base")
        print("2) Ejecutar queries requeridas")
        print("3) Insertar documentos de tu tema (50 + metadata)")
        print("4) Buscar (query libre)")
        print("5) Actualizar documento")
        print("6) Eliminar documento por ID")
        print("7) Eliminar toda la colección")
        print("8) Salir")

        option = input("Opción: ")

        if option == "1":
            load_base_dataset(collection, base_sentences)

        elif option == "2":
            run_required_queries(collection)

        elif option == "3":
            insert_student_documents(collection, new_sentences)

        elif option == "4":
            search_documents(collection)

        elif option == "5":
            update_document(collection)

        elif option == "6":
            delete_documents(collection)

        elif option == "7":
            reset_collection(collection)

        elif option == "8":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()