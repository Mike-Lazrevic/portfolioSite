function updateInputData() {
    const sourceMario = document.getElementById("sourceMario").value;
    const sourceEmpty = document.getElementById("sourceEmpty").value;
    const sourceTreasure = document.getElementById("sourceTreasure").value;

    fetch('/updateInputData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            sourceMario,
            sourceEmpty,
            sourceTreasure
        })
    })
    .then(response => {
        if (response.ok) {
            console.log('Input data updated successfully');
        } else {
            throw new Error('Failed to update input data');
        }
    })
    .catch(error => {
        console.error('Error updating input data:', error);
    });
}

function runMarioGame() {
    fetch('/runMarioGame', { method: 'POST' })
    .then(response => {
        if (response.ok) {
            return response.text();
        } else {
            throw new Error('Failed to run Mario game');
        }
    })
    .then(output => {
        const pythonShell = document.getElementById("shell-output");
        pythonShell.innerText = output;
    })
    .catch(error => {
        console.error('Error running Mario game:', error);
    });
}

function restart() {
    fetch('/restart', {
        method: 'POST'
    })
    .then(response => {
        if (response.ok) {
            console.log('Input data restarted successfully');
        } else {
            throw new Error('Failed to restart input data');
        }
    })
    .catch(error => {
        console.error('Error restarting input data:', error);
    });
}
