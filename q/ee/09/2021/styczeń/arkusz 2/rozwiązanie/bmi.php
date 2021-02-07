<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styl3.css">
  <title>Twoje BMI</title>
</head>
<body>
  <header>
    <div class="logo"><img src="img/wzor.png" alt="Twoje" BMI=""></div>
    <div class="banner">Oblicz swoje BMI</div>
  </header>
  <main>
    <table>
      <tr>
        <th>Interpretacja BMI</th>
        <th>Wartość minimalna</th>
        <th>Wartość maksymalna</th>
      </tr>
      <?php
        $db = mysqli_connect('localhost', 'root', '', 'ee09_a3_egzamin');
        $q1 = "SELECT informacja, wart_min, wart_max FROM bmi";
        $res1 = mysqli_query($db, $q1);
        if(mysqli_num_rows($res1) > 0) {
          while($r1 = mysqli_fetch_row($res1)) echo "<tr><td>$r1[0]</td><td>$r1[1]</td><td>$r1[2]</td></tr>";
          mysqli_close($db);
        } else echo "Some DB-Error occured..."
      ?>
    </table>
  </main>
  <div class="left">
    <h2>Podaj wagę i wzrost</h2>
    
    <form method="post" action="">
      <label for="m">Waga:</label>
      <input type="number" name="m" id="m" min="1">
      <br>
      <label for="h">Wzrost w cm:</label>
      <input type="number" name="h" id="h" min="1">
      <br>
      <input type="submit" value="Oblicz i zapamiętaj wynik">
    </form>
    <br>
    <?php
    if(!empty($_POST['m']) && !empty($_POST['h'])) {
        $m = (float)$_POST['m'];
        $h = (float)$_POST['h'];
        $bmi = $m/($h*$h)*10000;
        echo "<p>Twoja waga: $m kg; Twój wzrost: $h cm / BMI wynosi: $bmi</p>";
        // send data
        if($bmi > 100) $bmi = 99;
        $db = mysqli_connect('localhost', 'root', '', 'ee09_a3_egzamin');
        $q_bmi_id = "SELECT id FROM bmi WHERE $bmi > wart_min AND $bmi < wart_max";
        $res_bmi = mysqli_query($db, $q_bmi_id);
        $bmi_id = mysqli_fetch_row($res_bmi)[0];
        $q2 = "INSERT INTO wynik(bmi_id, data_pomiaru, wynik) VALUES ($bmi_id, NOW(), $bmi)";
        if(!empty($bmi)) mysqli_query($db, $q2);
        mysqli_close($db);
        $m = null;
        $h = null;
        $bmi = null;
      }
    ?>
  </div>
  <div class="right">
    <img src="img/rys1.png" alt="ćwiczenia">
  </div>
  <footer>Autor: 00000000000 <a href="kewrendy.txt">Zobacz kwerendy</a></footer>
</body>
</html>