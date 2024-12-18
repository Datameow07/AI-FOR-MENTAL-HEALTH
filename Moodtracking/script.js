// Initialize mood chart
const ctx = document.getElementById('moodChart').getContext('2d');
const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
let moodData = [null, null, null, null, null, null, null]; // Placeholder data for each day

const moodChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: daysOfWeek,
        datasets: [{
            label: 'Mood Trend',
            data: moodData,
            borderColor: 'rgba(255, 102, 153, 1)',
            backgroundColor: 'rgba(255, 153, 153, 0.2)',
            pointBackgroundColor: '#ff6699',
            pointBorderColor: '#ff3366',
            tension: 0.4,
            borderWidth: 3,
            fill: true,
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                grid: {
                    color: 'rgba(255, 204, 204, 0.3)',
                },
                ticks: {
                    color: '#ff9999',
                    font: {
                        size: 14,
                    },
                },
            },
            y: {
                min: 0,
                max: 4,
                ticks: {
                    stepSize: 1,
                    callback: (value) => ['Awful 😭', 'Bad 😞', 'Meh 😐', 'Good 🙂', 'Rad 😄'][value],
                    color: '#ff9999',
                    font: {
                        size: 14,
                    },
                },
                grid: {
                    color: 'rgba(255, 204, 204, 0.3)',
                },
            },
        },
        plugins: {
            legend: {
                display: false,
            },
            tooltip: {
                callbacks: {
                    label: (context) => {
                        const moodLabels = ['Awful 😭', 'Bad 😞', 'Meh 😐', 'Good 🙂', 'Rad 😄'];
                        return `Mood: ${moodLabels[context.raw]}`;
                    },
                },
            },
        },
    },
});

// Mood Button Functionality
document.querySelectorAll('.mood-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
        const mood = parseInt(btn.dataset.mood);
        const dayIndex = new Date().getDay() - 1; // Get the current day index (Monday = 0)
        if (dayIndex >= 0 && dayIndex < 7) {
            moodData[dayIndex] = mood; // Update the chart data
            moodChart.update(); // Refresh the chart

            // Update the weekly summary
            const moodLabels = ['Awful 😭', 'Bad 😞', 'Meh 😐', 'Good 🙂', 'Rad 😄'];
            document.getElementById('mood-summary').textContent = `Your mood today: ${moodLabels[mood]}`;
        }
    });
});
