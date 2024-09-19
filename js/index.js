function addEstudiante(){
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var grado = document.getElementById("grado").value;
    var especialidad = document.getElementById("especialidad").value;
    var correo = document.getElementById("correo").value;
    var carnet = document.getElementById("carnet").value;
    var edad = document.getElementById("edad").value;
    let headers = new headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    fetch('http://127.0.0.1:5000/addestudiante',{
        method: 'POST',
        headers,
        body: `{
        "nombre": "${nombre}",
        "apellido": "${apellido}",
        "grado": "${grado}",
        "especialidad": "${especialidad}",
        "correo": "${correo}",
        "carnet": "${carnet}",
        "edad": "${edad}"}`,	
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert("Estudiante agregado con éxito");
        location.reload();
    })
    .catch(error => console.log(error));
}
