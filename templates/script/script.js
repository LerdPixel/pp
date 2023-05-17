
window.onload = function(){
    // your code
/*
function click()
{
    console.log("f");
    if((this.elements.message1.value == '') || (this.elements.message2.value == '') || (this.elements.message1.value.length > 30) || (this.elements.message2.value.length > 30))
    {
        console.log("can not post");
        return false
    }
    var xhr = new XMLHttpRequest()
    xhr.open("GET", "/registration?name=" + this.elements.message1.value + "&password=" + this.elements.message2.value, true)
    xhr.send('')
    this.elements.message1.value = ''
    this.elements.message2.value = ''
    return false
}*/
document.querySelector("#sub").onclick = function(){
    window.location.href = "/login.html";
    if((document.getElementById("mes1").value == '') || (document.getElementById("mes2").value == '') /*|| (document.getElementById("mes1").value.length > 30) || (document.getElementById("mes2").value.length > 30)*/)
    {
        console.log("can not post");
        return false
    }
    console.log(document.getElementById("mes1").value);
    console.log(document.getElementById("mes2").value);
    var xhr = new XMLHttpRequest()
    xhr.open("GET", "/registrations?name=" + document.getElementById("mes1").value + "&password=" + document.getElementById("mes2").value, true)
    xhr.send('')
    document.getElementById("mes1").value = ''
    document.getElementById("mes2").value = ''
    return false
  }
}
