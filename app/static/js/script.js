document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded!");

    // Smooth Scroll for Buttons
    document.querySelectorAll("button").forEach((button) => {
        button.addEventListener("click", function () {
            button.style.transform = "scale(0.95)";
            setTimeout(() => {
                button.style.transform = "scale(1)";
            }, 200);
        });
    });

    // File Upload Preview
    const fileInput = document.getElementById("file-upload");
    const preview = document.getElementById("file-preview");

    if (fileInput) {
        fileInput.addEventListener("change", function () {
            const file = this.files[0];
            if (file) {
                preview.innerHTML = `<p>📄 ${file.name}</p>`;
            } else {
                preview.innerHTML = "";
            }
        });
    }

    // Form Validation for Login/Register
    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");

    function validateForm(event, formType) {
        event.preventDefault();
        const email = document.getElementById(`${formType}-email`).value;
        const password = document.getElementById(`${formType}-password`).value;

        if (!email.includes("@") || password.length < 6) {
            alert("⚠️ Please enter a valid email and password (min 6 characters)");
        } else {
            alert("✅ Form submitted successfully!");
            event.target.submit();
        }
    }

    if (loginForm) {
        loginForm.addEventListener("submit", (event) => validateForm(event, "login"));
    }

    if (registerForm) {
        registerForm.addEventListener("submit", (event) => validateForm(event, "register"));
    }
});
