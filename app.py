# Framework web.py
import web

from controllers.index import Index

# Rutas de los controladores
urls = (
    '/', 'Index',
)

# Crear la aplicacion web
app = web.application(urls, globals())


#Punto de entrada
if __name__ == "__main__":
    app.run()
