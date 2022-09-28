// проверка утсройств

const isMobile = {
  Android: function() {
      return navigator.userAgent.match(/Android/i);
  },
  BlackBerry: function() {
      return navigator.userAgent.match(/BlackBerry/i);
  },
  iOS: function() {
      return navigator.userAgent.match(/iPhone|iPad|iPod/i);
  },
  Opera: function() {
      return navigator.userAgent.match(/Opera Mini/i);
  },
  Windows: function() {
      return navigator.userAgent.match(/IEMobile/i);
  },
  any: function() {
      return (isMobile.Android() || 
              isMobile.BlackBerry() || 
              isMobile.iOS() || 
              isMobile.Opera() || 
              isMobile.Windows());
  }
};

if( isMobile.any() ) {
  document.body.classList.add('_touch');
} else {
  document.body.classList.add('_pc');
}

// Меню бургер

const iconMenu = document.querySelector('.menu-icon');
const menuBody = document.querySelector('.menu-body');
if (iconMenu) {
  iconMenu.addEventListener("click", function (e) {
    document.body.classList.toggle('_lock');
    iconMenu.classList.toggle('_active');
    menuBody.classList.toggle('_active');
  });
}

// прокрутка при клике

const menuLinks = document.querySelectorAll('.menu-link[data-goto]');
if (menuLinks.length > 0) {
  menuLinks.forEach(menuLink => {
    menuLink.addEventListener("click", onMenuLinkClick);
  });
  
  function onMenuLinkClick(e) {
    const menuLink = e.target;
    if (menuLink.dataset.goto && document.querySelector(menuLink.dataset.goto)) {
      const gotoBlock = document.querySelector(menuLink.dataset.goto);
      const gotoBlockValue = gotoBlock.getBoundingClientRect().top + scrollY - document.querySelector('header').offsetHeight;
    
      if (iconMenu.classList.contains('_active')) {
        document.body.classList.remove('_lock');
        iconMenu.classList.remove('_active');
        menuBody.classList.remove('_active');
      }

      window.scrollTo({
        top: gotoBlockValue,
        behavior: "smooth"
      });
      e.preventDefault();  
    }
  }
}

// модалка

const formEl = document.querySelector('#matrix-container');
const explanationModal = document.querySelector('#modal-explanation');

formEl.addEventListener('submit', function(event) {
  event.preventDefault();

  explanationModal.classList.add('modal-active');
});

const closeButtons = document.querySelectorAll('.modal-close-button');

closeButtons.forEach( function(closeBtn) {
  closeBtn.addEventListener('click', function () {
    explanationModal.classList.remove('modal-active');
  });
});