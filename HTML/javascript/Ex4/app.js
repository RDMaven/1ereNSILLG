window.onload=function() {
const jauge = new RGraph.Gauge({
    id: 'jauge',
    min:0,
    max:10,
    value:5
}).draw();
}