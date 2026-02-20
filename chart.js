document.addEventListener("DOMContentLoaded", function () {

    const delays = JSON.parse(document.getElementById("delay-data").textContent);

    const ctx = document.getElementById('delayChart').getContext('2d');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: delays.map(() => ""),
            datasets: [{
                label: 'Delay (minutes)',
                data: delays,
                tension: 0.4,
                fill: false,
                borderWidth: 2
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        min: 0
                    }
                }],
                xAxes: [{
                    display: false
                }]
            }
        }
    });

});
