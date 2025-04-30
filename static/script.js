
// Initialize items array
let items = [];

// Generate random items based on user input
function generateItems() {
    const numItems = parseInt(document.getElementById('numItems').value);
    if (numItems < 1 || numItems > 1000) {
        alert('Please enter a number between 1 and 1000.');
        return;
    }

    items = [];
    for (let i = 0; i < numItems; i++) {
        const weight = Math.floor(Math.random() * 100) + 1;
        const value = Math.floor(Math.random() * 100) + 1;
        items.push({ weight, value });
    }
    renderItems();
}

// Render items in a table
function renderItems() {
    const itemList = document.getElementById('itemList');
    itemList.innerHTML = '';

    items.forEach((item, index) => {
        const row = document.createElement('tr');
        row.className = 'hover:bg-gray-50';
        row.innerHTML = `
                    <td class="p-3">Item ${index + 1}</td>
                    <td class="p-3"><input type="number" class="item-weight w-full p-1 border rounded focus:ring-2 focus:ring-indigo-500" value="${item.weight}" min="1" data-index="${index}"></td>
                    <td class="p-3"><input type="number" class="item-value w-full p-1 border rounded focus:ring-2 focus:ring-indigo-500" value="${item.value}" min="1" data-index="${index}"></td>
                `;
        itemList.appendChild(row);
    });
}

// Add new item
function addItem() {
    items.push({ weight: 1, value: 1 });
    renderItems();
}

// Remove last item
function removeItem() {
    if (items.length > 0) {
        items.pop();
        renderItems();
    } else {
        alert('No items to remove.');
    }
}

// Clear all items
function clearItems() {
    items = [];
    renderItems();
    document.getElementById('solutionInfo').innerHTML = 'Select an algorithm and click "Solve" to find the best solution.';
    document.getElementById('solutionBody').innerHTML = '';
    document.getElementById('totalValue').textContent = '0';
    document.getElementById('totalWeight').textContent = '0';
}

// Update items array when inputs change
document.addEventListener('input', function (e) {
    if (e.target.classList.contains('item-weight')) {
        const index = parseInt(e.target.dataset.index);
        items[index].weight = parseInt(e.target.value) || 1;
    } else if (e.target.classList.contains('item-value')) {
        const index = parseInt(e.target.dataset.index);
        items[index].value = parseInt(e.target.value) || 1;
    }
});

// Solve the problem
async function solveProblem() {
    if (items.length === 0) {
        alert('Please generate or add items before solving.');
        return;
    }

    const solveButton = document.getElementById('solveButton');
    const loadingIndicator = document.getElementById('loadingIndicator');
    solveButton.disabled = true;
    solveButton.textContent = 'Solving...';
    loadingIndicator.classList.remove('hidden');

    const algorithm = document.getElementById('algorithm').value;
    const capacity = parseInt(document.getElementById('capacity').value);

    const weights = items.map(item => item.weight);
    const values = items.map(item => item.value);

    try {
        const response = await fetch('/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                weights: weights,
                values: values,
                capacity: capacity,
                algorithm: algorithm
            })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        displaySolution(data);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('solutionInfo').innerHTML = '<span class="text-red-600">Error solving the problem. Please try again.</span>';
    } finally {
        solveButton.disabled = false;
        solveButton.textContent = 'Solve Problem';
        loadingIndicator.classList.add('hidden');
    }
}

// Display the solution
function displaySolution(solution) {
    const solutionBody = document.getElementById('solutionBody');
    solutionBody.innerHTML = '';

    let algorithmName = '';
    switch (document.getElementById('algorithm').value) {
        case 'ga': algorithmName = 'Genetic Algorithm'; break;
        case 'aco': algorithmName = 'Ant Colony Optimization'; break;
        case 'pso': algorithmName = 'Particle Swarm Optimization'; break;
        case 'cs': algorithmName = 'Cuckoo Search'; break;
        case 'fa': algorithmName = 'Firefly Algorithm'; break;
    }

    document.getElementById('solutionInfo').innerHTML = `
                <strong class="text-gray-800">Algorithm:</strong> ${algorithmName}<br>
                <strong class="text-gray-800">Solution found:</strong> ${solution.solution.join(', ')}
            `;

    items.forEach((item, index) => {
        const row = document.createElement('tr');
        row.className = solution.solution[index] === 1 ? 'bg-green-100' : 'hover:bg-gray-50';
        row.innerHTML = `
                    <td class="p-3">Item ${index + 1}</td>
                    <td class="p-3">${item.weight}</td>
                    <td class="p-3">${item.value}</td>
                    <td class="p-3">${solution.solution[index] === 1 ? 'Yes' : 'No'}</td>
                `;
        solutionBody.appendChild(row);
    });

    document.getElementById('totalValue').textContent = solution.total_value;
    document.getElementById('totalWeight').textContent = solution.total_weight;
}

// Initialize with empty items
renderItems();

console.log('hello world')
