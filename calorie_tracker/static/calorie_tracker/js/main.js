var table = document.getElementById('table');
var carb = 0, protein = 0, fat = 0, calories = 0;
for (var i = 1; i < table.rows.length - 1; i++) {
    table.rows[i].cells[0].innerHTML = i + '.';
    carb += parseFloat(table.rows[i].cells[2].innerHTML);
    protein += parseFloat(table.rows[i].cells[3].innerHTML);
    fat += parseFloat(table.rows[i].cells[4].innerHTML);
    calories += parseFloat(table.rows[i].cells[5].innerHTML);
}

document.getElementById('totalCarb').innerHTML = '<b>' + Math.round(carb) + '(gm)</b>';
document.getElementById('totalProtein').innerHTML = '<b>' + Math.round(protein) + '(gm)</b>';
document.getElementById('totalFat').innerHTML = '<b>' + Math.round(fat) + '(gm)</b>';
document.getElementById('totalCalories').innerHTML = '<b>' + Math.round(calories) + '(gm)</b>';

var calPer = (calories / 5000) * 100;
document.getElementsByClassName('progress-bar')[0].setAttribute('style', 'width:' + calPer + '%');
document.getElementsByClassName('progress-bar')[0].innerHTML = '<b>' + calPer + '%</b>';



var total = carb + protein + fat
var carbPer = Math.round(carb / total * 100)
var proteinPer = Math.round(protein / total * 100)
var fatPer = Math.round(fat / total * 100)

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Carbs ' + carbPer + '%', 'Protein ' + proteinPer + '%', 'Fat ' + fatPer + '%'],
        datasets: [{
            label: 'calories consumed',
            data: [carbPer, proteinPer, fatPer],
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132, 1)',
                'rgb(54, 162, 235, 1)',
                'rgb(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    }
});
