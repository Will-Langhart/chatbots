document.addEventListener("DOMContentLoaded", function() {
  // Select all toggle buttons
  const toggleButtons = document.querySelectorAll('.toggle-btn');
  
  toggleButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      // Find the next sibling element with the class 'code-block'
      const codeBlock = this.nextElementSibling;
      if (codeBlock.style.display === "none") {
        codeBlock.style.display = "block";
        this.textContent = "Hide Code";
      } else {
        codeBlock.style.display = "none";
        this.textContent = "Show Code";
      }
    });
  });
});
