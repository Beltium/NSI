<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Heure en temps réel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 2em;
            text-align: center;
            margin-top: 20%;
        }
    </style>
</head>
<body>

    <div>
        Il est <span id="clock">
            <?php
                date_default_timezone_set('Europe/Paris');
                echo date("H:i:s");
            ?>
        </span>
    </div>

    <script>
        function updateClock() {
            const now = new Date();
            const h = String(now.getHours()).padStart(2, '0');
            const m = String(now.getMinutes()).padStart(2, '0');
            const s = String(now.getSeconds()).padStart(2, '0');
            document.getElementById('clock').textContent = `${h}:${m}:${s}`;
        }

        // Mettre à jour chaque seconde
        setInterval(updateClock, 1000);

        // Mettre à jour immédiatement sans attendre la première seconde
        updateClock();
    </script>

</body>
</html>
