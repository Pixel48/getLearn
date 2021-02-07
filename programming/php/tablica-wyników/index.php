<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>
  <?php
    if(!isset($_COOKIE['odwiedzone'])) {
      echo "Witamy poraz pierwszy!";
      setcookie('odwiedzone', 1, time() + 60);
    } else {
      $poke = $_COOKIE['odwiedzone'];
      $poke++;
      setcookie('odwiedzone', $poke, time() + 60);
      echo "Witamy po raz ".$_COOKIE['odwiedzone']." przez ostatnią minutę!";
    }
  ?>
  </h1>
  <table>
    <tr>
      <th>team 1</th>
      <th>team 2</th>
      <th>wynik</th>
    </tr>
  <?php
    $db = mysqli_connect('localhost', 'root', '', 'egzamin');
    $query = 'SELECT zespol1, zespol2, wynik FROM rozgrywka';
    $resume = mysqli_query($db, $query);
    while($resume_line = mysqli_fetch_row($resume)) { // mysqli_fetch_row / mysqli_fetch_array
      echo "<tr><td>$resume_line[0]</td><td>$resume_line[1]</td><td>$resume_line[2]</td></tr>";
    }
    mysqli_close($db);
  ?>
  </table>
  <form method='post'>
    <label for="z1">zespoł 1</label>
    <input type="text" name="z1" id="z1">
    <br>
    <label for="z2">zespół 2</label>
    <input type="text" id="z2" name="z2">
    <br>
    <label for="score" id="score">wynik</label>
    <input type="text" name="score" id="score">
    <br>
    <input type="submit" value="Wyślij!">
  </form>
  <?php
    if(!(empty($_POST['z1']) && empty($_POST['z2']) && empty($_POST['score']))) {
      $db = mysqli_connect('localhost', 'root', '', 'ee09_a1_egzamin');
      $z1 = $_POST['z1'];
      $z2 = $_POST['z2'];
      $score = $_POST['score'];
      $q = "INSERT INTO rozgrywka(zespol1, zespol2, wynik, data_rozgrywki) VALUES ('$z1', '$z2', '$score', NOW())";
      // echo "$q";
      mysqli_query($db, $q);
      mysqli_close($db);
      header('location: php1.php'); 
    } 
  ?>
  </body>
</html>