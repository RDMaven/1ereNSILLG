

function convert() {
    const somme = document.formul.somme.value
    const to = document.formul.to.value

    if (to == "eur") {
        alert( somme+"$ = " + somme*(0.9) + "€")
    }
    else if (to == "usd") {
        alert( somme+"€ = " + somme*(1/0.9) + "$")
    }
}

