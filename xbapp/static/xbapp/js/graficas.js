

function graficaSexo () {
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawSexo);
}

function drawSexo() {
        var data = google.visualization.arrayToDataTable([
          ['Ciclistas', 'Ciclistas por sexo'],
          ['Hombres',     parseInt($('#nhombres').data("n"))],
          ['Mujeres',      parseInt($('#nmujeres').data("n"))]
        ]);

        var options = {
          title: 'Ciclistas por sexo'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
}

function graficaEdades () {
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawSexo);
}

function drawEdades() {
        var data = google.visualization.arrayToDataTable([
          ['Ciclistas', 'Ciclistas por sexo'],
          ['Hombres',     parseInt($('#nhombres').data("n"))],
          ['Mujeres',      parseInt($('#nmujeres').data("n"))]
        ]);

        var options = {
          title: 'Ciclistas por sexo'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        chart.draw(data, options);
}

graficaSexo();