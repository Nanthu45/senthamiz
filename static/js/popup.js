document.addEventListener('DOMContentLoaded', () => {
    const popup = document.getElementById('popup');
    const closePopup = document.getElementById('close-popup');
    let popupShownAbout = false; 
    let popupShownCategory = false; 

    const showPopup = () => {
        popup.style.display = 'flex';
        document.body.classList.add('popup-open'); 
    };

    const hidePopup = () => {
        popup.style.display = 'none';
        document.body.classList.remove('popup-open'); 
    };

    const checkScroll = () => {
        const aboutSection = document.getElementById('about-us');
        const categorySection = document.getElementById('categorysection');
        
        if (!aboutSection || !categorySection) return; 
        
        const aboutSectionTop = aboutSection.getBoundingClientRect().top;
        const categorySectionTop = categorySection.getBoundingClientRect().top;

        if (aboutSectionTop <= window.innerHeight * 0.5 && !popupShownAbout) {
            showPopup();
            popupShownAbout = true;
        } else if (categorySectionTop <= window.innerHeight * 0.5 && !popupShownCategory) {
            showPopup();
            popupShownCategory = true;
        }

        if (popupShownAbout && popupShownCategory) {
            window.removeEventListener('scroll', checkScroll);
        }
    };

    window.addEventListener('scroll', checkScroll);

    closePopup.addEventListener('click', hidePopup);

    window.addEventListener('click', (event) => {
        if (event.target === popup) {
            hidePopup();
        }
    });
});