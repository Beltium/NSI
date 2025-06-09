<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $pseudo = strip_tags($_POST['pseudo']);
    $reactionTime = (int) $_POST['reactionTime'];

    $score = [
        'pseudo' => $pseudo,
        'reactionTime' => $reactionTime,
        'date' => date('Y-m-d H:i:s')
    ];

    $file = 'scores.json';

    $data = [];
    if (file_exists($file)) {
        $json = file_get_contents($file);
        $data = json_decode($json, true);
    }

    $data[] = $score;

    file_put_contents($file, json_encode($data, JSON_PRETTY_PRINT));

    header('Location: classement.php');
    exit();
}
?>
