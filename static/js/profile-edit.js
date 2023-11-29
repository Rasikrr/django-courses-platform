const sidebarMenu = document.querySelector(".sidebar");
const sidebarBtn = document.getElementById("menu-toggle-btn");

sidebarBtn.addEventListener("click", function (){
    if(sidebarMenu.style.display == "block"){
        sidebarMenu.style.display = "none";
    } else {
        sidebarMenu.style.display = "block";
    }
});