// let valor = document.getElementById("inGrados").value;

function calcularKelvin() {
  let texto = document.getElementById("inGrados").value;

  if (texto !== "" && !isNaN(texto)) {
    let numero = Number(texto);
    let kelvin = numero + 273.15;
    document.getElementById("grados").innerHTML = "Temperatura en Kelvin: " + kelvin;
  } else {
    document.getElementById("grados").innerHTML = "Por favor ingresa un número válido.";
  }
}
function calcularFahrenheit() {
  let texto = document.getElementById("inGrados").value;

  if (texto !== "" && !isNaN(texto)) {
    let numero = Number(texto);
    let kelvin = (numero*9/5)+32;
    document.getElementById("grados").innerHTML = "Temperatura en Kelvin: " + kelvin;
  } else {
    document.getElementById("grados").innerHTML = "Por favor ingresa un número válido.";
  }
}