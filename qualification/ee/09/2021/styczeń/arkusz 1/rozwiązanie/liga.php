<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>piłka nożna</title>
    <link rel="stylesheet" href="styl2.css">
</head>
<body>

    <div id='baner'>
        <h3>Reprezentacja polski w piłce nożnej</h3>
        <img src="obraz1.jpg" alt="reprezentacja">
    </div>
    <div id='lewy'>
    <form method="post" action="liga.php">
        <select name="lista" id="listaid">
        <option value="1">Bramkarze</option>
        <option value="2">Obrońcy</option>
        <option value="3">Pomocnicy</option>
        <option value="4">Napastnicy</option>
        </select>
        <input type="submit" value="Zobacz">
    </form>
    <img src="zad2.png" alt="piłka">
    <p>Autor: NUMER PESEL</p>
    </div>
    <div id='prawy'>
    <ol>
<?php
    $penis=$_POST['lista']; //wpisujesz name'a z pól wyboru z forma 
	$sql = "SELECT imie, nazwisko FROM zawodnik WHERE pozycja_id=$penis";
	$db = mysqli_connect('localhost', 'root', '', 'EE09_a1_egzamin');
	$res = mysqli_query($db,$sql);
	while($r = mysqli_fetch_array($res)){
        $imie=$r["imie"];
        $nazwisko=$r["nazwisko"];
        echo "<li>$imie $nazwisko</li>";
    }
    mysqli_close($db);
?>
    </ol>
    </div>
    <main>
        <h3>Liga mistrzów</h3>
    </main>
    <div id='liga'>
    <?php
        $sql = "SELECT zespol, punkty, grupa FROM "
    ?>
    </div>
</body>
</html>