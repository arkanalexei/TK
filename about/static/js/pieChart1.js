function pieChart1() {
    const dataPie = {
        labels: ["Food/Green", "Glass", "Metal", "Other",
    "Paper/Cardboard", "Plastic", "Rubber/Leather", "Wood"],

        datasets: [
            {
                label: "My First Dataset",
                data: [44,5,4,14,17,12,2,2],
                backgroundColor: [
                    'rgba(143, 204, 200, 0.8)',
                    'rgba(255, 205, 101, 0.8)',
                    'rgba(221, 109, 29, 0.8)',
                    'rgba(147, 189, 99, 0.8)',
                    'rgba(69, 106, 148, 0.8)',
                    'rgba(126, 168, 217, 0.8)',
                    'rgba(73, 69, 128, 0.8)',
                    'rgba(240, 169, 71, 0.8)',
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
                legend: {
                    display: true,
                    position: 'bottom',
                },
                tooltip: true,
                title: {
                    display: true,
                    text: 'Global Waste Composition (percent)',
                    align: 'center',
                    font: {
                      weight: 'bold',
                      size: 18,
                    },
                    fullSize: true,
                  },
            },
        },
        
    };

    var chartBar = new Chart(document.getElementById("pieChart1"), configPie);
 
}
                    
pieChart1();