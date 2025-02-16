document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('calculate').addEventListener('click', () => {
        let num1 = parseFloat(document.getElementById('num1').value);
        let num2 = parseFloat(document.getElementById('num2').value);
        let operation = document.getElementById('operation').value;
        fetch(`/calculate?num1=${num1}&num2=${num2}&operation=${operation}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').innerText = `Result: ${data.result}`;
            });
    });
});
