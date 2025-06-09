<?php
$scores = [];

if (file_exists('scores.json')) {
    $json = file_get_contents('scores.json');
    $scores = json_decode($json, true);
}

// Tri des scores
usort($scores, function($a, $b) {
    return $a['reactionTime'] - $b['reactionTime'];
});

// Recherche par pseudo si demandé
$search = isset($_GET['pseudo']) ? trim($_GET['pseudo']) : '';
if ($search !== '') {
    $scores = array_filter($scores, function($score) use ($search) {
        return stripos($score['pseudo'], $search) !== false;
    });
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Classement - Réflexes</title>
    <link rel="stylesheet" href="style.css" />
</head>
<body>
    <h1>Classement des meilleurs réflexes</h1>

    <form method="GET" action="classement.php" style="margin-bottom: 20px;">
        <label for="pseudo">Rechercher un pseudo :</label>
        <input type="text" name="pseudo" id="pseudo" value="<?= htmlspecialchars($search) ?>" />
        <button type="submit">Rechercher</button>
        <?php if ($search !== ''): ?>
            <a href="classement.php" class="button">Réinitialiser</a>
        <?php endif; ?>
    </form>

    <table>
        <tr><th>Rang</th><th>Pseudo</th><th>Temps (ms)</th><th>Date</th></tr>
        <?php foreach (array_slice($scores, 0, 20) as $i => $score): ?>
            <tr>
                <td><?= $i + 1 ?></td>
                <td><?= htmlspecialchars($score['pseudo']) ?></td>
                <td><?= $score['reactionTime'] ?></td>
                <td><?= $score['date'] ?></td>
            </tr>
        <?php endforeach; ?>
    </table>

    <br />
    <a class="button" href="index.html">Rejouer</a>
</body>
</html>
