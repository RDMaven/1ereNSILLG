var val = 5

window.onload=function() {
const jauge = new RGraph.Gauge({
    id: 'jauge',
    min:0,
    max:10,
    value: val,
    options: {
        adjustable: true
    }
}).draw();
}

function up() {
    val += 1
    
}
    



function down() {
    jauge.value -= 1
}