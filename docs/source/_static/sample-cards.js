document.addEventListener('DOMContentLoaded', function () {
    var modal = document.querySelector('.sample-modal');
    if (!modal) {
        return;
    }

    var body = modal.querySelector('.sample-modal-body');
    var title = modal.querySelector('.sample-modal-title');
    var closeButton = modal.querySelector('.sample-modal-close');
    var homes = new Map();
    var current = null;
    var lastFocus = null;

    function openDialog(id, label) {
        var detail = document.getElementById(id);
        if (!detail) {
            return;
        }
        lastFocus = document.activeElement;
        if (current) {
            homes.get(current).appendChild(current);
        }
        if (!homes.has(detail)) {
            homes.set(detail, detail.parentNode);
        }
        current = detail;
        title.textContent = label;
        body.appendChild(detail);
        modal.hidden = false;
        document.body.classList.add('sample-modal-open');
        closeButton.focus();
    }

    function closeDialog() {
        if (!current) {
            return;
        }
        homes.get(current).appendChild(current);
        current = null;
        modal.hidden = true;
        document.body.classList.remove('sample-modal-open');
        if (lastFocus && lastFocus.focus) {
            lastFocus.focus();
        }
    }

    document.querySelectorAll('.sample-card').forEach(function (card) {
        card.addEventListener('click', function () {
            var label = card.querySelector('.sample-card-title').textContent;
            openDialog(card.getAttribute('data-dialog'), label);
        });
    });

    modal.addEventListener('click', function (event) {
        if (event.target.closest('[data-close]')) {
            closeDialog();
        }
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && !modal.hidden) {
            closeDialog();
        }
    });
});
