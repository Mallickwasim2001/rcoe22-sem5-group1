const mobile_nav = document.querySelector(".mobile-navbar-btn");
const nav_header = document.querySelector(".header");

const toggleNavbar = () =>{
    nav_header.classList.toggle("active");
};

mobile_nav.addEventListener("click", () => toggleNavbar());

// Review Swiper
var swiper = new Swiper(".reviews-content", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: true,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    
  });


  // Email JS
  function validate() {
    let name = document.querySelector('.name');
    let email = document.querySelector('.email');
    let msg = document.querySelector('.message');
    let sendBtn = document.querySelector('.send-btn');

    sendBtn.addEventListener("click", (e) => {
      e.preventDefault();
      if(name.value == "" || email.value == "" || msg.value == ""){
        emptyerror();
      }
      else{
        sendmail (name.value,email.value,msg.value);
        success();
      }
    });

  }
  validate();

  function sendmail(name,email,msg){
    emailjs.send("service_2dd4ujn","template_9mrypwh",{
      from_name: email,
      to_name: name,
      message: msg,
      });
  }

  function emptyerror(){
    swal({
      title: "Oh No...",
      text: "Fields Cannot be Empty",
      icon: "error",
     
    });
  }

  function success(){
    swal({
      title: "Email Sent Successfully!!",
      text: "We try to reply as soon as Possible",
      icon: "Success",
     
    });
  }
