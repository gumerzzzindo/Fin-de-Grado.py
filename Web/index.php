<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Vulnerable</title>
</head>
<body>
    <h1>Página Vulnerable a XSS y SQL Injection</h1>

    <!-- Formulario vulnerable a XSS -->
    <form action="#" method="post">
        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre"><br>
        <input type="submit" value="Enviar">
    </form>

    <!-- Script vulnerable a XSS -->
    <script>
        var parametro = window.location.search.substring(1);
        document.write("<p>Parámetro: " + parametro + "</p>");
    </script>

    <?php
    // Código PHP vulnerable a SQL Injection
    $conexion = mysqli_connect("localhost", "usuario", "contraseña", "basededatos");

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nombre = $_POST["nombre"];
        $query = "INSERT INTO usuarios (nombre) VALUES ('$nombre')";
        mysqli_query($conexion, $query);
        echo "<p>Usuario '$nombre' insertado correctamente.</p>";
    }
    ?>
</body>
</html>
