function barChart() {
    Chart.defaults.color = "black";

    const labels = ["Middle East and North Africa",
    "Sub-Saharan Africa","Latin America and Caribbean",
    "North America","South Asia","Europe and Central Asia",
    "East Asia and Pacific"]

    const data = {
        labels: labels,
        datasets: [
            {
                label: '2016',
                data: [129, 174, 231, 289, 334, 392, 468],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.8)',
                  ],
            },
            {
                label: '2030',
                data: [177, 269, 290, 342, 466, 440, 602],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.8)',
                  ],


            },
            {
                label: '2050',
                data: [255, 516, 369, 396, 661, 490, 714],
                backgroundColor: [
                    'rgba(54, 162, 235, 0.8)',
                  ],
            }
        ]
    }


    const config = {
        type: 'bar',
        data: data,
        options: {
          responsive: true,
          plugins: {
            legend: {
              display: true,
              position: 'top',
            },
            title: {
              display: true,
              text: 'Projected waste generation, by rXXXegion (millions of tonnes/year)',
              align: 'end',
              font: {
                weight: 'bold',
                size: 16,
              },
              fullSize: true,
            },
          }
        },
      };

    var chartBar = new Chart(document.getElementById("whyBar1"), config);
 
}

barChart();