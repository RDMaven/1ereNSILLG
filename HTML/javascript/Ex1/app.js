

function voyage() {
    const last_name = document.formul.lname.value
    const first_name = document.formul.fname.value
    const from = document.formul.from.value
    const to = document.formul.to.value

    const matin = document.formul.matin
    const midi = document.formul.midi
    const soir = document.formul.soir
    var options = ""

    if (matin.checked) {
        options += "Petit déjeuner "
    }
    if (midi.checked) {
        options += "Déjeuner "
    }
    if (soir.checked) {
        options += "Diner"
    }

    alert(
        "Bonjour " + first_name + " " + last_name
        + "\n Votre voyage : " + from + " --> " + to
        + "\n Vos options : " + options
    )
    

}

