document.addEventListener("DOMContentLoaded", () => {
  const toggleButtons = document.querySelectorAll('.toggle-btn');
  const toggleAllButton = document.getElementById('toggle-all');
  let allVisible = true;

  // Check if a visibility preference is stored
  const storedPreference = localStorage.getItem('codeBlocksVisible');
  if (storedPreference !== null) {
    allVisible = storedPreference === 'true';
    document.querySelectorAll('.code-block').forEach(block => {
      block.style.display = allVisible ? "block" : "none";
    });
    toggleButtons.forEach(button => {
      button.textContent = allVisible ? "Hide Code" : "Show Code";
    });
  }

  // Toggle individual code blocks
  toggleButtons.forEach(button => {
    button.addEventListener('click', function() {
      const codeBlock = this.nextElementSibling;
      // Use computed style in case inline style isn't set
      const isHidden = codeBlock.style.display === "none" || window.getComputedStyle(codeBlock).display === "none";
      codeBlock.style.display = isHidden ? "block" : "none";
      this.textContent = isHidden ? "Hide Code" : "Show Code";
      updateGlobalVisibility();
    });
  });

  // Toggle all code blocks at once
  toggleAllButton.addEventListener('click', () => {
    const codeBlocks = document.querySelectorAll('.code-block');
    codeBlocks.forEach(codeBlock => {
      codeBlock.style.display = allVisible ? "none" : "block";
    });
    toggleButtons.forEach(button => {
      button.textContent = allVisible ? "Show Code" : "Hide Code";
    });
    allVisible = !allVisible;
    localStorage.setItem('codeBlocksVisible', allVisible);
    toggleAllButton.textContent = "Toggle All Code";
  });

  // Update global visibility state and store preference
  function updateGlobalVisibility() {
    const codeBlocks = document.querySelectorAll('.code-block');
    allVisible = Array.from(codeBlocks).every(block => {
      return block.style.display !== "none" && window.getComputedStyle(block).display !== "none";
    });
    localStorage.setItem('codeBlocksVisible', allVisible);
  }
});
