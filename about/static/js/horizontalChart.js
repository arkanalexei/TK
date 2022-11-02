function horizontalChart() {
    Chart.defaults.color = "black";

    const labels = ["High Income","Upper-middle Income","Lower-middle Income","Low Income"]

    const data = {
        labels: labels,
        datasets: [{
          axis: 'y',
          data: [96,82,51,39],
          fill: false,
          backgroundColor: [
            'rgba(255, 99, 132, 0.8)',
            'rgba(255, 159, 64, 0.8)',
            'rgba(255, 205, 86, 0.8)',
            'rgba(75, 192, 192, 0.8)',
          ],
        }]
      };

      const config = {
        type: 'bar',
        data: data,
        options: {
            indexAxis: 'y',
          responsive: true,
          plugins: {
            legend: {
              display: false,
            },
            title: {
              display: true,
              text: 'Waste collection rates, by income level (percent)',
              align: 'end',
              font: {
                weight: 'bold',
                size: 18,
              },
              fullSize: true,
            },
          }
        },
      };
        

    var chartBar = new Chart(document.getElementById("horizontalChart"), config);
 
}

horizontalChart();
