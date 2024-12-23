app = Flask(__name__)

# ... (Importaciones ya realizadas en la primera parte del código) #

html_code = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blockchain Demo</title>
</head>
<body>
    <h1>Blockchain Demo</h1>
    
    <button onclick="generarNuevoBloque()">Generar Nuevo Bloque</button>
    <div id="resultado"></div>

    <script>
        function generarNuevoBloque() {
            fetch('http://localhost:5000/nuevo_bloque?prueba=123&hash_anterior=abc')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('resultado').innerHTML = `<p>${data.mensaje}</p><pre>${JSON.stringify(data.bloque, null, 2)}</pre>`;
                })
                .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>
'''

@app.route('/')
http://localhost:5000/nuevo_bloque?prueba=123&hash_anterior=abc
