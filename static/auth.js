async function auth_post(string) {
    const response = await fetch("/password_auth", {
        method: "POST",
        body: JSON.stringify({'password': string}),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
    });
    const json = await response.json()
    return json
}

async function auth_password() {
    const password = document.getElementById('password').value;
    if (password == '') {
        alert('Enter Password!');
    } else {
        const resp = await auth_post(password);
        const status = resp.Access
        console.log(status);
        
    }
    
}

async function set_check() {
    const response = await auth_post('con');
    const status = response.Access
    if (status == 'Set password') {
        return true
    } else {
        return false
    }
}



document.addEventListener("DOMContentLoaded", function() {
    if (set_check()) {
        document.getElementById("message_text").innerHTML = 'No admin password has set, enter the password to set one!';
    }
});