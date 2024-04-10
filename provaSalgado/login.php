<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./css/bootstrap.css">
    <script src="js/movimento.js" defer></script>
    <script src="js/java.js" defer></script>
</head>

<body>
    <div class="container">
        
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email</label>
                <input type="email" class="form-control" id="mail" name="mail" aria-describedby="emailHelp">
                <div id="emailHelp" class="form-text"></div>
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Senha</label>
                <input type="password" class="form-control" id="senha" name="senha">
            </div>
            <button type="button" onclick="enviar()" class="btn btn-primary">Submit</button>
        
            <div style="display:none" id="alert"></div>
    </div>
</body>

</html>