function pieChart() {
    var plastik = document.getElementById("mass_plastik").innerHTML;
    var kaca = document.getElementById("mass_kaca").innerHTML;
    var kertas = document.getElementById("mass_kertas").innerHTML;
    var organik = document.getElementById("mass_organik").innerHTML;

    const dataPie = {
        labels: ["Plastik", "Kaca", "Kertas", "Organik"],
        datasets: [
            {
                label: "My First Dataset",
                data: [plastik, kaca, kertas, organik],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(255, 159, 64, 0.8)',
                ],
                hoverOffset: 4,
            },
        ],
    };

    const configPie = {
        type: "pie",
        data: dataPie,
        options: {
            plugins: {
                legend: false,
                tooltip: true,
            },
        },
    };

    var chartBar = new Chart(document.getElementById("pieChart3"), configPie);
 
}
                    
pieChart();