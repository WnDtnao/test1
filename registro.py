from mysqlconnection import connectToMySQL

class registros:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO registro (nombre, apellido, edad, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW());"
        return connectToMySQL('registro').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM registro;"

        results = connectToMySQL('registro').query_db(query)
        registros_list = []

        for registro in results:
            registros_list.append(cls(registro))
        return registros_list