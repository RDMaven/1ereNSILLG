

function laDate() {
    const name = document.formul.name.value

    var ajd = new Date();
    var dd = ajd.getDate();
    var mm = ajd.getMonth();
    var yyyy = ajd.getFullYear();
    var hh = ajd.getHours();
    var min = ajd.getMinutes();
    var sec = ajd.getSeconds();

    var answer = `Bonjour ${name} ! <br>Nous sommes le ${dd}/${mm}/${yyyy}.<br>Il est ${hh}h ${min}min ${sec}s.`

    if (name != '') {
        //alert(answer)

        document.querySelector(".result-div").style.display = '';
        document.querySelector(".result-p").innerHTML = answer;
    }
}

