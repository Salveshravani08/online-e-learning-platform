function showMore(section) {
    let info = document.getElementById(section + "-info"); // if section frontend hai to fronted para milega ,
    // backend hai to backend para milega and same for full stack
    // can also be access as :
    /* let frontend = document.getElementById("fronted-info");
    let backend = document.getElementById("backend-info");
    let fullstack = document.getElementById("fullstack-info");
    aise me sabhi variable ko same if else condition dena pdta , jise code ka length increase hojata
    ,so to avoid it we use : 
     let info = document.getElementById(section + "-info");
     jis btn me parameter('frontend-info','backend-info','fullstack-info') rhega vo card execute hoga
    */
    if (info.style.display === "block")
     {
        info.style.display = "none";
    } 
    else {
        info.style.display = "block";
    }
}