
window.onload = function(){

    document.querySelector("#sub").onclick = function(){
//        console.log("12345");
        if((document.getElementById("mes1").value == '') || (document.getElementById("mes2").value == '') /*|| (document.getElementById("mes1").value.length > 30) || (document.getElementById("mes2").value.length > 30)*/)
        {
            console.log("can not post")
            return false
        }
//        console.log(document.getElementById("mes1").value)
//        console.log(document.getElementById("mes2").value)
        var xhr = new XMLHttpRequest()
        xhr.open("GET", JSON.stringify({ "login" : document.getElementById("mes1").value, "pass" : document.getElementById("mes2").value}), true)
        xhr.onload = function () {
            var newMessages = JSON.parse(this.responseText)
            console.log(newMessages)
            if (newMessages.status == "ok") {
                document.cookie = "login=" + newMessages.name
                document.cookie = "pass=" + newMessages.pass
                setTimeout(profile, 50)
            }
            else {
                document.getElementById("error-message").innerHTML = "Неверный логин или пароль"
            }
        }
        xhr.send('')
        document.getElementById("mes1").value = ''
        document.getElementById("mes2").value = ''
        return true
    }
}
function profile() {
    window.location.href = "acc.html";
}
