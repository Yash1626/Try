document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('income').addEventListener('click', () => {
        let amount = prompt("Enter the amount to deposit:");
        if (amount) {
            fetch('/deposit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ amount: parseFloat(amount) })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Deposit successful!');
                } else {
                    alert('Deposit failed!');
                }
            });
        }
    });

    document.getElementById('expenses').addEventListener('click', () => {
        let amount = prompt("Enter the amount to spend:");
        if (amount) {
            fetch('/spend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ amount: parseFloat(amount) })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Expense recorded successfully!');
                } else {
                    alert('Expense recording failed!');
                }
            });
        }
    });

    document.getElementById('budget').addEventListener('click', () => {
        fetch('/get_budget')
        .then(response => response.json())
        .then(data => {
            if (data.budget_set) {
                alert(`Your current budget is ${data.budget}`);
            } else {
                let amount = prompt("Enter your budget for this month:");
                if (amount) {
                    fetch('/set_budget', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ amount: parseFloat(amount) })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            alert('Budget set successfully!');
                        } else {
                            alert('Failed to set budget!');
                        }
                    });
                }
            }
        });
    });
});
