document.getElementById('delete-form').addEventListener('click', (e)=>{
    e.preventDefault();
    document.getElementById("register-form").reset();
    location.reload();
});
