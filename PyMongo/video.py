from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING


# Instanciar un cliente de Mongo
client = MongoClient('localhost',
                     port=27017,
                     username='user',
                     password='pass')

# Base de Datos
print (client.list_database_names())

# Crear base
db = client['prueba']
print (client.list_database_names())

# Colecciones
print (db.list_collection_names())

# Crear Coleccion
col = db['personas']
print (db.list_collection_names())

# Contar documentos
print (col.count_documents())

# Insertar un documento
col.insert_one({
    'edad': 20,
    'nombre': 'Leonardo',
    'intereses': ['Musica', 'Youtube']
})

# Insertar varios documentos
col.insert_many([
    {
        'edad': 23,
        'nombre': 'Nombre 2',
        'intereses': ['1', '2']
    },
    {
        'edad': 40,
        'nombre': 'Nombre 3',
        'intereses': ['3', '4']
    },
    {
        'edad': 50,
        'nombre': 'Nombre 2',
        'intereses': ['1', '2']
    },
    {
        'edad': 80,
        'nombre': 'Nombre 3',
        'intereses': ['3', '4']
    }
])

print (col.count_documents())

# Eliminar un documento
col.delete_one({
    "edad": 40
})

# Eliminar varios documentos
col.delete_many({
    "edad": {
        "$gt": 21
    }
})

# Leer documentos
for documento in col.find({}):
    print(documento)

# Leer un documento
doc = col.find_one({
    "edad": 20
})
print (doc)

# Proyeccion
doc = col.find_one({
    "edad: 20"
}, {
    "edad": 1
})
print (doc)

# Update one
doc = col.update_one({
    "edad": 20
}, {
    "$set": {
        "edad": 99
    }
})

# Update Many
# Same but with update_many()


# Crear indices
col.create_index([('edad', ASCENDING)])

# Eliminar lo que se ha hecho
db.drop_collection('personas')
client.drop_database('prueba')

# Cerrar el cliente
client.close()