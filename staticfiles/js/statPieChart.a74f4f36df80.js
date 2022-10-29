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
                    "#CCE2CB",
                    "#FFE1E9",
                    "#FDD7C2",
                    "#F6EAC2",
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

    var chartBar = new Chart(document.getElementById("chartPie"), configPie);
 
}
                    
pieChart();