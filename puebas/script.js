document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navList = document.querySelector('.nav-list');

    // Menú hamburguesa
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navList.classList.toggle('active');
    });

    // Cerrar menú al hacer click en enlace
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
            // Solo para móviles
            if (window.innerWidth <= 700) {
                hamburger.classList.remove('active');
                navList.classList.remove('active');
            }
            
            // Scroll suave
            const targetId = link.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                e.preventDefault();
                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Formulario Newsletter
const newsletterForm = document.getElementById('newsletterForm');
const formMessage = document.querySelector('.form-message');
const submitBtn = document.getElementById('submitBtn');

async function handleSubmit(event) {
    event.preventDefault();
    submitBtn.classList.add('loading');
    
    const formData = new FormData(event.target);
    
    try {
        const response = await fetch('https://formspree.io/f/YOUR_FORM_ID', {
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        });
        
        if (response.ok) {
            showMessage('¡Gracias por suscribirte!', 'success');
            newsletterForm.reset();
        } else {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Error desconocido');
        }
    } catch (error) {
        showMessage(`Error: ${error.message}`, 'error');
    } finally {
        submitBtn.classList.remove('loading');
    }
}

function showMessage(text, type = 'success') {
    formMessage.textContent = text;
    formMessage.className = `form-message visible ${type}`;
    
    setTimeout(() => {
        formMessage.classList.remove('visible');
    }, 5000);
}

newsletterForm.addEventListener('submit', handleSubmit);



//*! Abrir Modal  */
var modal = document.getElementById("modalForm");

var btn = document.getElementById("openModal");


var span = document.getElementById("closeModal");

btn.onclick = function() {
    modal.style.display = "block";
}


span.onclick = function() {
    modal.style.display = "none";
}


window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}