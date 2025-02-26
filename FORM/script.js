document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita el envío del formulario

    const email = document.querySelector('input[type="text"]').value;
    const password = document.querySelector('input[type="password"]').value;

  
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
      alert('Por favor, ingresa un correo electrónico válido.');
      return;
    }

    
    if (password.length < 6) {
      alert('La contraseña debe tener al menos 6 caracteres.');
      return;
    }

   
    alert('Formulario enviado con éxito.');
   
  });