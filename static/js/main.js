document.addEventListener("DOMContentLoaded", () => {
  const toggleButtons = document.querySelectorAll('.toggle-btn');
  const toggleAllButton = document.getElementById('toggle-all');
  let allVisible = true;

  // Retrieve stored visibility preference
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
      const isHidden = codeBlock.style.display === "none" || window.getComputedStyle(codeBlock).display === "none";
      codeBlock.style.display = isHidden ? "block" : "none";
      this.textContent = isHidden ? "Hide Code" : "Show Code";
      updateGlobalVisibility();
    });
  });

  // Toggle all code blocks
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

  /* --- Copy Button Functionality --- */
  // Add copy buttons to all code block containers if not already present
  const codeContainers = document.querySelectorAll('.code-block-container');
  codeContainers.forEach(container => {
    // Create a copy button if it doesn't exist
    if (!container.querySelector('.copy-btn')) {
      const copyBtn = document.createElement('button');
      copyBtn.classList.add('copy-btn');
      copyBtn.textContent = 'Copy';
      container.appendChild(copyBtn);
      // Add event listener for copy functionality
      copyBtn.addEventListener('click', () => {
        const codeBlock = container.querySelector('pre.code-block');
        copyTextToClipboard(codeBlock.innerText, copyBtn);
      });
    }
  });

  // Function to copy text to clipboard and provide feedback
  function copyTextToClipboard(text, button) {
    navigator.clipboard.writeText(text).then(() => {
      const originalText = button.textContent;
      button.textContent = "Copied!";
      setTimeout(() => {
        button.textContent = originalText;
      }, 2000);
    }).catch(err => {
      console.error("Failed to copy text: ", err);
    });
  }
});
