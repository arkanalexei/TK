function pieChart2() {
    const dataPie = {
        labels: ["Composting","Incineration","Controlled Landfill",
    "Landfill(unspecified)","Sanitary Landfill","Open Dump","Other","Recycling"],

        datasets: [
            {
                label: "My First Dataset",
                data: [5.5,11.1,3.7,25.2,7.7,33,0.3,13.5],
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
                    text: 'Global Treatment and disposal of waste (percent)',
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

    var chartBar = new Chart(document.getElementById("pieChart2"), configPie);
 
}
                    
pieChart2();