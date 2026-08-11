// Unit Converter - Common logic for both blog post and dedicated page
const units = {
    length: ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches'],
    weight: ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces', 'tons'],
    temperature: ['celsius', 'fahrenheit', 'kelvin'],
    volume: ['liters', 'milliliters', 'gallons', 'quarts', 'cups', 'tablespoons', 'teaspoons'],
    area: ['square_meters', 'square_kilometers', 'square_feet', 'square_yards', 'acres', 'hectares'],
    speed: ['meters_per_second', 'kilometers_per_hour', 'miles_per_hour', 'feet_per_second', 'knots']
};

const unitLabels = {
    meters: 'Meters',
    kilometers: 'Kilometers',
    centimeters: 'Centimeters',
    millimeters: 'Millimeters',
    miles: 'Miles',
    yards: 'Yards',
    feet: 'Feet',
    inches: 'Inches',
    kilograms: 'Kilograms',
    grams: 'Grams',
    milligrams: 'Milligrams',
    pounds: 'Pounds',
    ounces: 'Ounces',
    tons: 'Tons',
    celsius: 'Celsius',
    fahrenheit: 'Fahrenheit',
    kelvin: 'Kelvin',
    liters: 'Liters',
    milliliters: 'Milliliters',
    gallons: 'Gallons',
    quarts: 'Quarts',
    cups: 'Cups',
    tablespoons: 'Tablespoons',
    teaspoons: 'Teaspoons',
    square_meters: 'Square Meters',
    square_kilometers: 'Square Kilometers',
    square_feet: 'Square Feet',
    square_yards: 'Square Yards',
    acres: 'Acres',
    hectares: 'Hectares',
    meters_per_second: 'Meters/Second',
    kilometers_per_hour: 'Kilometers/Hour',
    miles_per_hour: 'Miles/Hour',
    feet_per_second: 'Feet/Second',
    knots: 'Knots'
};

function updateUnits() {
    const category = document.getElementById('category').value;
    const fromUnit = document.getElementById('from-unit');
    const toUnit = document.getElementById('to-unit');
    
    const categoryUnits = units[category];
    
    fromUnit.innerHTML = '';
    toUnit.innerHTML = '';
    
    categoryUnits.forEach((unit, index) => {
        fromUnit.innerHTML += `<option value="${unit}">${unitLabels[unit]}</option>`;
        toUnit.innerHTML += `<option value="${unit}">${unitLabels[unit]}</option>`;
    });
    
    // Set default selections
    if (categoryUnits.length > 1) {
        toUnit.selectedIndex = 1;
    }
    
    convert();
}

async function convert() {
    const value = document.getElementById('value').value;
    const fromUnit = document.getElementById('from-unit').value;
    const toUnit = document.getElementById('to-unit').value;
    const category = document.getElementById('category').value;
    const resultDiv = document.getElementById('result');
    const formulaDiv = document.getElementById('formula');
    
    if (!value) {
        resultDiv.textContent = 'Enter a value to see the conversion';
        formulaDiv.textContent = '';
        return;
    }
    
    try {
        const response = await fetch('/api/v1/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                value: parseFloat(value),
                from_unit: fromUnit,
                to_unit: toUnit,
                category: category
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            resultDiv.textContent = 'Error: ' + data.error;
            formulaDiv.textContent = '';
            return;
        }
        
        resultDiv.textContent = `${data.value} ${unitLabels[fromUnit]} = ${data.result} ${unitLabels[toUnit]}`;
        formulaDiv.textContent = `Conversion: ${fromUnit} -> ${toUnit}`;
        
    } catch (error) {
        resultDiv.textContent = 'Error performing conversion';
        formulaDiv.textContent = '';
    }
}

// Initialize when DOM is ready
if (document.getElementById('unit-converter')) {
    document.addEventListener('DOMContentLoaded', function() {
        updateUnits();
    });
}
