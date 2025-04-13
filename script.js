document.addEventListener('DOMContentLoaded', function () {
    function updateClock() {
      const now = new Date();
      const clock = document.getElementById('clock');
      const date = document.getElementById('date');
      clock.textContent = now.toLocaleTimeString('en-US', { hour12: false });
      date.textContent = now.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    }

    setInterval(updateClock, 1000);
    updateClock();

    // Tabs
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    const tabIndicator = document.querySelector('.tab-indicator');

    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelector('.tab-btn.active').classList.remove('active');
        btn.classList.add('active');

        tabContents.forEach(content => content.classList.remove('active'));
        document.getElementById(btn.dataset.tab).classList.add('active');

        tabIndicator.style.width = `${btn.offsetWidth}px`;
        tabIndicator.style.left = `${btn.offsetLeft}px`;
      });
    });
  });
  let isEditing = false;

  document.getElementById('edit-toggle').addEventListener('click', () => {
    isEditing = !isEditing;
    document.body.classList.toggle('editing-mode', isEditing);
  });
  document.querySelectorAll('.link-name').forEach(name => {
    name.addEventListener('click', (e) => {
      if (!isEditing) return;

      const newName = prompt('Edit link name:', name.textContent);
      if (newName) {
        name.textContent = newName;
      }
    });
  });
